
# Definición de la clase Animal
class Animal:
    def _init_(self, nombre):
        self.nombre = nombre
        print(f"Se ha creado un nuevo animal llamado {self.nombre}.")

    def _del_(self):
        print(f"El animal {self.nombre} ha sido eliminado.")


# Definición de la clase Perro, que hereda de Animal
class Perro(Animal):
    def _init_(self, nombre, raza):
        super()._init_(nombre)
        self.raza = raza

    def ladrar(self):
        print("¡Guau! ¡Guau!")


# Definición de la clase Gato, que hereda de Animal
class Gato(Animal):
    def _init_(self, nombre, color):
        super()._init_(nombre)
        self.color = color

    def maullar(self):
        print("¡Miau! ¡Miau!")


# Creación de instancias de las clases
perro = Perro("Fido", "Labrador")
gato = Gato("Pelusa", "Blanco")

# Llamada a los métodos de las instancias
perro.ladrar()
gato.maullar()

# Eliminación de las instancias al finalizar el programa# Online Python - IDE, Editor, Compiler, Interpreter

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')
