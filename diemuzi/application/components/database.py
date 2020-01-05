"""
Database Configuration
"""

# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DATABASE',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'HOSTNAME',
        'PORT': 5432,
        'TEST': {
            'NAME': 'test_DATABASE'
        },
        'ATOMIC_REQUESTS': True
    },
    'default_slave1': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'DATABASE',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'HOSTNAME',
        'PORT': 5432,
        'TEST': {
            'MIRROR': 'default'
        },
        'ATOMIC_REQUESTS': False
    }
}

# Database Routers
DATABASE_ROUTERS = [
    'database.router.MasterSlave'
]
