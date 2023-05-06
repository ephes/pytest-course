from django.db import models
from mastodon import Mastodon


class Server(models.Model):
    api_base_url = models.URLField(verbose_name="API Base URL", unique=True)
    client_name = models.CharField(max_length=100, default="pytooterapp")
    client_id = models.CharField(max_length=100)
    client_secret = models.CharField(max_length=100)

    def __str__(self):
        return self.api_base_url

    def create_client(self):
        self.client_id, self.client_secret = Mastodon.create_app(self.client_name, api_base_url=self.api_base_url)

    def get_access_token(self, username, password):
        mastodon = Mastodon(
            client_id=self.client_id,
            client_secret=self.client_secret,
            api_base_url=self.api_base_url,
        )
        return mastodon.log_in(username, password)

    def public_timeline(self):
        mastodon = Mastodon(api_base_url=self.api_base_url)
        return mastodon.timeline_public()


class Login(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)

    def __str__(self):
        return f"<{self.username}, {self.server}>"

    def personal_timeline(self):
        mastodon = Mastodon(
            access_token=self.access_token,
            api_base_url=self.server.api_base_url,
        )
        return mastodon.timeline_home()
