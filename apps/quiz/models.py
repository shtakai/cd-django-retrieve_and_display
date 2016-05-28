from django.db import models


class Question(models.Model):
    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Meta:
        db_table = 'questions'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.TextField(max_length=200)

    class Meta:
        db_table = 'choices'


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'musicians'


class Album(models.Model):
    name = models.CharField(max_length=100)
    release_date = models.IntegerField()
    num_stars = models.IntegerField()
    musician = models.ForeignKey(Musician)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'albums'


class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

