#practica de poo

class contacto :
    def __init__(self, nombre, telefono, correo, apodo1 = None, apodo2 = None, apodo3 = None):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.apodo1 = apodo1
        self.apodo2 = apodo2
        self.apodo3 = apodo3


class agenda:
    def __init__(self):
        self.contactos = []


    def agregar_contacto(self, nombre, telefono, correo, apodo1 = None, apodo2 = None, apodo3 = None):
            nuevo_contacto = contacto(nombre, telefono, correo, apodo1, apodo2, apodo3)
            self.contactos.append(nuevo_contacto)
    

    def mostrar_contacto(self):
        if len(self.contactos) == 0:
             print("tu lista de contactos esta vacia")
        else:
             print("lista de contactos")
             for contacto in self.contactos:
                  print("nombre", contacto.nombre)
                  print("telefono", contacto.telefono)
                  print("correo", contacto.correo)
                  print(" ")

    def buscar_contacto(self, dato_de_entrada):
        encontrado = False
        for contacto in self.contactos:

            if contacto.nombre.lower() == dato_de_entrada.lower() or \
                str(contacto.telefono) == dato_de_entrada or \
                contacto.correo.lower() == dato_de_entrada.lower() or \
                (contacto.apodo1 is not None and contacto.apodo1.lower() == dato_de_entrada.lower()) or \
                (contacto.apodo2 is not None and contacto.apodo2.lower() == dato_de_entrada.lower()) or \
                (contacto.apodo3 is not None and contacto.apodo3.lower() == dato_de_entrada.lower()):
                    print("informacion de ", contacto.nombre, ":")
                    print("numero : ", contacto.telefono)
                    print("correo : ", contacto.correo)
                    encontrado = True
        if not encontrado:
            print("no se encontro el usuario en tu agenda")




#ahora sigue lo bueno qlo


agenda_obj = agenda()
agenda_obj.agregar_contacto("Juan", 123456789, "juan@example.com", "Juancito")
agenda_obj.agregar_contacto("María", 987654321, "maria@example.com", "Mary")
agenda_obj.agregar_contacto("Pedro", 456789123, "pedro@example.com")
agenda_obj.agregar_contacto("Ana", 555555555, "ana@example.com", "Anita")
agenda_obj.agregar_contacto("Carlos", 111111111, "carlos@example.com")
agenda_obj.agregar_contacto("Luisa", 999999999, "luisa@example.com", "Lu")
agenda_obj.agregar_contacto("Miguel", 444444444, "miguel@example.com")
agenda_obj.agregar_contacto("Laura", 222222222, "laura@example.com", "Lau")
agenda_obj.agregar_contacto("Diego", 777777777, "diego@example.com")
agenda_obj.agregar_contacto("Sofía", 888888888, "sofia@example.com", "Sofi")





#aqui puedes poner cualquier dato ya sea numero, correo, apodo, o nombre y buscara dentro de la lista
#el siguiente paso son bases de datos

#a puedes poner mayusculas y minusculas e igual lo va a encontrar "MIguEL"

agenda_obj.buscar_contacto("MIguEL")