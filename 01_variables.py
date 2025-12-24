#variables
my_string_variable = "String"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)
print(type(my_int_variable))
#concatenación de cadenas.
print(my_string_variable, my_int_variable)

#Tipo: none_type
print(type(print(my_string_variable, my_int_variable)))

#Algunas funciones del sistema
#len() cuenta caracteres de un string
print(len(my_string_variable))

#Variables en una sola línea
name, surname, alias, age = "Simón", "Kwon", "Saimon", 22
print("My name is:", name, surname, "My age is", age, "and people say", alias)

#Inputs
name = input("¿Cuál es tu nombre?")
age = input("¿Cuántos años tienes?")
print(name)
print(age)