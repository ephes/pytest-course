```shell
cd tests
```

```python first_tests.py
from .first import add_numbers  
  
  
def test_passing():  
	assert (1, 2, 3) == (1, 2, 3)  
  
  
def test_add_numbers():  
	assert add_numbers(1, 2) == 3
```

```python first.py
def add_numbers(a, b):  
	return a + b  
  
  
def concat_strings(a, b):  
	return a + b
```

```python second_test.py
def test_failing():  
	assert (1, 2, 3) == (3, 2, 1)
```
