def Nota_final (num , alumno):
    if num < 60:
        print("Sacaste 1", alumno)
    elif num >  60 and num < 71:
        print("Sacaste 2", alumno)
    elif num > 70 and num < 76:
        print("sacaste 3", alumno)
    elif num > 75 and num < 86:
        print("sacaste 4", alumno)
    elif num > 85 and num < 96:
        print("Sacaste 5", alumno)
    else:
        print("Sacaste 5 Felicitado",alumno)
    
    Nota_final(int(input("ingresar el puntaje")), "name")