import random    
# generate random number from 1 to 100                                                     
com_number=random.randrange(1,101)  
while True:                                  
   user_number = int (input("Enter your number:"))
   if com_number<user_number:
    print(" You guessed too high!! ") 
   elif com_number>user_number:
    print(" You guessed too low!! ")    
   else:
    print("  You guessed correct  ")
    print("computer number", com_number)
    break   

