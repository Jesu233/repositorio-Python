#menu principal con 3 opciones
registro={}
usuario=""

def validadorUsiuario(usuario):
    if usuario in registro:
        print("El usuario ya existe. Intente otra vez")

def validadorSex(sexo):
    print(sexo)
    if sexo not in ["F","M"]:
        print("Debe ingresar M o F solamente. Intente denuevo")
        return False
    
    return True
    
def Validador_contraseña(contraseña): 
    #contraseña debe tener al menos 1 numero, almenos 1 letra
    contador_numeros= 0
    contador_letras= 0
    for letra in str(contraseña):
        if letra.isnumeric():
            contador_numeros+=1
        if letra.isupper():
            contador_letras+=1
    if contador_numeros!=4:
        print("la contraseña debe tener al menos 4 numeros")
        return False
    if contador_letras!=4:
        print("La contraseña debe tener al menos 4 letras")
        return False
    if len(contraseña)!=8:

        print("La contraseña debe tener 8 caracteres")
        return False
    else:
        return True

def main():
    opcion="0"
    while opcion!="4":
        print("*"*50 + "\n")
        print("MENU PRINCIPAL".center(50))
        print("\n" + "*"*50)
        print("1. Ingresar usuario ")
        print("2. Buscar Usuario")
        print("3. Eliminar Usuario")
        print("4. Salir")
        opcion= input("Elija una opcion que desea: ")
        
        match opcion:

            case "1":
                while True:
                    usuario= input("Ingrese nombre de usuario: ").upper()
                    
                    if validadorUsiuario(usuario)==True:
                        print("El usuario ya existe. Intente otra vez")

                    else:   
                        registro[usuario]=[]
                        break

                while True:
                    sexo=input("Ingrese sexo: ").upper()
                    if validadorSex(sexo)==True:
                        print("sexo ingresado correctamente: ")
                        registro[usuario].append(sexo)
                        break
            
                while True:
                    contraseña = input("Ingrese la contraseña: ").upper()

                    if Validador_contraseña(contraseña)==True:
                        print("contreña valida\nUsuario Ingresado con exito")
                        break
                    else: 
                        print("contraseña no valida")
                        break
        
            case "2":
                usuario = input("Ingrese le nombre de usuario que desea buscar")
                print("Nombre: ",registro[usuario])
                pass 
            case "3":
                usuario = input("ingrese el nombre del usuario que desea eliminar")
                del registro [usuario]
            case "4":
                print("Programa terminado....")
                
main()