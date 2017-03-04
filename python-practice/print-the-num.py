#\21天学通Python\
import time

one = ('   |','   |','   |','   |','   |')
two = ('||||','   |','||||','|   ','||||')
thr = ('||||','   |','||||','   |','||||')
fou = ('  ||',' | |','||||','   |','   |')
fiv = ('||||','|   ','||||','   |','||||')
six = ('||||','|   ','||||','|  |','||||')
sev = ('||||','   |','   |','   |','   |')
eig = ('||||','|  |','||||','|  |','||||')
nin = ('||||','|  |','||||','   |','||||')
zer = ('||||','|  |','|  |','|  |','||||')
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
    if a >100 :
        print ('invilid num')
    else:
        a1 = a%10
        a2 = (a-a%10)%100/10
    A = [a1,a2]
    return A
def gettime() :
    t = time.localtime(time.time())
    nt = [t.tm_hour,t.tm_min,t.tm_sec]
    return nt
while(1):
    nt = gettime()
    ntpr = [printnum(splitnum(nt[0])),printnum(splitnum(nt[1])),printnum(splitnum(nt[2]))]
    timelist = [ntpr[0][0]+'    '+ntpr[1][0]+'    '+ntpr[2][0],ntpr[0][1]+' -- '+ntpr[1][1]+' -- '+ntpr[2][1],ntpr[0][2]+'    '+ntpr[1][2]+'    '+ntpr[2][2],ntpr[0][3]+' -- '+ntpr[1][3]+' -- '+ntpr[2][3],ntpr[0][4]+'    '+ntpr[1][4]+'    '+ntpr[2][4]]

    print ('\n',timelist[0],timelist[1],timelist[2],timelist[3],timelist[4],sep = '\n')
    time.sleep(1)
