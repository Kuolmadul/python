math = int(input('math: '))
english = int(input('eng: '))
#
# if math > english:
#     print("math is greater than english")
# elif math < english:
#     print('math is less than english')
# else:
#     print('math is equals english')
#

if math > 0 and english > 0:
    print('Both are positive numbers')
elif math < 0 and english < 0:
    print('Both are negative numbers')
elif math < 0 and english > 0:
    print("One of the numbers is negative")
elif math > 0 and english < 0:
    print("One of the numbers is positive")
else:
    print(' Both are zero')









