import pytz
from django.conf import settings
from django.contrib.auth import models as auth_models
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _

TIME_ZONE_CHOICES = (
    sorted([(x, x) for x in pytz.all_timezones_set])
)


class UserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)

        if password is None:
            password = self.make_random_password()

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        subject = 'User Registration - Diemuzi.com'

        message = "Hey,\n\n"
        message += "Thank you for registering on https://diemuzi.com\n\n"
        message += "Here are a few details you will need:\n\n"
        message += "Username: %s\n" % email
        message += "Password: %s\n\n" % password
        message += "After logging in, please change your password.\n\n"
        message += "Thank you,\n"
        message += "~ Sammie S. Taunton"

        email_from = settings.DEFAULT_FROM_EMAIL
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class AccessLog(models.Model):
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=False,
        null=False
    )

    date_from = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created On')
    )

    ipaddress = models.GenericIPAddressField(
        verbose_name=_('IP Address'),
        blank=False,
        null=False
    )

    reverse_ipaddress = models.TextField(
        verbose_name=_('Reverse IP Address'),
        blank=True,
        null=True
    )

    class Meta:
        db_table = 'access_log'

        default_permissions = ('view',)

    @staticmethod
    def search(account_id, **kwargs):
        search_params = {
            'ipaddress': 'icontains',
            'reverse_ipaddress': 'icontains'
        }

        query = {}

        for key, value in kwargs.items():
            if value is None:
                del kwargs[key]

            if key in search_params:
                query[key + '__' + search_params[key]] = kwargs[key]

        return AccessLog.objects.filter(account_id=account_id, **query)


class Account(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    class Comment(models.IntegerChoices):
        NORMAL = 0, _('Normal - Oldest to Newest')
        REVERSE = 1, _('Reverse - Newest to Oldest')

    class FormDisplay(models.TextChoices):
        COMPACT = 'compact', _('Compact')
        EXPAND = 'expand', _('Expanded')

    class HelpText(models.IntegerChoices):
        NO = 0, _('No')
        YES = 1, _('Yes')

    class Locale(models.TextChoices):
        DE = 'de', _('German')
        EN = 'en', _('English')

    class TimeFormat(models.TextChoices):
        LAMEN_LONG = 'l, F d, Y g:i:s A', 'Sunday, January 01, 2000 1:00:00 PM'
        LAMEN_MED = 'F d, Y g:i:s A', 'January 01, 2000 1:00:00 PM'
        LAMEN_SHORT = 'Y-m-d g:i:s A', '2000-01-01 1:00:00 PM'
        STANDARD_LONG = 'l, F d, Y H:i:s', 'Sunday, January 01, 2000 13:00:00'
        STANDARD_MED = 'F d, Y H:i:s', 'January 01, 2000 13:00:00'
        STANDARD_SHORT = 'Y-m-d H:i:s', '2000-01-01 13:00:00'

    comment_order = models.IntegerField(
        choices=Comment.choices,
        default=0,
        verbose_name=_('Comment Order'),
        help_text=_('Choose how comments should be displayed.')
    )

    date_from = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Created On')
    )

    email = models.EmailField(
        validators=[
            validators.MinLengthValidator(5),
            validators.EmailValidator
        ],
        verbose_name=_('Email Address'),
        unique=True,
        blank=False,
        null=False,
        help_text=_('Email address for any notifications.')
    )

    first_name = models.CharField(
        max_length=255,
        validators=[
            validators.RegexValidator('^[a-zA-Z .\'-]+$')
        ],
        verbose_name=_('First Name'),
        blank=False,
        null=False,
        help_text=_('Your legal first name.')
    )

    form_display = models.CharField(
        max_length=7,
        choices=FormDisplay.choices,
        default='expand',
        verbose_name=_('Form Display'),
        blank=False,
        null=False,
        help_text=_('Choose how forms should be displayed.')
    )

    help_text = models.IntegerField(
        choices=HelpText.choices,
        default=1,
        verbose_name=_('Help Text'),
        help_text=_('Choose if help text should be displayed.')
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    last_name = models.CharField(
        max_length=255,
        validators=[
            validators.RegexValidator('^[a-zA-Z .\'-]+$')
        ],
        verbose_name=_('Last Name'),
        blank=False,
        null=False,
        help_text=_('Your legal last name.')
    )

    locale = models.CharField(
        max_length=2,
        choices=Locale.choices,
        default='en',
        verbose_name=_('Language'),
        blank=False,
        null=False,
        help_text=_('Choose a default language.')
    )

    time_format = models.CharField(
        max_length=255,
        choices=TimeFormat.choices,
        default='Y-m-d H:i:s',
        verbose_name=_('Time Format'),
        blank=False,
        null=False,
        help_text=_('Choose a preferred time format.')
    )

    time_zone = models.CharField(
        max_length=32,
        choices=TIME_ZONE_CHOICES,
        default='UTC',
        verbose_name=_('Time Zone'),
        blank=False,
        null=False,
        help_text=_('Choose a preferred time zone.')
    )

    REQUIRED_FIELDS = ['first_name', 'last_name']
    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        db_table = 'account'

        permissions = [
            ('change_manage', 'Can change manage'),
            ('change_password', 'Can change password'),
            ('change_permission', 'Can change permissions'),
            ('view_manage', 'Can view manage'),
            ('view_password', 'Can view password'),
            ('view_permission', 'Can view permissions')
        ]

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def create_account(self):
        extra_fields = {}

        extra_fields.setdefault('first_name', self.first_name)
        extra_fields.setdefault('last_name', self.last_name)

        user = Account.objects.create_user(email=self.email, **extra_fields)

        group = auth_models.Group.objects.get(name='Client')
        group.user_set.add(user)

    @staticmethod
    def search(**kwargs):
        search_params = {
            'first_name': 'icontains',
            'last_name': 'icontains',
            'email': 'icontains'
        }

        query = {}

        for key, value in kwargs.items():
            if value is None:
                del kwargs[key]

            if key in search_params:
                query[key + '__' + search_params[key]] = kwargs[key]

        return Account.objects.filter(is_superuser=False, **query)
