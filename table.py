
def mult():
    
    n=int(input('enter an number'))
    num=0
    while num<=10:
        table=num*n
        print(table)
        
        tbl=('table  of {} is {} , {}'.format(n,num,n*num))
        num=num+1
    return table
table=mult()
print(table)
mult()   


def tbl():
    number=int(input('enter a number'))
    for x in range(1,11,1):
        table=('table is {} multiplied by {} equal to {}'.format(number,x,number*x))
        print(table)
tbl()       



