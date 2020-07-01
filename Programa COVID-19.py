print("Verificación COVID-19")
print("*************************************")
print("Ingrese la temperatura del paciente: ")
temp = float(input())

if temp > 36:
    
    print()
    print("El paciente necesita de la prueba molecular.")
    print()
    print("*******************************************")
    print()
    print("Resultado de la prueba. (+/-)")
    prueba = str(input())
    
    if prueba == "+":
        
        print()
        print("El paciente necesita aislamiento.")
        
    else:
        
        print()
        print("Descartado al 100% el contagio.")
    
else:
    
    print()
    print("Se descarta la posibilidad de COVID-19, aplicar prueba de descarte.")
