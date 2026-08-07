text = input("camelCase: ")
print("snake_case: ", end="")
for c in text:
    if c.isupper():
        print("_", end ="")
        print(c.lower(), end="")
    else:
        print(c, end="")
print()
