import inspect
import types

def introspection_info(obj):
    info = {}

    info['type'] = type(obj).__name__

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes


    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods

    # Модуль, к которому объект принадлежит
    info['module'] = getattr(obj, '__module__', 'N/A')

    # Дополнительные свойства
    if isinstance(obj, types.FunctionType):
        info['signature'] = inspect.signature(obj)
        info['docstring'] = inspect.getdoc(obj)
    elif isinstance(obj, types.MethodType):
        info['signature'] = inspect.signature(obj)
        info['docstring'] = inspect.getdoc(obj)
    elif isinstance(obj, (list, tuple, set, frozenset)):
        info['length'] = len(obj)
    elif isinstance(obj, dict):
        info['keys'] = list(obj.keys())

    return info

# Пример использования
number_info = introspection_info(42)
print(number_info)

class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        pass

my_object = MyClass(10)
object_info = introspection_info(my_object)
print(object_info)
