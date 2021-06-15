from django.db import models

# Create your models here.

TITLE_CHOICES = {
    ('Ms', 'Ms'),
    ('Miss', 'Miss'),
    ('Mrs', 'Mrs'),
    ('Mr', 'Mr'),
    ('Dr', 'Dr'),
}


class UserProfile(models.Model):
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    first_name = models.CharField(max_length=60, default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.first_name
