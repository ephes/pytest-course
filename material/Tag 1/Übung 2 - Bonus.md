```python

class Duck:
	def quack(self, volume):
        if volume < 0:
            return "..."
        if volume <= 20:
            return "quack"
        if volume <= 50:
            return "Quack"
        if volume <= 80:
            return "QUACK"
        return "QUAAAACK!"


from animals import Duck

def test_quack_volume():
    # Arrange
    daffy = Duck()
    quack_volumes = {
        10: "quack",
        40: "Quack",
        70: "QUACK",
        100: "QUAAAACK!",
        -5: "..."
    }

    # Act
    results = {volume: daffy.quack(volume) for volume in quack_volumes.keys()}

    # Assert
    assert results == quack_volumes, "The quack sounds are incorrect."

```