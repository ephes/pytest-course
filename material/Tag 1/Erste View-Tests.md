```python views_test.py
from django.urls import reverse  
  
  
def test_get_create_server(client):  
	server_list = reverse("locnus:get-create-server")  
	response = client.get(server_list)  
	assert response.status_code == 200
```

```python
from http import HTTPStatus

# ginge auch, ich mache das aber nicht..
assert response.status_code == HTTPStatus.ok  
```
