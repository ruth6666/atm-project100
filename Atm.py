class Atm:
    def __init__(self,cardNo,pin):
        self.cardNo = cardNo
        self.pin = pin

    def check_balance(self):
        print("Your balance is 100000")

    def withdrawl(self,amount):
        new_amount = 100000 - amount
        print("You have withdrawn ₹"+str(amount) +"Your remaining balance is "+ str(new_amount))


def main():
    cardNumber = input("insert your card number:- ")
    pinNumber  = input("enter your pin number:- ")

    new_user =  Atm(cardNumber ,pinNumber)

    print("Choose your activity ")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter activity number :- "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()