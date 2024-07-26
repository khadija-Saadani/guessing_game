import random
import time
def main ():
    print("\nWelcome to the Guessing Game! \n I'm thinking of a number between 1 and 100. How many guesses will it take you to uncover it ?")
    time.sleep(1)  
    attempts=0 
    random_number=random.randint(1,100)
    while True :
        try :
            x=int(input("Take a guess!  "))
            if 1<= x <= 100 :
                attempts+=1
                if x> random_number :
                    print("That's not quite right. Guess lower!   ")
                    
                elif x< random_number:
                    print("That's not quite right. Guess higher!  ")
                                   
                else :
                    print(f"You got it in {attempts} attempts ! The secret number was {random_number}.")
                    break
            else :
                print("Whoops! That number is out of range. Gotta be between 1 and 100, champ!")
        except ValueError :
            print ("Invalid input. Please enter a number.")
            
     
main()