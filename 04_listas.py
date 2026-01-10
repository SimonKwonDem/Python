#Listas

my_list = list ()
print(len(my_list))

my_list = [1,54,23,88,88]
print(my_list)
print(len(my_list))

my_other_list = [24,"simon", 177, "José"]
print(my_other_list)
print(type(my_other_list))

print(my_other_list[1])
#Función count, cuenta cant de veces que se repite dato en una lista.
print(my_list.count(88))

age, name, height, surname = my_other_list
print(height)

#Se concatenan dos listas y se imprimen en una misma linea
print(my_list + my_other_list)

#Algunas funciones para trabajar las listas.
my_other_list.append(2003)
print(my_other_list)

my_other_list.insert(1,"rojo")
print(my_other_list)

#Accedemos al índice del color y lo modificamos
my_other_list[1] = "verde"
print(my_other_list)

my_other_list.remove("verde")
print(my_other_list)

#De esta manera .pop() elimina por defecto el último valor
print(my_other_list.pop())
print(my_other_list)

#De esta manera .pop() elimina el valor del índice indicado
my_other_list.pop(1)
print(my_other_list)

#guardamos una copia de la lista en una nueva referencia.
my_new_list = my_list.copy()
my_list.clear()
print(my_list)
print(my_new_list)

#Da vuelta el orden de la lista.
my_new_list.reverse()
print(my_new_list)

#Ordena alfabéticamente o de menor a mayor por defecto.
my_new_list.sort()
print(my_new_list)

#De esta manera se pueden realizar subListas
print(my_new_list[1:3])

#Cambio el tipo de dato de mi variable my_list, tipado dinámico
my_list = "Hola Python"
print(my_list)