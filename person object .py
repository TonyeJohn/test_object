class Person:
    def __init__(self, name, gender, age):
        self.name=name
        self.gender=gender
        self.age=age
    def talk(self):
        print('Name: ',self.name)
    def genders(self):
        print('Gender: ',self.gender)
    def ages(self):
        print('Age: ',self.age)
    def vote(self):
        if self.age>18:
            print('You are eligible to vote')
        else:
            print('You are not eligible to vote')
            
person1=Person('Tonye', 'Male', 26)
person1.talk()
person1.genders()
person1.ages()
person1.vote()

person2=Person('Nancy','Female', 17)
person2.talk()
person2.genders()
person2.ages()
person2.vote()

person3=Person('Moses', 'Male', 20)
person3.talk()
person3.genders()
person3.ages()
person3.vote()

person4=Person('Betty', 'Female', 29)
person4.talk()
person4.genders()
person4.ages()
person4.vote()