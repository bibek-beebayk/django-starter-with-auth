from django.utils import timezone

USERNAME_FIELD = "email"
USE_OTP_VALIDATION = True
OTP_LENGTH = 4

# Database settings
DATABASE_NAME = "django_auth"
DATABASE_USER = "postgres"
DATABASE_PASSWORD = ""
DATABASE_HOST = ""
DATABASE_PORT = ""

# Email Settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'beebayk63478@gmail.com'
EMAIL_HOST_PASSWORD = 'htqryayloavyjbmm'
EMAIL_USE_TLS = True

# JWT token settings
JWT_ACCESS_TOKEN_LIFETIME = timezone.timedelta(minutes=60)
JWT_REFRESH_TOKEN_LIFETIME = timezone.timedelta(days=1)

# Custom Response
ALLOW_NULL_VALUES_IN_RESPONSE = True
'''
If false, the null values in response are replaced by some default value.
IntegerField: 0
FloatField: 0.0
CharField: ""
.... and so on.
'''