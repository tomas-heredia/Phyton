diccionario = {
"nombre" : 'lucas',
"apellido" : 'dalto',
"subs": '10000'
}

#obtener laas claves
claves = diccionario.keys()

#obtener un valor por su clave
valor = diccionario.get("nombre")

#obteniendo un elemento dic_iterable 
diccionario_iterable = diccionario.items()

#eliminando un elelmento del dic
diccionario.pop("nombre","apellido")

#eliminando los elementos del diccionario
diccionario.clear()