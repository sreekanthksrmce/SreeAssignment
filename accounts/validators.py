import re

from django.core import validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class UnicodeUsernameIdValidator(validators.RegexValidator):
    regex = r"^[\d.@+-]+\Z"
    message = _(
        "Enter a valid username. This value may contain only Integers, "
        "numbers only."
    )
    flags = 0
