from src.database import users

def login():
    print("\n---Inicio de sesión----")
    email_joined= input("Ingresa tú correo electronico: ")
    password_joined= input("Ingresa tú contraseña: ")
    
    users_found = None
    for i in users:
        if i["email"]== email_joined and i["password"] == password_joined:
            users_found= i
            break
    
    if users_found:
        print(f"\nBienvenido de nuevo, {users_found['name']}")
        return users_found
    else:
        print ("\n ERROR: Credenciales incorrectas \n Intentalo de nuevo")
        input("Presiona enter para volver al menú")
        return None