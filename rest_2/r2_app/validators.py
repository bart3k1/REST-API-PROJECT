from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


def validate_username(value):
    try:
        User.objects.get(username=value)
        raise ValidationError("User exists")
    except User.DoesNotExist:
        pass

