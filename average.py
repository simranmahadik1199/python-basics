s1=float(input('enter first subject'))
s2=float(input('enter second subject'))
s3=float(input('enter third subject'))
s4=float(input('enter fourth subject'))
s5=float(input('enter fifth subject'))
total=('addition of {} and {} and {} and {} and {}is {}'.format(s1,s2,s3,s4,s5,s1+s2+s3+s4+s5))
print(total)
average=(s1+s2+s3+s4+s5)/5
print(average)

if s1<35:
    print('fail')
elif s2<35:
    print('fail')
elif s3<35:
    print('fail')
elif s4<35:
    print('fail')
elif s5<35:
    print('fail')
else:
    print('pass')


