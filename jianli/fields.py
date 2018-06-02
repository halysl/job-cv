from django.db import models
import ast
import json

class ListField(models.TextField):
    
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []
        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return str(value)

    def value_to_string(self, onj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)

class StringListField(models.Model):
    data = models.CharField(max_length=500)
    def set(self, value):
        self.data = json.dumps(value)
    def get(self):
        return dump.loads(self.data)