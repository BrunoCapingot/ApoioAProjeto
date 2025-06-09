from django.db import models

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    categoria = models.CharField(max_length=10)

    def __str__(self):
        return self.usuario

class CadastroDeUsuario(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    equipe = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario

class Refatoracao(models.Model):
    id = models.AutoField(primary_key=True)
    projeto = models.CharField(max_length=100)
    equipe = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario