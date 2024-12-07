import inspect
import colorama as c
print(dir(c))
print(type(c))
print(hasattr(c, "Cursor")) # Показывает курсор
print(getattr(c, "Style")) # Меняет стиль
print(inspect.getdoc(c)) # Нет документации для этого модуля, поэтому в консоль выводится "None"