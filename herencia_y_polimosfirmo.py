class Father:

    def __init__(self, name: str, lastname: str, age: int):

        self.name = name
        self.lastname = lastname
        self.age = age
    def nick_name(self):

        print(f"Su usuario es: {self.name[0:4]}{self.lastname[0:3]}{self.age}")


class Chield(Father):

    def __init__(self, name: str, lastname: str, age: int, height: float):
        super().__init__(name, lastname, age)

        self.height = height




chield_1 = Chield("Francisco", "Vanegas", 28, 1.74)
chield_2 = Chield("Cristian", "Vanegas", 25, 1.64)
father =  Chield("Efren","Mosquera",60,1.80)

print(f"Bienvenid(@): {chield_1.name} {chield_1.lastname} {chield_1.age} {chield_1.height}")
chield_1.nick_name()
print("")

print(f"Bienvenid(@): {chield_2.name} {chield_2.lastname} {chield_2.age} {chield_2.height}")
chield_2.nick_name()
print("")

print(f"Bienvenid(@): {father.name} {father.lastname} {father.age} {father.height}")
father.nick_name()

