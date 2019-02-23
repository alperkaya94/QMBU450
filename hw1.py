import random
import datetime

class Portfolio(object):
    def __init__(self):
        self.fundDict = {}
        self.stockDict = {}
        self.cash = 0
        self.hist = []
    
            
    def buyMutualFund(self, quantity, mfType):
        mf_type = mfType.getType()
        time = datetime.datetime.now()
        if quantity <= self.cash:
            if type(quantity) == float:        
                if mf_type in self.fundDict:            
                    self.fundDict[mf_type] += quantity
                    self.cash -=quantity
                    self.hist.append(str(time) + "   " + str(quantity) + " unit " + str(mf_type) + " was purchased.")
                else:
                    self.fundDict[mf_type] = 0
                    self.fundDict[mf_type] += quantity
                    self.cash -=quantity
                    self.hist.append(str(time) + "   " + str(quantity) + " unit " + str(mf_type) + " was purchased.")
            else:
                print("Mutual funds can only be purchased as fractional shares.")
        else:
            print("There is not enough cash")
            

    def sellMutualFund(self, quantity, mfType):
        mf_type = mfType.getType()        
        randomPrice = quantity*random.uniform(0.9,1.2)
        time = datetime.datetime.now()
        if mf_type in self.fundDict:
            self.fundDict[mf_type] -= randomPrice
            self.cash +=randomPrice
            self.hist.append(str(time) + "   " + str(quantity) + " unit " + str(mf_type) + " was sold.")
        else:
            print("This portfolio does not contain " + str(mf_type) + " type of mutual fund.")
        
    def buyStock(self, share, stockName):
        stock = stockName.getStock()
        price = stockName.getPrice()
        time = datetime.datetime.now()
        if share*price <= self.cash:
            if type(share) == int:
                if stock in self.stockDict:
                    self.stockDict[stock] += share*price
                    self.cash -= share*price
                    self.hist.append(str(time) + "   " + str(share) + " share " + str(stock) + " was purchased.")
                else:
                    self.stockDict[stock] = 0
                    self.stockDict[stock] += share*price
                    self.cash -= share*price
                    self.hist.append(str(time) + "   " + str(share) + " share " + str(stock) + " was purchased.")
            else:
                print("Stocks can only be purchased as whole units.")
        else: 
            print("There is not enough cash")
    def sellStock(self, share, stockName):
        stock = stockName.getStock()
        price = stockName.getPrice()
        randomPrice = price*random.uniform(0.5,1.5)
        time = datetime.datetime.now()
        if type(share) == int:
            if stock in self.stockDict:
                self.stockDict[stock] -= share*randomPrice
                self.cash += share*randomPrice
                self.hist.append(str(time) + "   " + str(share) + " share " + str(stock) + " was sold.")
            else:
                print("This portfolio does not contain " + str(stock) + " type of stock.")
        else:
            print("Stocks can only be sold as whole units.")
            
    def addCash(self, quantity):
        self.cash += quantity
    
    def minusCash(self, quantity):
        self.cash -= quantity
    
    def history(self):
        a = 0
        while a < len(self.hist):
            print (self.hist[a])
            a += 1        
    
    
    def __str__(self):
        return "#Cash:  " + str(self.cash) + "\n" + "#Stocks:  " + str(self.stockDict) + "\n" + "#Mutual Funds:  " + str(self.fundDict) 

#    def buyBond(self, bondName):
#        bond_name = bondName.getBondName()
#       Similar buying algorithm with stock and mutual fund will be here as given specifications
        
#    def sellBond(self, bondName):
#        bond_name = bondName.getBondName()
#       Similar selling algorithm with stock and mutual fund will be here as given specifications

class MutualFund(Portfolio):
    def __init__(self, mfType):
        self.mfType = mfType
    def getType(self):
        return self.mfType
    def __str__(self):
        return str(self.mfType)
        
        
   
class Stock(Portfolio):
    def __init__(self, stockPrice, stock):
        self.stockPrice = stockPrice
        self.stock = stock
    def getPrice(self):
        return self.stockPrice
    def getStock(self):
        return self.stock
    def __str__(self):
        return str(self.stock) + " with price " + str(self.stockPrice)

class Bond(Portfolio):
    #Initialize bond with given specification as in Stock and Mutual Fund
    
    def __init__(self, bondName):
        self.bondName = bondName
    def getBondName(self):
        return self.bondName
    def __str__(self):
        return str(self.bondName)
    
        
    


asd = Portfolio()
asd.addCash(100)

s = Stock(2,"DLLD")
mf = MutualFund("Daaa")
mf2 = MutualFund("asd")
asd.buyMutualFund(10.1, mf2)
asd.buyMutualFund(20.7, mf)
asd.sellMutualFund(10, mf)
asd.buyStock(20, s)
asd.sellStock(10, s)
print(asd)
asd.history()