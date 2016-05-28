from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)
    interest = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}:{}'.format(str(self.id), self.name)

    class Meta:
        db_table = 'users'
