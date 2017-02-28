#\21天学通Python\
def printnum(num):
    a = num
    if a < 0 | a > 10 :
        print ('invilid input!')
    elif a == 1 :
        print('   *','   *','   *','   *','   *',sep = '\n')
    elif a == 2 :
        print('****','   *','****','*   ','****',sep = '\n')
    elif a == 3 :
        print('****','   *','****','   *','****',sep = '\n')
    elif a == 4 :
        print('  **',' * *','****','   *','   *',sep = '\n')
    elif a == 5 :
        print('****','*   ','****','   *','****',sep = '\n')
    elif a == 6 :
        print('****','*   ','****','*  *','****',sep = '\n')
    elif a == 7 :
        print('****','   *','   *','   *','   *',sep = '\n')
    elif a == 8 :
        print('****','*  *','****','*  *','****',sep = '\n')
    elif a == 9 :
        print('****','*  *','****','   *','****',sep = '\n')
    elif a == 0 :
        print('****','*  *','*  *','*  *','****',sep = '\n')
def splitnum(num):
    a = num
    if a >10000 :
        print ('invilid num')
    else:
        a1 = a%10
        a2 = (a-a%10)%100/10
        a3 = (a-a%100)%1000/100
        a4 = (a-a%1000)%10000/1000
        a5 = (a-a%10000)%100000/10000
    return a1,int(a2),int(a3),int(a4),int(a5)

b = 1
while(b):
    x = input('Please input an int num : ')
    x = int(x)
    print (splitnum(x))
    b = input('want to continue? y(1)/n(0)')
    b = int(b)
