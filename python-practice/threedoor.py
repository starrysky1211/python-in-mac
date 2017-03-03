import random

total = int(input('input total times for this test: '))
bingo = 0
for i in range(total):
    my_choice = random.randint(0,2)
    car = random.randint(0,2)
    if my_choice == car :
        bingo += 1
print (bingo,' times bingo')
pro = 100*(bingo/total)
print ('probablity for directly choosing is ',pro,'%. ')

bingo1 = 0

for i in range(total):
    my_choice = random.randint(0,2)
    car = random.randint(0,2)
    if my_choice == car :
        bingo1 = bingo1
    else :
        bingo1 += 1
print (bingo1,'times bingo')
pro1 = 100*(bingo1/total)
print ('probablity fot changedly choosing is ',pro1,'%. ')

