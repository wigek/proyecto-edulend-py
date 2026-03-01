from src.database import users

def login():
    print("\n---Inicio de sesión----")
    email_joined= input("Ingresa tú correo electronico: ")
    password_joined= input("Ingresa tú contraseña: ")
    
    users_found = None
    for u in users:
        if u["email"]== email_joined and u["password"] == password_joined:
            users_found= u
            break
    
    if users_found:
        print(f"\nBienvenido de nuevo, {users_found['name']}")
    else:
        print ("\n ERROR: Credenciales incorrectas \n Intentalo de nuevo")
        input("Presiona enter para volver al menú")