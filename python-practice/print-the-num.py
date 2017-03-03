#\21天学通Python\
one = ('   *','   *','   *','   *','   *')
two = ('****','   *','****','*   ','****')
thr = ('****','   *','****','   *','****')
fou = ('  **',' * *','****','   *','   *')
fiv = ('****','*   ','****','   *','****')
six = ('****','*   ','****','*  *','****')
sev = ('****','   *','   *','   *','   *')
eig = ('****','*  *','****','*  *','****')
nin = ('****','*  *','****','   *','****')
zer = ('****','*  *','*  *','*  *','****')
number = (zer,one,two,thr,fou,fiv,six,sev,eig,nin)
def printnum(num = [0,0]):
    #将数字拼合输出 两个数字中间存在一列空格
    for i in range(10) :
        if num[0] == i :
            c1 = number[i]
        if num[1] == i :
            c10 = number[i]
    numlist = [c10[0]+' '+c1[0],c10[1]+' '+c1[1],c10[2]+' '+c1[2],c10[3]+' '+c1[3],c10[4]+' '+c1[4]]
    return numlist
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
    A = [a1,a2,a3,a4,a5]
    return A
def gettime(time) :


b = 1
while(b):
    x = input('Please input an int num : ')
    x = int(x)
    numsingle = (splitnum(x))
    printnum(numsingle)
    b = input('want to continue? y(1)/n(0)')
    b = int(b)
