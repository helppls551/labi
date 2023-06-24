class Person():
    def __init__(self,name,gender,age,weight,height):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.height = height
    
    def print_info(self):
        print('Имя:',self.name)
        print('Пол:',self.gender)
        print('Возраст:',self.age)
        print('Вес:',self.weight)
        print('Рост:',self.height)

a = Person('Андрей','мужской',16,64,180)
a.print_info()
