class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()

    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee)

    def result(self):
        self.customer.printFood()


class Customer:
    def __init__(self):
        self.foodName = None

    def placeOrder(self, foodName, employee):
        self.foodName = employee.takeOrder(foodName).name

    def printFood(self):
        print self.foodName


class Employee:
    def takeOrder(self, foodName):
        return Food(foodName)


class Food:
    def __init__(self, name):
        self.name = name


if __name__ == "__main__":
    l1 = Lunch()
    l1.order("eggs")
    l1.result()

    l1.order("chiken")
    l1.result()
