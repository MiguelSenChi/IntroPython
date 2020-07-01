#Condicional simple
def evaluacion(nota):
    estado = "Promovido"
    
    if nota < 11:
        estado = "Sustitutorio"
        
    return estado

print(evaluacion(14))

print("Calificación del primer semestre")

calificacion = int(input("Ingrese la nota: "))

def evaluacion(nota):
    estado = "Promovido"
    
    if nota < 11:
        estado = "Sustitutorio"
        
    return estado

print(evaluacion(calificacion))

#Condicional doble
sueldo_gerente = int(input("Ingrese el salario del Gerente General: "))
print('Salario del Gerente General: S/.{}'.format(sueldo_gerente))

sueldo_jefe_area = int(input("Ingrese el salario del Jefe de Área: "))
print('Salario del Jefe de Área: S/.{}'.format(sueldo_jefe_area))


sueldo_asistente = int(input("Ingrese el salario del Asistente: "))
print('Salario del Asistente: S/.{}'.format(sueldo_asistente))

sueldo_tecnico = int(input("Ingrese el salario del Técnico: "))
print('Salario del Tecnico: S/.{}'.format(sueldo_tecnico))

sueldo_practicante = int(input("Ingrese el salario del Practicante: "))
print('Salario del Practicante: S/.{}'.format(sueldo_practicante))

if sueldo_gerente > sueldo_jefe_area > sueldo_asistente > sueldo_tecnico > sueldo_practicante:
    print("Se cumple con la estructura jerarquica")
    
else:
    print("Existencia de fallas en el sistema de pagos.")
    
#Condicional anidada
print("Programa de Becas al extrajero")

edad = int(input("Ingrese la edad del estudiante: "))
print(edad)

if edad >= 18:
    
    print("Usted es mayor de edad...")
    print()
    ponderado = float(input("Ingrese su promedio ponderado: "))
    
    if ponderado >= 15.5:
        print("Su promedio cumple con los requisitos del programa.")
        print()
        nro_cursos_aprob = int(input("Ingrese número de cursos aprobados: "))
        
        if nro_cursos_aprob >= 36:
            
            print("Usted si cumple el número de cursos aprobados")
            print()
            salario = int(input("Ingrese el salario familiar del estudiante: "))
            
            if salario < 15000:
                
                print("Cumple las condiciones del programa")
                
            else:
                
                print("El salario es mayor al minimo requerido.")
                
        else:
            
            print("El número de cursos aprobados debe ser mayor a 36")
        
    else:
        
        print("Su promedio debe ser mayor a 15.5")
            
else:

    print("Debe ser mayor de edad para postular.")













