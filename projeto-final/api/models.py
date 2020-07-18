from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, validate_ipv4_address

import logging
from django.utils.translation import ugettext_lazy as _

LOG_LEVELS = (
    (logging.NOTSET, _('NotSet')),
    (logging.INFO, _('Info')),
    (logging.WARNING, _('Warning')),
    (logging.DEBUG, _('Debug')),
    (logging.ERROR, _('Error')),
    (logging.FATAL, _('Fatal')),
)


class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    last_login = models.DateTimeField('Último Login', auto_now=True)
    email = models.CharField('Email', max_length=254, validators=[EmailValidator()])
    password = models.CharField('Senha', max_length=50, validators=[MinLengthValidator(8)])

    def __str__(self):
        return str(self.name)

class Event(models.Model):
    title = models.CharField('Título', max_length=254)
    level = models.PositiveSmallIntegerField(choices=LOG_LEVELS, default=logging.ERROR, db_index=True)
    address = models.GenericIPAddressField('Endereço IP', max_length=39, validators=[validate_ipv4_address], null=True)
    date_event = models.DateTimeField(auto_now_add=True, verbose_name='Data do log')
    detail = models.TextField('Detalhe')
    trace = models.TextField(blank=True, null=True)
    arquivado = models.BooleanField('Arquivado', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ('-date_event',)
        verbose_name_plural = verbose_name = 'Log'