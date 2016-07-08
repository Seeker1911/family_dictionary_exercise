my_family = { 'sister': { 'name': 'Ali', 'age': 26 }, 'brother': { 'name': 'Lane', 'age': 27 } } 

for key, value in my_family.items():
	sibling = key
	name = value['name']
	age = value['age']
	print(sibling)
	print(name)
	print(age)
	readable = '{0} is my {1} and is {2} years old. '.format(name, sibling, age)
	print(readable)
