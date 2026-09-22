```python

from django.db.utils import IntegrityError


@pytest.mark.django_db  
	def test_account_without_server_fail():  
	account = models.Account(username="foo@example.com",access_token="test_token")  
	with pytest.raises(IntegrityError):  
	account.save()
```