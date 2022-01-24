import os

os.system("color b")
os.system("cls")

name = input("Type something: ")

def change():
    print(name)
    os.system("color a")
    os.system("cls")
    print(name)
    os.system("color b")
    os.system("cls")
    print(name)
    os.system("color c")
    os.system("cls")

while True:
    change()
