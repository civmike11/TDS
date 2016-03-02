from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from utility.models import CountryField


# Create your models here.
class Customer (models.Model):
    """
        Customer Model
    """

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    country = CountryField()
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=12)
    email_address = models.EmailField()

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Employee (models.Model):
    """
        Employee Model
        One to One to Builtin Django User Model
    """
    # Tuple of Departments
    dep = (('T', 'Technician'), ('O', 'Other'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(choices=dep, max_length=2)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

    @classmethod
    def get_technician_users(cls):
        return User.objects.filter(department='Technician')


class Ticket (models.Model):
    """
        Ticket Model
    """
    # List of Priority choices
    priority_choices = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    )
    # ticket Status
    status_choices = (
        ('R', 'Ready'),
        ('IP', 'In Progress'),
        ('WP', 'Waiting on Part'),
        ('WC', 'Waiting on Customer'),
        ('C', 'Completed')
    )

    ticket_id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(Customer)
    priority = models.CharField(choices=priority_choices, default=None, max_length=2)
    created_by = models.TextField(max_length=30)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    status = models.CharField(choices=status_choices, default=status_choices[0][0], max_length=2)
    issue_type = models.CharField(max_length=30)
    issue = models.TextField(max_length=255)
    assigned_tech = models.CharField(max_length=30)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.ticket_id







