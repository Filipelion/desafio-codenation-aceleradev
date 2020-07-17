from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, validate_ipv4_address
import logging

def validate_level(level):
    options = ('CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO')
    if level not in options:
        raise Exception('Level not allowed')

class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    last_login = models.DateTimeField('Último Login', auto_now=True)
    email = models.CharField('Email', max_length=254, validators=[EmailValidator()])
    password = models.CharField('Senha', max_length=50, validators=[MinLengthValidator(8)])

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField('Título', max_length=254)
    level = models.CharField('Nível', max_length=20, validators=[validate_level])
    address = models.GenericIPAddressField('Endereço IP', max_length=39, validators=[validate_ipv4_address])
    date_event = models.DateTimeField('Data do log', auto_now=True)
    detail = models.TextField('Detalhe')
    arquivado = models.BooleanField('Arquivado')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.level