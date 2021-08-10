print("Hello World!!")

# Assume the user has input these
x = 3
y = 11

x,y = y,x
print('x, y= ',x,y)

from mytime import Time

t = Time()
#t.set_time(10,20,35)
#t.display()

from my_lamp import Lamp
la = Lamp()
la.plug_in()
print(la.is_on)

la.toggle()
print(la.is_on)

la.toggle()
print(la.is_on)

