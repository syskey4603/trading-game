'''

Plan:
create a simple UI where we can see stocks and information/news
simple buy and sell buttons at that price then store the stock owned
add a next button after the turn is complete and show the new price

start with a simple program without UI that has stocks with prices and news for each one
create a before and after price and make it work on console after that add the Ui
add a json to add data easily also make a random generator later
add total networth and all
Add a loop for the buy/sell/pass question until valid input is provided.

'''


import random
import json

cash = 10000
networth = cash
allstocks = []
roundnum = 0
validinput = False

class Stock:
    def __init__(self, name, originalprice, newprice, news, financials, ownedshares, oldnew=False, oldstock=None):
        self.originalprice = originalprice
        self.news = news
        self.newprice = newprice
        self.financials = financials
        self.ownedshares = ownedshares
        self.name = name
        self.oldnew = oldnew
        self.oldstock = oldstock

    

def genstock(newprice, news, financials, oldnew, name=None, currentprice=None, oldstock=None):
    if(oldstock):
        newstock = Stock(oldstock.name, oldstock.newprice, newprice, news, financials, oldstock.ownedshares, oldnew, oldstock=oldstock)
    else:
        newstock = Stock(name, currentprice, newprice, news, financials, 0)
    
    return newstock

relbuy = Stock("Reliance", 2000, 2200, "profits increase by 236%", "PE ratio of 12", 0)
tcs = Stock("TCS", 1000, 600, "profits decrease by 236%", "PE ratio of 42", 0)


allstocks.append(relbuy)
allstocks.append(tcs)
relsell = genstock(1200, "reliance workers leave and die on the job", "PE ratio 45", True, oldstock=relbuy)
allstocks.append(relsell)





for x in range(len(allstocks)):
    if(allstocks[x].oldnew == True):
        allstocks[x].ownedshares = allstocks[x].oldstock.ownedshares
        allstocks[x].oldstock.ownedshares = 0

    print("Round: " + str(x+1) + " " + allstocks[x].name + " \nPrice per share: " + str(allstocks[x].originalprice))
    print("News: " + allstocks[x].news + "\n" + "Financials/Ratios: " + allstocks[x].financials)
    print("\n")

    while validinput == False:
        action = input("What would you like to do? Buy, Sell or Pass: ")

        if(action.lower() == "buy"):
            numofshares = int(input("How many shares would you like to purchase: "))
            if(cash - allstocks[x].originalprice*numofshares >= 0):
                cash = cash - allstocks[x].originalprice*numofshares
                allstocks[x].ownedshares = allstocks[x].ownedshares + numofshares
                print("You now have: " + str(cash) + "$")
                validinput = True
            else:
                print("not enough money")
        elif(action.lower() == "sell"):
            if(allstocks[x].ownedshares > 0):
                numofshares = int(input("How many shares would you like to sell: "))
                allstocks[x].ownedshares = allstocks[x].ownedshares - numofshares
                cash = cash + allstocks[x].originalprice*numofshares
                validinput = True
            else:
                print("You do not have enough shares to sell")
        elif(action.lower() == "pass"):
            validinput = True
            pass
        
        networth = cash
        for y in allstocks:
            if(y.ownedshares >0):
                networth = networth + y.ownedshares*y.newprice
                print("You own " + str(y.ownedshares) + " shares of " + y.name + " at price " + str(y.newprice))
        print("Your networth is now: " + str(networth) + "$")
        print("\n")

    validinput = False
            








'''

 At the end of each round, update prices for the next round
for stock in allstocks:
    stock.originalprice = stock.newprice
    # Optionally, generate new newprice, news, and financials for the next round



    figma token 
'''