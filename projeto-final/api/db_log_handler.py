import logging

db_default_formatter = logging.Formatter()


class DatabaseLogHandler(logging.Handler):
    def emit(self, record):
        from .models import Event

        trace = None

        if record.exc_info:
            trace = db_default_formatter.formatException(record.exc_info)

        if False:
            detail = self.format(record)
        else:
            detail = record.getMessage()

        kwargs = {
            'title': record.name,
            'level': record.levelno,
            'detail': detail,
            'trace': trace
        }

        Event.objects.create(**kwargs)

    def format(self, record):
        if self.formatter:
            fmt = self.formatter
        else:
            fmt = db_default_formatter

        if type(fmt) == logging.Formatter:
            record.message = record.getMessage()

            if fmt.usesTime():
                record.asctime = fmt.formatTime(record, fmt.datefmt)

            # ignore exception traceback and stack info

            return fmt.formatMessage(record)
        else:
            return fmt.format(record)