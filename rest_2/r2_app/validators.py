from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


def validate_username(value):
    try:
        User.objects.get(username=value)
        raise ValidationError("User exists")
    except User.DoesNotExist:
        pass

