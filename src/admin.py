import os
from src.database import loans

def login_admin():
    print("\nIngresa como administrador")
    password= input("\nIngresa la clave de administrador")
    if password== "admin123":
        print ("\nBievenido")
        panel_admin()
        
def panel_admin():
    while True:
        print("\n PANEL DE ADMINISTRACIÓN EDULEND\n 1. Ver todas las solicitudes\n2. Salir al menú principal")
        opcion= input("\n Selecciona una opción")
        if opcion== "1":
            see_all()
        else: 
            break
        
def see_all():
    print("\n Todas las solicitudes")
    if not loans:
        print("No hay solicitudes registradas")
    else:
        for i, p in enumerate(loans):
            print(f"{i+1}. Usuario: {p['user']}- Articulo:{p['article']}")
        input("\n Presiona enter para continaur")

