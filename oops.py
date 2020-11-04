class speed:
    def bike(self):
        print('below given are speeds')
class unicorn(speed):
    def f1(self):
        print('speed is 140kmph')
class r15(speed):
    def f2(self):
        print('speed is 120kmph')
class subchild(unicorn,r15):
    def f3(self):
        print('subchild')

sb=subchild()
#sb.bike()
sb.f1()
sb.f2()
sb.f3()
      
