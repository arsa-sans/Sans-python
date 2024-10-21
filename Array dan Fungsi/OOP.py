# Object-oriented Programming
# created by Arsa
# 8-10-2024

print('\n')
print('='*30)
print('Object-oriented Programming')
print('='*30)

class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    def __str__(self):
        return f"Nama: {self.name}, Umur: {self.age}, Spesies: {self.species}"

class Cat(Animal):
    def __init__(self, name, age, species="Kucing"):
        super().__init__(name, age, species)
    def deskripsi(self):
        return f"{self.name} adalah kucing berjenis {self.species} yang sudah berumur {self.age} tahun"
    def suara(self):
        return "meow!"
      
myCat = Cat("Neko", 3, "Persian")

print(myCat.deskripsi())  
print(myCat.suara())
print()