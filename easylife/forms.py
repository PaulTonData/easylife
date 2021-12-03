import unicodedata

from django.contrib.auth import get_user_model
from django.core.validators import ValidationError
from django.utils.deconstruct import deconstructible
from django_registration.forms import RegistrationForm
from django_registration import validators

User = get_user_model()

@deconstructible
class StevensDomainValidator:
    """
    Validator which checks if e-mail ends with stevens.edu
    """

    def __init__(self, model, field_name, error_message):
        self.model = model
        self.field_name = field_name
        self.error_message = error_message
    
    def __call__(self, value):
        if not isinstance(value, str):
            return
        value = unicodedata.normalize("NFKC", value).casefold()

        if not value.endswith("stevens.edu"):
            raise ValidationError(self.error_message, code="invalid")

DOMAIN_ERROR = "Email address must be a stevens.edu email."

class RegistrationFormStevensEmail(RegistrationForm):
    """
    Subclass of ``RegistrationForm`` which enforces stevens.edu domain
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        email_field = User.get_email_field_name()
        self.fields[email_field].validators.append(
            StevensDomainValidator(
                User, email_field, DOMAIN_ERROR
            )
        )