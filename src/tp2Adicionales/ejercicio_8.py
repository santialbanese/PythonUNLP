p1 = input("ingrese palabra 1: ")
p2 = input("ingrese palabra 2: ")

ok = True
num = 0
for letter in p2[::-1]:
    if p1[num] != letter:
        ok = False
    num += 1        
if ok:
    print("Son anagramas.")
else:
    print("No son anagramas.")