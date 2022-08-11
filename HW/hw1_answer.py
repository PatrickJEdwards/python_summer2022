# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 22:38:21 2022

@author: edwar

@title: Homework #1: Python Summer Course 2022
"""

# Tasks/functions---three items & some general requirements.
## ITEM 1: CASH.
### CASH FUNCTIONS.
#### C.F1: Added to portfolio.
#### C.F2: Removed from portfolio.
#### C.F3: Used to buy stocks/mutual funds.

## ITEM 2: STOCK.
### STOCK FUNCTIONS.
#### S.F1: Purchased with existing cash in the portfolio.
#### S.F2: Sold (adding cash to portfolio).
### STOCK REQUIREMENTS.
#### S.R1: Stocks can only be bought/sold as whole units.
#### S.R2: Stocks havea price and ticker symbol.
#### S.R3: Stocks can be purchased for $X/share.
#### S.R4: When stocks are sold, they are sold for a price 
####       that is uniformly drawn from [0.5X-1.5X]

## ITEM 3: MUTUAL FUNDS.
### MUTUAL FUND FUNCTIONS.
#### S.F1: Purchased with existing cash in the portfolio.
#### S.F2: Sold, adding cash to portfolio.
### MUTUAL FUND REQUIREMENTS.
#### S.R1: Mutual funds can only be purchased as fractional shares.
#### S.R2: Mutual funds have a price and ticker symbol.
#### S.R3: Mutual funds can be purchased for $1/share.
#### S.R4: Mutual funds are sold for a price that is uniformly drawn 
####       from [0.9-1.2]

## GENERAL REQUIREMENTS.
### G.R1: Your program must facilitate managing the correct balance of 
###       cash, stocks and mutual funds as the user buys and sells items.
### G.R2: in order to help with customer service your portfolio software 
###       needs to keep an audit log of all transactions and make them 
###       available to users of your program.



# STRATEGY: Organize stock/mutual fund info in portfolio as LIST OF DICTIONARIES.
##          Each list entry is type of stock/mutual fund.
##          And each dictionary entry is CHARACTERISTIC of stock/mutual fund (buying price, symbol, time/date of purchase).


# STEP 1: Create Stock Class (UNFINISHED).
class Stock():
    def __init__(self, price, symb):
        self.price = price # Stock price, no default
        self.symb = symb # Stock symbol, no default

# STEP 2: Create Mutual Fund Class (UNFINISHED).
class MutualFund():
    def __init__(self, symb):
        self.symb = symb # Mutual Fund Symbol.
        self.price = 1 # Buying price, $1/share default.

# STEP 3: Create Portfolio Class. (UNFINISHED).
class Portfolio():
    def ___init___(self):
        self.balance = 0 # Portfolio cash balance, initially zero.
        self.stock = [] # Portfolio stock balance, initially empty list of dictionaries.
        self.mutualfund = [] # Portfolio mutual fund balance, initially empty list of dictionaries.
        self.audit_log = [] # Audit log, initially empty list.
    
    def addCash(self, amt):
        # Ensure `amt` input is U.S. currency form.
            # Must be integer or float
            # No 1000th or smaller decimals (I just round it)
        if type(amt) not in [int, float]:
            raise Exception("Cannot use non-numeric inputs. Please provide numeric cash deposit.")
        if amt % 1 != 0:
            string_amt = f"{amt}"
            amt_dec = str(int(string_amt.split(".")[1]))
            if len(amt_dec) > 2:
                raise Exception("Cash deposits cannot have more than two decimal places.")
  
s = Portfolio()

s.addCash(500)
s.addCash("500")
s.addCash(500.53)
s.addCash(500.522)
        
amt = 500.306
amt2 = 5



    #def withdrawCash(self, amt):
        
    #def buyStock(self, amt, symb):
        
    #def sellStock(self, symb, amt):
        
    #def buyMutualFund(self, amt, symb):
        
    #def sellMutualFund(self, symb, amt):
        
    #def __str__(self): #Print function.
        
    #def history(self):
        
    


