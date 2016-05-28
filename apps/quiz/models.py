from django.db import models
from datetime import datetime


class Question(models.Model):
    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField(datetime.now())

    def __str__(self):
        return self.question_text

    class Meta:
        db_table = 'questions'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.TextField(max_length=200)

    def __str__(self):
        return self.choice_text

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


class Manufacturer(models.Model):

    class Meta:
        db_table = 'manufacturers'


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer)

    class Meta:
        db_table = 'cars'


class Topping(models.Model):
    class Meta:
        db_table = 'toppings'


class Pizza(models.Model):
    topping = models.ManyToManyField(Topping)

    class Meta:
        db_table = 'pizzas'


class Customer(models.Model):

    class Meta:
        db_table = 'customers'


class CustomerDetail(models.Model):
    customer = models.OneToOneField(Customer)

    class Meta:
        db_table = 'customer_details'
