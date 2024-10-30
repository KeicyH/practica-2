x=0
suma=0

cantidad= int(input("¿Cuántos exámenes hizo su estudiante en el curso?: "))
for i in range(cantidad):
       nota = float(input(f"Ingrese la nota del examen {i+1} :  "))
       suma+=nota

promedio=suma/cantidad
print(f"el promedio del estudiante es: {promedio:f}")

if promedio>=70:
    print("Aprobo el curso")
elif promedio>=60:
    print("Tiene que ir a ampliacion")
else:
    print("Reprobo el curso")