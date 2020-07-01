#Ciclo WHILE (La ejecución se detiene cuando la condición es falsa)
a = 1
while (a<=7):
    print(a)
    a = a + 1
    
a = 9
while (a>-1):
    print(a)
    a = a - 1
    
##Caso complejo
edad = int(input("Ingrese su edad: "))

while edad < 18 or edad > 70:
    
    print("No estás apto para sufragar!")
    
    edad = int(input("Ingrese la edad nuevamente: "))
    
print("Usted si puede sufragar")

#Ciclo FOR (Ciclo que se repite determinado número de veces)
print("INICIO")

for a in [1,2,3,4,5,6]: #Cuando son posiciones los cuenta como números
    
    print("Hola.")
    
print("FIN")

print("INICIO")

for a in ["Juan","José",12,14.5,True]:
    
    print(f"Hola soy {a}") #Palabra reservada f
    
print("FIN")

##Caso complejo
correo = str(input("Ingrese su correo: "))
cont = 0

for a in correo:
    
    if(a == "@" or a == "."):
        
        cont = cont + 1
        
if cont == 2:
    print("El email está correcto")
    
else:
    print("No cumple con el formato establecido")
    
for i in range(10):
    
    print("Hola gente!!")
    
for i in range(2,10,3): #(valor menor,valor mayor, aumento sucesivo)
    
    print(i)
    
for i in range(7,0,-1):
    print(i)
    
    
    





  