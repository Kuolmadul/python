print('Grades calculator')
math = int(input('math: '))
eng = int(input('eng: '))
phyc = int(input('phyc: '))
kis = int(input('kis: '))
hist = int(input('hist: '))

total = math + eng + phyc + kis + hist
average = total/5

if average >= 91 and average<=100:
    print('Your grade is A1')
elif average>=81 and average<91:
    print('Your grade is A2')
elif average >=71 and average<81:
    print('Your grade is B1')
elif average >=61 and average<71:
    print('Your grade is B2')
elif average >=51 and average<61:
    print('Your grade is C1')
elif average >=41 and average<51:
    print('Your grade is C2')
elif average >=33 and average<41:
    print('Your grade is D')
elif average >=21 and average<33:
    print('Your grade is E')
elif average >=0 and average<21:
    print('Your grade is E2')
else:
    print('Invalid input!')

















