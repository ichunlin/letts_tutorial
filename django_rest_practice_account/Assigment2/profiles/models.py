from django.db import models
from django.forms.fields import RegexField
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.validators import RegexValidator

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.
class loginModel(models.Model):
    email = models.EmailField(max_length=400, blank=False)
    password = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('created',) #?????

# Create your models here.
class ProfileModel(models.Model):
    #ProfileModel {first_name, last_name, email, phoneNo)
    #r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    email = models.EmailField(max_length=400, blank=False, 
    validators=[
            RegexValidator(
                regex='(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
                message='incorrect email address',
            ),
        ])
    first_name = models.CharField(max_length=100, blank=False) 
    last_name = models.CharField(max_length=100, blank=False)
    #"^[0-9]{10}$"
    #phoneNo = RegexField(regex=r'^[0-9]{10}$')
    phoneNo = models.CharField(max_length=10, blank=False, 
    validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message='Phone number is not correct,it needs 10 digit',
            ),
        ])
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('created',) #?????