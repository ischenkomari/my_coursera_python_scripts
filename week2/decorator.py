import functools
import json

def to_json(func):
    @functools.wraps(func)
    def wrapped():
        d=func()
        result = json.dumps(d)
        return result
    return wrapped

@to_json
def get_data():
  return {
    'data': 42
  }

print(get_data())  # вернёт '{"data": 42}'
print(get_data.__name__)
