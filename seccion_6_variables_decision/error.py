def make_list(number):
    names = []
    for i in range(number):  # iterar usando range, no directamente el int
        names.append(input("Enter your name with a capital letter: "))
    return names  # devolver la lista

number = int(input("How many names need to be entered? "))
names = make_list(number)

for name in names:
    if name[0] == "A":  # comprobar la primera letra
        print("Name", name, "starts with A")
