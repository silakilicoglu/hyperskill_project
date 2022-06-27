# Coffee Machine

class CoffeeMachine:
    def __init__(self, machine_water = 400, machine_milk = 540, machine_beans = 120, cups_of_coffee = 9, money = 550):
        self.machine_water = machine_water
        self.machine_milk = machine_milk
        self.machine_beans = machine_beans
        self.cups_of_coffee = cups_of_coffee
        self.money = money
    
    def __repr__(self):
        return f"The coffee machine has:\n{self.machine_water} ml of water\n{self.machine_milk} ml of milk\n{self.machine_beans} g of coffee beans\n{self.cups_of_coffee} disposable cups\n$ {self.money} of money"
    
# Teach your virtual coffee machine to perform three basic actions: collect the money, renew the supplies, and serve the coffee.

    # serve the coffee
    def buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:, back - to main menu")    
        coffee_type = input()
        if coffee_type != 'back':    
            if coffee_type == '1':
                water = 250
                milk = 0
                beans = 16
                cost = 4
            elif coffee_type == '2':
                water = 350
                milk = 75
                beans = 20
                cost = 7
            elif coffee_type == '3':
                water = 200
                milk = 100
                beans = 12
                cost = 6
            remain_water = self.machine_water // water
            remain_beans =  self.machine_beans // beans
            if coffee_type != '1':    
                remain_milk =  self.machine_milk // milk
                list1 = [remain_water, remain_beans, remain_milk]
                list2 = ["water", "beans", "milk"]
                N = min([remain_water, remain_milk, remain_beans]) # the number of coffees that can be made.
                index = list1.index(N)
            else: #coffee_type = 1
                N = min([remain_water, remain_beans]) # the number of coffees that can be made.
                list1 = [remain_water, remain_beans]
                list2 = ["water", "beans"]
                index = list1.index(N)
            if N > 0:
                print("Yes, I have enough resources, making you a coffee!")
                self.machine_water -= water
                self.machine_milk -= milk
                self.machine_beans -= beans
                self.cups_of_coffee -= 1  
                self.money += cost
            else:
                if self.cups_of_coffee == 0:
                    print("Sorry not enough cups")
                else:
                    print("Sorry not enough", list2[index])                
        else:
            return menu()

    # renew the supplies
    def fill(self):    
        print("Write how many ml of water you want to add:")
        water_add = int(input())
        print("Write how many ml of milk you want to add:")
        milk_add = int(input()) 
        print("Write how many grams of coffee beans you want to add:") 
        beans_add = int(input())
        print("Write how many disposable cups of coffee you want to add:")
        cups_add = int(input())
        self.machine_water += water_add 
        self.machine_milk += milk_add
        self.machine_beans += beans_add
        self.cups_of_coffee += cups_add

    # collect the money
    def take(self):
        print("I gave you $" + str(self.money))
        self.money = 0

# Set the main loop: now the menu keeps updating until you enter “exit”.
def menu():
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "buy":
            coffee_machine.buy()
        elif action == "fill":
            coffee_machine.fill()
        elif action == "take":
            coffee_machine.take()
        elif action == "remaining":
            print(coffee_machine)
        elif action == "exit":
            print("exit")
            exit()
        else:
            continue

coffee_machine = CoffeeMachine()
menu()
