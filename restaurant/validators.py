from django.utils import timezone
from django.core.exceptions import ValidationError


def validate_date(date):
    if date < timezone.now():
        raise ValidationError("The booking date can't be in the past!")
