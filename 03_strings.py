#Strings
my_string = 'string'
my_other_string = "mi otro string"
print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)

my_new_string = "String con\nsalto de linea"
print(my_new_string)

my_string_tab = "\tString con tabulación"
print(my_string_tab)

#Formateo 
name, surname, age = "Simón", "Kwon", 22

print("Mi nombre es {} {}, mi edad es {} años".format(name, surname, age))
print("Mi nombre es %s %s, mi edad es %d años"%(name, surname, age))

#Desempaquetado de caracteres

language = "python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)

#Divisón 
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-2]
print(language_slice)

#Reverse
reversed_language = language[::-1]
print(reversed_language)
