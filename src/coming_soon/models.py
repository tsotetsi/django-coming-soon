from django.db import models


class PrelaunchSignUp(models.Model):
    """Prelaunch SignUp model."""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} ({}) signed-up on {}".format(self.name, self.email, self.created)
