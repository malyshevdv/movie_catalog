

# Create your tests here.
class dd(dict):
    def get(self, __key,  default = None):
        res = super().get(__key, default=default)

        return res




ddd = dd()
print(chr(ord("A")))

def poli(my : int):
    res = 0
    myint = my
    nextStep = 10
    prevStep = 0
    print(myint)
    res = myint % nextStep
    print(res)
    while my > nextStep:
        prevStep = nextStep
        nextStep *=10

        ost = (myint  % nextStep) // prevStep
        res = res*10 + ost

        print(res)
    return res


def mylength(mystr, nextstep = 0):
    if mystr == "":
        return nextstep
    else:
        return mylength(mystr[1:], nextstep+1)


def mysort(myarray):

    wasExchange = True
    while wasExchange:
        wasExchange = False
        for i in range(len(myarray)-1):
            if myarray[i]>myarray[i+1]:
                myarray[i], myarray[i + 1] = myarray[i+1], myarray[i]
                wasExchange = True


class Car:
    def __init__(self, name, value, cost):
        self.name = name
        self.value = value
        self.rentpersent = 1
        self.cost = cost

        if value>1000:
            self.rentpersent = 5
        elif value > 5000:
            self.rentpersent = 10
    def __str__(self):
        #return "dddd"
        return f'ddd{self.name} = ${self.cost}'

    def getRentStaff(self):
        res = 0;
        res = self.value  * self.rentpersent / 100



myint = 1245871234
res = poli(myint)
print(res)

print('LEN')
print(mylength('Hello!1234'))

print('SORT')
myerray = ['2','1','3','7','1','9','8',]
print(myerray)
mysort(myerray)
print(myerray)

print('CARS')
mycars = []
mycars.append(Car('Toyota', 1500, 120))
mycars.append(Car('Crysler', 1500, 120))
mycars.append(Car('BMW', 1500, 98))
print(mycars)
print(mycars[1])
chipCar = [car for car in mycars if car.cost<100]
print(chipCar)


