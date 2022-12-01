import pyinstaller

print("Welcome to Veggie Store!")

class grocery:
    def __init__(self,cardNo,name):
        self.cardNo=cardNo
        self.name=name
    
    def integers(self):
         print("Please choose what you would like to purchase:")
         print("1)Vegetables 2)Fruits 3)Other")
         activity=int(input("Enter activity number: "))
         if(activity==1):
            print("Clean Eats currently has in stock:")
            print("1)Tomatoes 2)Potatoes 3)Spinach 4)Eggplants 5)Bell peppers")
            answerV=(input("Please put your choices down here(with the amount): "))
            print("You have purchased "+answerV)
            print("That will be $110.")
            amount=int(input("Pay: "))
            if amount<110:
                print("Insufficient funds!")
                amount=int(input("Please pay again: "))
                if amount<110:
                    print("Insufficient funds!")
                    amount=int(input("Please pay again: "))
                    
                elif amount>110:
                    new_amount=amount-110
                    print( "Thank you. Your change is $"+str(new_amount))
                else:
                    print("Thank you! You may expect your delivery within 3-4 days.")

            elif amount>110:
                new_amount=amount-110
                print( "Thank you. Your change is $"+str(new_amount))
            else:
                print("Thank you! You may expect your delivery within 3-4 days.")




         elif(activity==2): 
            print("Clean Eats currently has in stock:")
            print("1)Oranges 2)Apples 3)Bananas 4)Pears 5)Grapes")
            answerV=(input("Please put your choices down here(with the amount): "))
            print("You have purchased ."+answerV)
            print("That will be $90.")
            amount=int(input("Pay: "))
            if amount<90:
                print("Insufficient funds!")
                amount=int(input("Please pay again: "))
                if amount<90:
                    print("Insufficient funds!")
                    amount=int(input("Please pay again: "))
                    
                elif amount>90:
                    new_amount=amount-90
                    print( "Thank you. Your change is $"+str(new_amount))
                else:
                    print("Thank you! You may expect your delivery within 3-4 days.")

            elif amount>90:
                new_amount=amount-90
                print( "Thank you. Your change is $"+str(new_amount))
            else:
                print("Thank you! You may expect your delivery within 3-4 days.")




         elif(activity==3):
            answerV=(input("Please put your choices down here: "))
            print("You have purchased "+answerV)
            print("That will be $246.")
            amount=int(input("Pay: "))
            if amount<246:
                print("Insufficient funds!")
                amount=int(input("Please pay again: "))
                if amount<246:
                    print("Insufficient funds!")
                    amount=int(input("Please pay again: "))
                    
                elif amount>246:
                    new_amount=amount-246
                    print( "Thank you. Your change is $"+str(new_amount))
                else:
                    print("Thank you! You may expect your delivery within 3-4 days.")

            elif amount>246:
                new_amount=amount-246
                print( "Thank you. Your change is $"+str(new_amount))
            else:
                print("Thank you! You may expect your delivery within 3-4 days.")
    
def main():
    name=input("Enter name: ")
    card_number=input("Insert card number: ")
    print("Welcome "+name+"!")
    new_user=grocery(card_number, name)

    if card_number.strip().isdigit():
        new_user.integers()
        
    else:
        print("Please only enter numbers! If you enter a letter again, the app will lock you for 5 minutes.")
        card_number=input("Insert card number: ")
        if card_number.strip().isdigit():
            new_user.integers()

    
if __name__=="__main__":
    main()