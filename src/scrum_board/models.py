from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)


class Card(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    owner = models.ForeignKey(User, verbose_name=('User'))
    created_date = models.DateField(blank=True, null=True)


class Board(models.Model):
    name = models.CharField(max_length=50)
    back_log = models.ManyToManyField(Card, related_name="backlog_id")
    todo = models.ManyToManyField(Card, related_name="todo_id")
    doing = models.ManyToManyField(Card, related_name="doing_id")
    done = models.ManyToManyField(Card, related_name="done_id")
