def contieneNumero(name):
    if any(char.isdigit() for char in name):
        return True
    else:
        return False
    
def contieneMayuscula(name):
    return True if any(char.isupper() for char in name) else False
name = input("Ingrese nombre de usuario: ")

def mayorA5(name):
    return True if name.__len__() >= 5 else False 

def numOrletters(name):
    return True if name.isalnum() else False 

if mayorA5(name) and contieneNumero(name) and contieneMayuscula(name) and numOrletters(name):
    print("El nombre de usuario ES válido.")
else:
    print("El nombre de usuario NO cumple con los requisitos.")