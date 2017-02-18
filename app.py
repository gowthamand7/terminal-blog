from menu import Menu
from monogoDB import Database


Database.initialize()

menu = Menu()
menu.user()
menu.runMenu()