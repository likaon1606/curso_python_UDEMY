# 99 Bottles of Rum on the Wall
# De tantas solicitudes que ha recibido, Pyratilla no cabe en sí de la emoción y se pone a cantar

# "99 bottles of rum on the wall, 99 bottles of rum.
# Take one down, pass it around, 98 bottles of rum on the wall.
# 98 bottles of rum on the wall, 98 bottles of rum.
# Take one down, pass it around, 97 bottles of rum on the wall..."
# Ayuda a Pyratilla a cantar la canción al completo con un bucle while.

#? *** WHILE ***

bottles = 99

while bottles > 0:
    if bottles > 1:
        print(f"{bottles} bottles of rum on the wall, {bottles} bottles of rum.")
        print(f"Take one down, pass it around, {bottles - 1} bottles of rum on the wall.")
    else:
        print(f"{bottles} bottle of rum on the wall, {bottles} bottle of rum.")
        print("Take one down, pass it around, no more bottles of rum on the wall.")
    bottles -= 1

print("No more bottles of rum on the wall, no more bottles of rum.")
print("Go to the store and buy some more, 99 bottles of rum on the wall.")

#? *** FOR ***

for bottles in range(99, 0, -1):
    if bottles > 1:
        print(f"{bottles} bottles of rum on the wall, {bottles} bottles of rum.")
        print(f"Take one down, pass it around, {bottles - 1} bottles of rum on the wall.")
    else:
        print(f"{bottles} bottle of rum on the wall, {bottles} bottle of rum.")
        print("Take one down, pass it around, no more bottles of rum on the wall.")

print("No more bottles of rum on the wall, no more bottles of rum.")
print("Go to the store and buy some more, 99 bottles of rum on the wall.")