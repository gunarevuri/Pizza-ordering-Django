from django.db import models

class PizzaModel(models.Model):
	name = models.CharField(max_length = 10)
	price =  models.CharField(max_length = 10)

class CustomerModel(models.Model):
	userid = models.CharField(max_length = 10)
	phoneno = models.IntegerField()


class OrderModel(models.Model):
	username = models.CharField(max_length = 10)
	phoneno = models.IntegerField(default = 0)
	address = models.CharField( max_length = 100)
	ordereditems = models.CharField(max_length = 100)
	status = models.CharField(max_length = 10, default = 'pending')




# Create your models here.
