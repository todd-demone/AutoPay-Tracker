from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    card = models.ForeignKey('Card', on_delete=models.SET_NULL, null=True) # set null to True so if card is deleted then vendor is NOT deleted.
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('vendor_update_form', args=[str(self.id)])
    
class Card(models.Model):
    TYPE_CHOICES = (
        ('American Express', 'American Express'),
        ('Mastercard', 'Mastercard'),
        ('Visa', 'Visa'),
    )
    nickname = models.CharField(max_length=50)
    name_on_card = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="American Express")
    card_number = models.CharField(max_length=16, validators=[RegexValidator(r'^\d{1,16}$', message='Card number has to be 16 digits, no spaces')])
    security_code = models.CharField(max_length=4, validators=[RegexValidator(r'^\d{1,4}$', message='Security code has to be 3 or 4 digits, no spaces')])
    expiry_date = models.DateField()
    
    
    def __str__(self):
        return self.nickname
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('card_update_form', args=[str(self.id)])
    
