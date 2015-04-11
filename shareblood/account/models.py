"""
shareblood.account.models
~~~~~~~~~~~~~~~~~~~~~~~~~

Account models.
It can be either a common user or an organization.
"""


from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import ugettext_lazy as _

from custom_user.models import AbstractEmailUser

from shareblood import constants


GENDER_CHOICES = (('m', _('Masculino')),
                  ('f', _('Feminino')))


DEFAULT_URL_IMAGE = 'http://www.randomimage.com/random.jpg'

class CustomAccount(AbstractEmailUser):
    """
    CustomAccount class.
    """
    REQUIRED_FIELDS = ['name', 'gender', 'birth_date']

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    site = models.CharField(max_length=255, null=True, blank=True)
    image = models.URLField(default=DEFAULT_URL_IMAGE, blank=True)
    about = models.TextField(null=True)
    blood_type = models.CharField(max_length=2, choices=constants.BLOOD_TYPES)
    role = models.ForeignKey(Group, null=True)
    #location = models.ForeignKey('location.Location')
