my_dict = { 'Igor': 1986, 'Vadim': 1995 , 'Mariya': 1986}
print(my_dict)
print(my_dict.get('Igor'))
print(my_dict.get('Denis'))
a = my_dict.pop('Vadim')
print(a)
my_dict.update({'Sofia': 2002,
                'Dima': 2009})
print(my_dict)



my_set = { 1,3,4,5,'Яблоко',45.85634,1,2,3,4,}
print(my_set)
my_set.add(8)
my_set.add(6)
my_set.discard('Яблоко')
print(my_set)
