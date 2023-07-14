import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import transaction
from django_countries.fields import CountryField

from cloudinary.models import CloudinaryField
from phonenumber_field.modelfields import PhoneNumberField
from custom.models import User
from model.common_fields import BaseModel


class Vendor(BaseModel):
    """Vendor model for storing vendor information"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    GENDER_SELECT = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=100, choices=GENDER_SELECT)
    store_name = models.CharField(max_length=100)
    
    store_address = models.CharField(max_length=100)
    store_phone = PhoneNumberField(
        verbose_name="Phone Number", region="TA", default="+255"
    )
    description = models.CharField(max_length=100)
    store_logo = CloudinaryField("logo", null=True, blank=True)

    """Personal details"""
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    country_of_citizenship = CountryField()
    country_of_birth = CountryField()
    date_of_birth = models.DateField(null=True)

    country_of_residence = CountryField()
    postal_code = models.CharField(max_length=100)
    address_line1 = models.CharField(max_length=100)
    address_line2 = models.CharField(max_length=100)
    city = models.CharField(max_length=100, verbose_name="Town")
    state = CountryField(verbose_name="Region")

    personal_phone = PhoneNumberField(
        verbose_name="Phone Number", region="TA", default="+255"
    )

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = _("Vendors")
