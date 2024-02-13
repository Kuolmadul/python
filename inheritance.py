class Animal:
    def animals(self):
        print('Can breath')
    def monkey(self):
        print('can walk')
    def baboon(self):
         print('can run')


class Humans(Animal):
    def mtu(self):
        print('Mtu lives on land')

being = Humans()

print(being.mtu())