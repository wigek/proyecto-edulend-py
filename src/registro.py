from src.database import users

def registro ():
    print("------REGISTRO DE USUARIO------")
    name = input("Ingresa tú nombre")
    email= input("Ingresa tú email")
    password= input("Ingresa tu contraseña")
    
    new_user={
        "name": name,
        "email": email,
        "password": password
    }
    users.append(new_user)
    print("Registro exitoso")