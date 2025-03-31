def contieneNumero(name):
    if any(char.isdigit() for char in name):
        return True
    else:
        return False
    
def contieneMayuscula(name):
    if any(char.isupper() for char in name):
        return True
    else:
        return False
name = input("Ingrese nombre de usuario: ")

if name.__len__() >= 5 and contieneNumero(name) and contieneMayuscula(name) and name.isalnum():
    print("El nombre de usuario ES válido.")
else:
    print("El nombre de usuario NO cumple con los requisitos.")