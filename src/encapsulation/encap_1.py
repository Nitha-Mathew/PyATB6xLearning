from dotenv import load_dotenv
import os

class Loginpage:
    def __init__(self,username,password):
        self.username=username
        self.password=password

    def login_confirm(self):
        load_dotenv()
        if (self.username == os.getenv("USERNAME") and self.password == os.getenv("PASSWORD")):
            print("login success")
        else:
            print("login failed")

username=input("Enter the username: ")
password=input("Enter the password: ")

Lp_obj=Loginpage(username, password)
Lp_obj.login_confirm()
