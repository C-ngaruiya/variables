#Inbuilt functions
greeting="Hello there"
print(greeting)
print(greeting.upper())
print(greeting.lower())

#Custom/User defined functions
def motto():
    print("Hello there, this is our motto")
motto()
motto()


def add():
    x=10
    y=20
    z=x+y
    print("your answer is",z)
add()

def addition(x, y, z):
    answer = x + y + z
    print("your answer is",answer)

addition(200,320,650)
addition(654,987,324)

def avg(name,first_number,second_number,third_number):
    answer=(first_number+second_number+third_number) /3
    print("Hello",name, "your average is",answer)

avg("Cate",300,400,600)
avg("Jane",20,67,34)

def simple_interest(p,r,t):
    interest=(p*r*t)/100
    return interest
print(simple_interest(2000,8,4))
