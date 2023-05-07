from django.db import models
from mastodon import Mastodon


class Client(models.Model):
    name = models.CharField(max_length=100, default="pytooterapp")
    remote_id = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)

    def __str__(self):
        return f"<{self.name}>"

    def set_remote_id_and_secret(self, api_base_url):
        self.remote_id, self.secret = Mastodon.create_app(self.name, api_base_url=api_base_url)

    @classmethod
    def from_api_base_url(cls, api_base_url, name=None):
        client = cls()
        if name is not None:
            client.name = name
        client.set_remote_id_and_secret(api_base_url)
        return client


class Server(models.Model):
    api_base_url = models.URLField(verbose_name="API Base URL", unique=True)
    client = models.OneToOneField(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name="server")

    def __str__(self):
        return self.api_base_url

    def get_access_token(self, username, password):
        if self.client is None:
            self.client = Client.from_api_base_url(self.api_base_url)

        mastodon = Mastodon(
            client_id=self.client.remote_id,
            client_secret=self.client.secret,
            api_base_url=self.api_base_url,
        )
        return mastodon.log_in(username, password)

    def public_timeline(self):
        mastodon = Mastodon(api_base_url=self.api_base_url)
        return mastodon.timeline_public()


class Login(models.Model):
    server = models.ForeignKey(Server, on_delete=models.CASCADE, related_name="logins")
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