#Extraen valores de una función que recorren objetos de la lista(estado inmóvil hasta ser llamados)
##Función
def listPares(limite):
    
    num = 1
    miLista = []
    
    while (num < limite):
        
        miLista.append(num*2)
        num = num + 1
        
    return miLista

print(listPares(8))

##Generador (YIELD)
def listPares(limite):
    
    num = 1
    
    while (num < limite):
        
        yield(num*2)
        num = num + 1

returnPares = listPares(8)

for i in returnPares: #FOR muestra todos los elementos
    print(i)

###Mostrar elementos especificos del objeto iterable
print(next(returnPares))
print("Puede igresar aqui... ")

##Generador (YIELD FROM) Muestra los subelementos de la clase
def listarcursos(*cursos):
    
    for elemento in cursos:
        
        yield from elemento
        
cursos_listados = listarcursos("CTA","Matemáticas","Lenguaje","Historia")

print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))
print(next(cursos_listados))




