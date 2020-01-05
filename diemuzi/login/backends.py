from django.contrib.auth import backends


class AuthBackend(backends.ModelBackend):
    def user_can_authenticate(self, user):
        """
        Reject users with is_active=False.
        """

        is_active = getattr(user, 'is_active', None)

        if is_active:
            return True
        else:
            return False
