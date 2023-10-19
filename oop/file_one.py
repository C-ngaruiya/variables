from our_classes_file import Fruit,Car,User,Admin
from abstraction import Car
fruitOne =Fruit("Mango","Yellow","300g","ksh.100")
fruitTwo = Fruit("Apple","Green","0.30g","ksh.40")
print(fruitOne.price)
print(fruitTwo.color)

car0ne = Car("Mercedes","Grey","KDN300J","ksh.4,500,000")
carTwo = Car("Bugatti","Orange","KCE456U","KSH.25,000,000")
print(carTwo.model)

userOne = User("Cate","acfde@gmail.com","234rthg")
userTwo = User("Betty","aerd@test.com","345678")

userOne.register()
userTwo.login()

adminOne = Admin("Fraciah","fraciah3456","2345")

adminOne.login()

toyotaOne = Toyota()
toyotaOne.mileage()

nissanOne = Nissan()
nissanOne.mileage()