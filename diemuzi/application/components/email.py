"""
Email Settings
"""

# Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Hostname
EMAIL_HOST = 'HOSTNAME'

# Username
EMAIL_HOST_USER = 'USERNAME'

# Password
EMAIL_HOST_PASSWORD = 'PASSWORD'

# Port
EMAIL_PORT = 587

# TLS Support
EMAIL_USE_TLS = True

# From Email Address
DEFAULT_FROM_EMAIL = 'FROM_EMAIL_ADDRESS'

#
# Set the administrator email address(es)
#
# Only used when important notications need to be sent
# Example; Queue failed to process
#
# For more than 1 admin, recommended to use a mailing list address here
ADMINS = [
    'ADMIN_EMAIL_ADDRESS'
]

#
# Set the manager email address(es)
#
# Only used when DEBUG is False
# Example; 404 Errors
#
# For more than 1 manager, recommended to use a mailing list address here
MANAGERS = [
    'MANAGER_EMAIL_ADDRESS'
]
