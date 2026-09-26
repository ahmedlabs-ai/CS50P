name = []
while True:
    try:
        name.append(input("Name: "))
    except EOFError:
        break
print()
if len(name) == 1:
    print("Adieu, adieu, to",name[0])
elif len(name)== 2:
    print("Adieu, adieu, to",name[0] + " and " + name[1])
else:
    print("Adieu, adieu, to",", ".join(name[:-1]) + ", and " + name[-1])
