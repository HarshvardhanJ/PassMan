import random
from cryptography.fernet import Fernet
import os

upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*-_"


class PassWordManager():

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    @staticmethod
    def generate_password(length):
        passlist = "" + upper_case + lower_case + numbers + symbols
        password = "".join(random.sample(passlist, length))
        return password

    def generate_key(self):
        self.key = Fernet.generate_key()
        with open("PassMan.key", 'wb') as f:
            f.write(self.key)
        print(f"Key generated successfully! Please save it somewhere safe!") 



def main():

    done = False
    pm = PassWordManager()
    

    while not done:
        
        print('''What do you wanna do:
            [1] Generate password
            [2] Generate key
            [q] Quit''')

        option = input(">> ")

        if option == 'q':
            done = True

        elif option == "2":
            pm.generate_key()
    
        elif option == "1":
            input_length = int(input("length of the password? >> "))
            #input_path = input('Enter the path to save password >> ')
            password = pm.generate_password(input_length)
            print(f"Here is the password: {password}")
            # ALSO IMPLEMENT SAVING ENCRYPTED PASSWORD IN A FILE 

main()
