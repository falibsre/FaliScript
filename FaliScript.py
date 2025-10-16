import importlib
def написать(текст):
  print(текст)
def счетчик(мин, макс, шаг):
    for i in range(мин, макс, шаг):
        print(i)
def импорт(модуль):
  return importlib.import_module(модуль)
