# object oriented programming
# self is a parameter
# class is a blue print
# object is input
class People:
    def __init__(self, name, age, email, contact):
        self.name = name
        self.age = age
        self.email = email
        self.contact = contact

person1 = People('Jonny', 20, '123@gmail.com', '087654432')
person2 = People('Teddy', 30, 'kk@gmail.com', '0776543432')


print(f'Hi, my name is {person2.name}' )













#
# print(person1.name, person1.contact, person1.email, person1.age)
#
# print(person2.name, person2.contact, person2.email, person2.age)
#








