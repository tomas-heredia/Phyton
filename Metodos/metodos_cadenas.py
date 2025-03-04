#metodos dato + . + nombre del metodo()
cadena1 = "Hola soy Dalto"
cadena2 = "Bienvenido maquinola"

#print(dir(cadena1)) #devuelve todas las operaciones disponibles 

#resutlado = dir(cadena2)
resutlado = cadena1.upper() #convierte a mayusculas

resutlado = cadena1.lower() #convierte a minusculas

resutlado = cadena1.capitalize() #priemra letra a mayuscula

resutlado = cadena1.find("o") #busca una cadena en otra cadena y debuelve la posicion de la coincidencia, si ni encuetra retorna -1

resutlado = cadena1.index("H") # lo mismo que find pero si no encuentra nada regresa una exepcion (error)

resutlado = cadena1.isnumeric() #si es numerito da true, aunque sea texto de solo nuemros

resutlado = cadena1.isalpha() #da true si es alpha numerico, solo validos caracteres a-z

resutlado = cadena1.count("a") #numero de coincidencias de una cadena en otra

resultado = len(cadena1) #cantidad de caractere 

resutlado = cadena1.endswith("to") #ture si termina con los caracteres

resutlado = cadena1.startswith("ho") #true si inicia con los caracteres

resutlado = cadena1.replace("Hola","Chau") #reemplaza una cadena vieja por una nueva
resutlado = cadena1.replace("a","u")

resutlado = cadena1.split(" ") #regresa una lista de los elementos de la cadena separados por el caracter



print(type(resutlado))