class Field:
    def __init__(self, value, validator=None):
        self.value = value
        self.validator = validator
        self._validate()

    def _validate(self):
        if self.validator and not self.validator(self.value):
            raise ValueError(f"Invalid value for field: {self.value}")

    def __str__(self):
        return self.value