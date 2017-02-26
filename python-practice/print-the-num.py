#\21天学通Python\
b=1

while(b):
    a = input('a num between 0~9: ')
    a = int(a)
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
    b = input('want to continue? y(1)/n(0)')
    b = int(b)
