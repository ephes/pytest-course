from django.db import models
from mastodon import Mastodon


class Client(models.Model):
    api_base_url = models.URLField(verbose_name="API Base URL", unique=True)
    name = models.CharField(max_length=100, default="pytooterapp")
    remote_id = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)

    def __str__(self):
        return self.api_base_url

    def public_timeline(self):
        mastodon = Mastodon(api_base_url=self.api_base_url)
        return mastodon.timeline_public()


class Login(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
