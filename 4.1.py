r1= (("Іванов", "Математика", 5), (("Петров", "Фізика", 3)))
print(r1)
r2= (("Іванов", "Математика", 5), (("Іванов", "Фізика", 4)))
print(r2)

print()

r3=set(r1)|set(r2)
print(r3)

print()

r4=set(r1)&set(r2)
print(r4)

print()

r5=set(r1)-set(r2)
print(r5)
