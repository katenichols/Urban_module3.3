# распаковка словаря

def print_params(**kwargs):
  for key, value in kwargs.items():
    print(key,value)
    

dict_ = {'a': 1, 'b': 2, 'd': 3}
print_params(**dict_)


# распаковка составных параметров

def print_params1(a, b, c):
  print(a, b, c)
    

list_ = [1, 2]
dict_ = {'c': 3}
print_params1(*list_, **dict_)
