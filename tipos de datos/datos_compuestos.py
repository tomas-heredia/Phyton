lista = [4,5]
lista2 = ["hola","mundo", True, 123]
print(lista2)
print(lista[1])

#igual que lista pero no se puede modificar
tupla = ("hola","mundo", True, 123)

#esto es valido 
lista[1] = 6

#esto no es valido
#tupla[1] = "chau"


#creando un conjunto (set) 
#no se pueden modificar sus elementos pero si su distribucion 
#no perminte acceso por indice y no permite valores repetidos
conjunto = {"hola","mundo", True, 123}

#creando un diccionario (dic)

diccionario = {
    'nombre' : "tomas Heredia",
    'edad' : 23,
    'sexo' : True
}

print(diccionario["nombre"])