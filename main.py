import time
import random 
from blockchain import Blockchain


class User:
    points = 1000                                           
    local_blockchain = Blockchain()
    money = 50
    
    def user_points(self):
        print('\n')
        return user.points 

    def get_money(self):
        return self.money

    def get_seeds(self):
        count = 0 
        for i in self.local_blockchain.chain:
            if len(i.transactions) == 0:
                pass
            else:
                count += 1
        
        if count == 0:
            print("You don't have any $eeds yet")
             
        else:
            print('You have {} $eed(s) in total'.format(count))
            
        
    


user = User()

class Prompt:
    transactions = 0
    counter = 0

    def interface(self):

        print("You have three options: ")
        time.sleep(0.2)
        print('1: View the amount of points you have \n')
        print('2: Buy a $eed \n')
        print('3: Make a transaction with either a $eed or with points \n')
        print('4: View the amount of money you have from our crypto \n')
        print('Please type either: ')
        for i in range(1,5):
          print(i)
        print('to acess a command')
        time.sleep(0.5)
        running = True 
        while running:
            
            self.value()
            user.money += self.crypto_value

            if self.counter % 6 == 0 or self.counter == 0:                                              # Rate of when the ratio changes
                self.point_to_crypto = random.randint(100, 750)

            print('\n')
            print("The ratio of points:$eed = {}:1".format(self.point_to_crypto))
            print('The current value $eed is ${} dollars'.format(self.crypto_value))
            print("\n")
            user_input = input("Please enter a command: ")

            if user_input == '1':
                print("-"*24)
                print("You currently have {} points \n".format(user.user_points()))
                self.counter += 1 
                print("-"*24)
            
            elif user_input == '2':
                print("-"*24)
                self.purchase()
                self.counter += 1
                print("-"*24)

            elif user_input == '3':
                num_users = random.randint(1, 1000)
                
                users = {}
                
                for i in range(num_users):
                    num_points = random.randint(1, 2500)
                    string = "user" + str(i)
                    users[string] = num_points

                print("-"*24)
                print("There are currently {} users online right now! ".format(num_users))
                time.sleep(0.5)
                
                print("How would you like to make your transaction: \n")
                time.sleep(0.5)
                print('Type \'$eed\' if you would like to sell your $eed')
                time.sleep(0.5)
                print('Type \'points\' if you would like to send someone points ')
                print('\n')
                
                prompt2 = input(':')
                print("\n")

                if prompt2 == "points":
                    if user.points >= 100:                                                        # You need to atleast have 100 points to transfer points
                        for k, l in users.items():
                            print("{num}: {points} points".format(num=k, points=l))
                        
                        print("\n")
                        print("Here are the users that are currently online")
                        
                        game = True 
                        while game:
                            print("\n")
                            user_chooser = input('Please enter a user that you want to trade with by typing "user(number)": ')

                            if user_chooser in list(users.keys()):
                                try:
                                    print("NOTE: You must transfer at least 100 points minimum")
                                    transfer_points = input("How many points would you like to transfer: ")

                                    if int(transfer_points) < 100:                                 #Must transfer more than 100 points                      
                                        print("That amount is too less to transfer ")
                                    else:
                                    
                                        if int(transfer_points) > user.points:                  
                                            print("You do not have that many points...")
                                        else:
                                            current_user_value = users[user_chooser]
                                            new_user_value = current_user_value + int(transfer_points)
                                            user.points = user.points - int(transfer_points)
                                            print("\n")
                                            print("Completing transaction ")
                                            for i in range(3):
                                                print("...")
                                                time.sleep(0.2)
                                            
                                            print("Transaction complete! ")
                                            print("\n")
                                            time.sleep(0.1)
                                            returns =  random.randint(1, 90)
                                            user.points += returns
                                            users[user_chooser] += returns
                                            print("You now have {} points \n".format(user.points))
                                            print("{} now has {point} points".format(user_chooser, point=new_user_value))
                                            self.transactions += 1
                                            
                                            print("-"*24)
                                            self.counter += 1


                                            time.sleep(0.5)
                                            chance = random.randint(1, 4)

                                            if chance == 1:
                                                random_user = random.randint(1, num_users)
                                                random_user_value = users['user' + str(random_user)]
                                                random_points = random.randint(100, random_user_value - 100)
                                                print("\n")
                                                print("{user} has sent you {points} points! ".format(user=random_user, points=random_points))

                                                user.points += random_points
                                                users[random_user] -= random_points
                                                self.counter += 1
                                                self.transactions += 1
                                            else:
                                                pass

                                            print("-"*24)
                                            break
                                except ValueError:
                                    print("That value does not seem to be a valid input")
                                    
                            
                            elif user_chooser == "/quit":
                                print("-"*24)
                                self.counter += 1
                                break 
                        
                            else:
                                print("That user does not seem to be online")
                    else:
                        print("You do not have enough points to create a transaction")
                        print("You must have above 100 points")
                        print("-"*24)

                elif prompt2 == "$eed":
                    if len(user.local_blockchain.chain) > 1:

                        print("The ratio of points:$eed = {}:1".format(self.point_to_crypto))
                        print('The current value of our crypto is ${} dollars'.format(self.crypto_value))

                        prompting = True
                        while prompting:
                            prompt3 = input('Would you like to sell your $eed(s) for points or money?: ')

                            if prompt3 == "points" or prompt3 == "Points":
                                num_blockchain = input("How many $eed(s) would you like to sell: ")

                                if int(num_blockchain) > len(user.local_blockchain.chain):
                                    print('You do not seem to have that many $eed(s) yet...')
                                else:
                                    seed_to_points = self.point_to_crypto * int(num_blockchain)
                                    user.points += seed_to_points
                                    
                                    for m in range(1, int(num_blockchain) + 1):
                                        user.local_blockchain.chain.pop(m)

                                    print("Processing your transaction")
                                    for i in range(3):
                                        print("...")
                                        time.sleep(0.2)
                                    print("Transaction complete!")
                                    print("\n")
                                    time.sleep(0.1)
                                    user.points += random.randint(1, 90)
                                    print('You now have {} points!'.format(user.points))
                                    print('You now have {} $eed(s)'.format(len(user.local_blockchain.chain) - 1))
                                    self.transactions += 1
                                    
                                    break

                            elif prompt3 == "money" or prompt3 == "Money":
                                num_blockchain = input("How many $eed(s) would you like to sell: ")

                                if int(num_blockchain) > len(user.local_blockchain.chain):
                                    print("You do not seem to have that many $eed(s) yet...")
                                else:
                                    seed_to_money = self.crypto_value * int(num_blockchain)
                                    user.money += seed_to_money

                                    for m in range(1, int(num_blockchain) + 1):
                                        user.local_blockchain.chain.pop(m)
                                    
                                    print("Processing your transaction")
                                    for i in range(3):
                                        print("...")
                                        time.sleep(0.2)
                                    print("Transaction complete!")
                                    print("\n")
                                    time.sleep(0.1)
                                    user.points += random.randint(1, 90)
                                    print("You now have ${} dollars! ".format(user.money))
                                    print('You now have {} $eed(s)'.format(len(user.local_blockchain.chain) - 1))
                                    self.transactions += 1
                                    
                                    print("-"*24)
                                    self.counter += 1
                                    break 
                                    
                            
                            elif prompt3 == "/quit":
                                print("-"*24)
                                self.counter += 1
                                break 
                                

                            else:
                                print("That input does not seem to be valid")
                    else:
                        print('You do not have that many $eeds yet!')
                        print("-"*24)
                else:
                    print("That command does not seem to be valid ")
                    print("-"*24)

            elif user_input == "4":
                print("-"*24)
                print("You currently have ${} dollars".format(user.get_money()))
                self.counter += 1
                print("-"*24)

            else:
                print('That input does not seem to be valid')    
        
    def purchase(self):

        time.sleep(0.5)
        print('Checking to see if you have enough points')
        time.sleep(0.5)
        for i in range(3):
            print("...")
            time.sleep(0.5)
        
        if user.points <= self.point_to_crypto:
            print("Looks like you do not have enough points right now. Maybe check back later! ")
            time.sleep(0.1)
            self.counter += 1
            
        else:
            sender = "$eed"
            receiver = "You"
            amount = self.point_to_crypto
            user.points = user.points - amount
            block_transaction = {"sender":sender, "receiver": receiver, "amount":amount}
            user.local_blockchain.add_block(block_transaction)
            user.local_blockchain.validate_chain()
            time.sleep(0.3)
            print()

            print("You have purchased a $eed")
            user.get_seeds()
            time.sleep(0.1)
            print('You now have {} points! '.format(user.points))
            time.sleep(0.1)
            
            
            
        self.counter += 1
        self.transactions += 1



    def value(self):
        self.crypto_value = 0.01 

        if 0 <= self.transactions <= 5:
            percentage_increase = random.uniform(0, 0.02)
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase
        
        elif 5 <= self.transactions <= 10:
            percentage_increase = random.uniform(0.02, 0.1)
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase

        elif 11 <= self.transactions <= 20:
            percentage_increase = random.uniform(0.1, 0.3)
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase

        elif 21 <= self.transactions <= 30:
            percentage_increase = random.uniform(0.3, 0.35)
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase

        elif 31 <= self.transactions <= 55:
            percentage_increase = random.uniform(0.35, 0.55)
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase

        elif 56 <= self.transactions <= 75:
            percentage_increase = random.uniform(0.55, 0.65)
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase

        elif 76 <= self.transactions <= 88:
            percentage_increase = random.uniform(0.65, 0.75)
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase
        
        elif 89 <= self.transactions <= 100:
            percentage_increase = random.uniform(0.75, 0.88)
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase

        elif 101 <= self.transactions <= 120:
            percentage_increase = random.uniform(0.88, 1.02)
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase

        elif 121 <= self.transactions <= 150:
            percentage_increase = random.uniform(1.02, 1.32)
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase

        else:
            percentage_incrase = random.uniform(1.32, random.randint(2.00, 5.00))
            percentage_increase = self.crypto_value * percentage_increase
            self.crypto_value += percentage_increase
        
        







test = Prompt()
        
print(test.interface())
