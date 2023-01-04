import os
import time
import json
import requests

def btcPrice():
    response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
    json_response = json.loads(response.text)
    price = json_response['price']
    splitPrice = price.split(".")
    print('BTC PRICE:', splitPrice[0])
    input("press Enter um zum Menü zu kommen")
    os.system("cls")
    return 1

def wrongInput():
    print("Bitte gebe eine gültige Zahl ein")
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")

def euroToDollar():
    dollar = float(1.06)
    userInputEuroNumber = input("Euro: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * dollar
        
        print(str(userInputEuroNumber), "Euro")
        print(str(calculate), "US-Dollar")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        euroToDollar()

def euroToFranken():
    franken = float(0.99)
    userInputEuroNumber = input("Euro: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * franken
        
        print(str(userInputEuroNumber), "Euro")
        print(str(calculate), "Schweizer Franken")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        euroToFranken()

def euroToPfund():
    pfund = float(0.88)
    userInputEuroNumber = input("Euro: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * pfund
        
        print(str(userInputEuroNumber), "Euro")
        print(str(calculate), "Pfund Sterling")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        euroToPfund()

def dollarToEuro():
    euro = float(0.95)
    userInputEuroNumber = input("US-Dollar: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * euro
        
        print(str(userInputEuroNumber), "US-Dollar")
        print(str(calculate), "Euro")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        dollarToEuro()

def dollarToFranken():
    franken = float(0.93)
    userInputEuroNumber = input("US-Dollar: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * franken
        
        print(str(userInputEuroNumber), "US-Dollar")
        print(str(calculate), "Schweizer Franken")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        dollarToFranken()

def dollarToPfund():
    pfund = float(0.83)
    userInputEuroNumber = input("US-Dollar: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * pfund
        
        print(str(userInputEuroNumber), "US-Dollar")
        print(str(calculate), "Pfund Sterling")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        dollarToPfund()

def frankenToDollar():
    dollar = float(1.07)
    userInputEuroNumber = input("Schweizer Franken: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * dollar
        
        print(str(userInputEuroNumber), "Schweizer Franken")
        print(str(calculate), "US-Dollar")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        frankenToDollar()

def frankenToEuro():
    euro = float(1.01)
    userInputEuroNumber = input("Schweizer Franken: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * euro
        
        print(str(userInputEuroNumber), "Schweizer Franken")
        print(str(calculate), "Euro")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        frankenToEuro()

def frankenToPfund():
    pfund = float(0.89)
    userInputEuroNumber = input("Schweizer Franken: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * pfund
        
        print(str(userInputEuroNumber), "Schweizer Franken")
        print(str(calculate), "Pfund Sterling")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        frankenToPfund()

def pfundToDollar():
    dollar = float(1.20)
    userInputEuroNumber = input("Pfund Sterling: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * dollar
        
        print(str(userInputEuroNumber), "Pfund Sterling")
        print(str(calculate), "US-Dollar")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        pfundToDollar()

def pfundToFranken():
    franken = float(1.12)
    userInputEuroNumber = input("Pfund Sterling: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * franken
        
        print(str(userInputEuroNumber), "Pfund Sterling")
        print(str(calculate), "Schweizer Franken")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        pfundToFranken()

def pfundToEuro():
    euro = float(1.13)
    userInputEuroNumber = input("Pfund Sterling: ")
    
    if userInputEuroNumber == "menu" or userInputEuroNumber == "back":
        os.system("cls")
        return 1

    try:
        userInputEuroNumber = int(userInputEuroNumber)
        calculate = userInputEuroNumber * euro
        
        print(str(userInputEuroNumber), "Pfund Sterling")
        print(str(calculate), "Euro")
        input("press Enter um zum Menü zu kommen")
        os.system("cls")
    except ValueError:
        os.system("cls")
        print("Bitte gebe eine Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^\n")
        pfundToEuro()

def euroToAnother():
    inputOneOptions = ["1", "2", "3", "menu", "back"]
    print("In was möchtst du es umrechen?")
    print("1 | Dollar")
    print("2 | Franken")
    print("3 | Pfund")
    userInputChois = input("chois: ")
    if userInputChois in inputOneOptions:
        if userInputChois == "1":
            os.system("cls")
            euroToDollar()
        
        if userInputChois == "2":
            os.system("cls")
            euroToFranken()
        
        if userInputChois == "3":
            os.system("cls")
            euroToPfund()
        
        if userInputChois == "menu" or userInputChois == "back":
            os.system("cls")
            return 1

    else:
        os.system("cls")
        print("Bitte gebe eine gültige Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        euroToAnother()

def dollarToAnother():
    dollarToAnotherOptions = ["1", "2", "3", "menu", "back"]
    print("In was möchtst du es umrechen?")
    print("1 | Euro")
    print("2 | Franken")
    print("3 | Pfund")
    userInputChois = input("chois: ")
    if userInputChois in dollarToAnotherOptions:
        if userInputChois == "1":
            os.system("cls")
            dollarToEuro()
        
        if userInputChois == "2":
            os.system("cls")
            dollarToFranken()
        
        if userInputChois == "3":
            os.system("cls")
            dollarToPfund()
    else:
        os.system("cls")
        print("Bitte gebe eine gültige Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        dollarToAnother()

def frankenToAnother():
    dollarToAnotherOptions = ["1", "2", "3", "menu", "back"]
    print("In was möchtst du es umrechen?")
    print("1 | Dollar")
    print("2 | Euro")
    print("3 | Pfund")
    userInputChois = input("chois: ")
    if userInputChois in dollarToAnotherOptions:
        if userInputChois == "1":
            os.system("cls")
            frankenToDollar()
        
        if userInputChois == "2":
            os.system("cls")
            frankenToEuro()
        
        if userInputChois == "3":
            os.system("cls")
            frankenToPfund()
    else:
        os.system("cls")
        print("Bitte gebe eine gültige Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        frankenToAnother()

def pfundToAnother():
    dollarToAnotherOptions = ["1", "2", "3", "menu", "back"]
    print("In was möchtst du es umrechen?")
    print("1 | Dollar")
    print("2 | Euro")
    print("3 | Franken")
    userInputChois = input("chois: ")
    if userInputChois in dollarToAnotherOptions:
        if userInputChois == "1":
            os.system("cls")
            pfundToDollar()
        
        if userInputChois == "2":
            os.system("cls")
            pfundToEuro()
        
        if userInputChois == "3":
            os.system("cls")
            pfundToFranken()
    else:
        os.system("cls")
        print("Bitte gebe eine gültige Zahl ein")
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n")
        pfundToAnother()

inputOptions = ["1", "2", "3", "4", "btc", "info", "exit"]

while 1:
    print("Wähle deine wärung die du in eine andere umrechnen willst:")
    print("1 | Euro") 
    print("2 | Dollar")
    print("3 | Franken")
    print("4 | Pfund")
    print("btc für Bitcoin Kurs\n")
    userInput = input("ValueConverter: ")
    
    if userInput in inputOptions:
        if userInput.lower() == "btc":
            os.system("cls")
            btcPrice()
        
        if userInput.lower() == "1":
            os.system("cls")
            euroToAnother()
        
        if userInput.lower() == "2":
            os.system("cls")
            dollarToAnother()
        
        if userInput.lower() == "3":
            os.system("cls")
            frankenToAnother()
        
        if userInput.lower() == "4":
            os.system("cls")
            pfundToAnother()
        
        if userInput.lower() == "exit":
            os.system("cls")
            exit("Danke fürs nutzen")
    else:
        wrongInput()