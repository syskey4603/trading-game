import customtkinter as ctk



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
            







class StockMarketGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Stock Market Simulator")
        self.geometry("500x600")

        # Setting the theme colors
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.create_widgets()

    def create_widgets(self):
        # News Section
        self.news_label = ctk.CTkLabel(self, text="News", font=("Arial", 14))
        self.news_label.pack(pady=(10, 5))

        self.news_text = ctk.CTkLabel(self, text="(Your news will be displayed here)", font=("Arial", 12), width=450, height=100, anchor="nw", justify="left", wraplength=450)
        self.news_text.pack(padx=10, pady=(0, 10))

        # Financial Ratios Section
        self.financial_label = ctk.CTkLabel(self, text="Financial Ratios", font=("Arial", 14))
        self.financial_label.pack(pady=(10, 5))

        self.financial_text = ctk.CTkLabel(self, text="(Your financial ratios will be displayed here)", font=("Arial", 12), width=450, height=100, anchor="nw", justify="left", wraplength=450)
        self.financial_text.pack(padx=10, pady=(0, 10))

        # Buy, Sell, Pass Buttons
        self.buttons_frame = ctk.CTkFrame(self)
        self.buttons_frame.pack(pady=(10, 20))

        self.buy_button = ctk.CTkButton(self.buttons_frame, text="Buy", command=lambda: self.buy_action())
        self.buy_button.grid(row=0, column=0, padx=10)

        self.sell_button = ctk.CTkButton(self.buttons_frame, text="Sell", command=lambda: self.sell_action())
        self.sell_button.grid(row=0, column=1, padx=10)

        self.pass_button = ctk.CTkButton(self.buttons_frame, text="Pass", command=lambda: self.pass_action())
        self.pass_button.grid(row=0, column=2, padx=10)

        # Slider to select the number of shares
        self.slider_label = ctk.CTkLabel(self, text="Select Number of Shares", font=("Arial", 14))
        self.slider_label.pack(pady=(10, 5))

        self.shares_slider = ctk.CTkSlider(self, from_=1, to=100, number_of_steps=100, command=self.update_slider_value)
        self.shares_slider.pack(pady=(0, 5))

        self.slider_value_label = ctk.CTkLabel(self, text="1", font=("Arial", 12))
        self.slider_value_label.pack()

        

    def update_slider_value(self, value):
        self.slider_value_label.configure(text=str(int(float(value))))

    def buy_action(self):
        numofshares = int(self.shares_slider.get())
        if(cash - allstocks[x].originalprice*numofshares >= 0):
                cash = cash - allstocks[x].originalprice*numofshares
                allstocks[x].ownedshares = allstocks[x].ownedshares + numofshares
                print("You now have: " + str(cash) + "$")
                validinput = True
        else:
            print("not enough money")
        print("Buy action executed with {} shares".format(int(self.shares_slider.get())))

    def sell_action(self):
        numofshares = int(self.shares_slider.get())
        if(allstocks[x].ownedshares > 0):
                numofshares = int(input("How many shares would you like to sell: "))
                allstocks[x].ownedshares = allstocks[x].ownedshares - numofshares
                cash = cash + allstocks[x].originalprice*numofshares
                validinput = True
        else:
            print("You do not have enough shares to sell")
        print("Sell action executed with {} shares".format(int(self.shares_slider.get())))

    def pass_action(self):
        validinput = True
        pass
        print("Pass action executed")
            
    networth = cash
    for y in allstocks:
        if(y.ownedshares >0):
            networth = networth + y.ownedshares*y.newprice
            print("You own " + str(y.ownedshares) + " shares of " + y.name + " at price " + str(y.newprice))
    print("Your networth is now: " + str(networth) + "$")
    print("\n")

validinput = False
            

if __name__ == "__main__":
    app = StockMarketGUI()
    app.mainloop()