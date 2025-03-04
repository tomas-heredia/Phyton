#creando lista con list()
lista = list(["hola","tomas", True])

resultado = len(lista) #cantidad de elementos de la lista 

#agregando elementos a la lista con append

lista.append("jajaja")

#agregando elementso a la lista con un indice especifico
lista.insert(2,"queso")

#agregando varios elementos a la lista

lista.extend([False,2025])

#eliminando elementos por su indice

lista.pop(0)
lista.pop(-1) #elimina el ultimo elemento 
lista.pop(-2) #elimina el anteultimo y asi sucesivamente

#removiendo un elemento por su valor
lista.remove("hola")

#eliminando todo elemento de la lista
lista.clear()

#ordena de menor a mayor, pero no puede tener cadenas de texto
lista.sort()
lista.sort(reverse=True) #de mayor a menor

#invierte los elementos de la lista
lista.reverse()
