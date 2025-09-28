# .count() recibe un elemento como argumento y cuenta la cantidad de veces que aparece en la lista

numbers = [0,1,1,2,2,2,3,3,3,3]

counted = []
for element in numbers:
    if element not in counted:
        counted.append(element)
        print("El elemento {} aparece {} veces" .format(element, numbers.count(element)))
        
#? resultado: 
# El elemento 0 aparece 1 veces
# El elemento 1 aparece 2 veces
# El elemento 2 aparece 3 veces
# El elemento 3 aparece 4 veces