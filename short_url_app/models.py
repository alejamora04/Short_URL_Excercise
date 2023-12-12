from django.db import models

import string
import secrets


# Create your models here.
class UrlHandler(models.Model):

    original_url = models.TextField()
    url_suffix = models.CharField(max_length=7, blank=True, null=True)

    # Generate URL suffix via model save() methods upon object save.
    def save(self):
        # Leverage python's crytography secrets module to generate alphanumeric strings.
        def generate_url_string():
            # Set the length of the url suffix.
            N = 7

            # select random alphanumeric characters among ascii letters (which includes upper, lowercase)
            url_string = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(N))
            return url_string
        
        self.url_suffix = generate_url_string()
        super(UrlHandler, self).save()
