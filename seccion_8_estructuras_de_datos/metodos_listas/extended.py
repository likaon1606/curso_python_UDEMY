# El método .extended() extiende la lista agregando al final el iterable indicado por parámetro

numbers = [1,2,3,4,5]
print(numbers)
numbers.extend([6])
print(numbers)
numbers.extend([7,8])
print(numbers)
numbers.extend(range( 9, 16 ))
print(numbers)

# [1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6, 7, 8]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]