import random


class Animal:
    def __init__(self, name):
        self.name = name
        self.sitost = 50
        self.alive = True
        self.day = 0

    def to_eat(self):
        self.sitost += 5

    def to_play(self):
        self.sitost -= 5

    def is_alive(self):
        if self.sitost <= 2.5:
            self.alive = False

    def endOfDay(self):
        print("Sitost:", self.sitost)

    def showResult(self):
        print("Day", str(self.day), " of ", self.name, "life")
        self.endOfDay()

    def live(self):
        self.day += 1
        num = random.randint(1, 2)
        if num == 1:
            self.to_eat()
        elif num == 2:
            self.to_play()

        self.is_alive()


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    #     1 реализовать метод добавления студента в группу
    def addAnimal(self, newAnimal):
        self.animals.append(newAnimal)

    #     2 реализовать метод показа в консоль списка студентов этой группы
    def printAnimals(self):
        if self.animals != []:
            print("Name of the Zoo: ", self.name)
            for st in self.animals:
                print(st.name)
        else:
            print("No students in this grupp!")

    def delAnimal(self, delAnimal):
        try:
            self.animals.remove(delAnimal)
        except:
            print("There are no", delAnimal.name, "in this zoo ", self.name)

    def kormlenie(self):
        print("Kormlenie")
        self.to_eat

 #     3 реализовать метод симуляции жизни группы
    def simulateZoo(self):
        for st in self.animals:
            for day in range(365):
                if st.alive == False:
                    self.delAnimal(st)
                    break
                st.live()

            st.showResult()


lion = Animal("White lion")
slon = Animal("Obichniy slon")

zoo = Zoo("Giena")

zoo.addAnimal(lion)
zoo.addAnimal(slon)
# zoo.delAnimal(lion)

zoo.printAnimals()

zoo.simulateZoo()


