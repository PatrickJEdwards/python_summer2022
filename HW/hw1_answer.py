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


# Import packages for uniform sampling.
from random import uniform



# STEP 1: Create Stock Class.
class Stock():
    def __init__(self, price, symb):
        # Ensure stock price argument is numeric.
        if type(price) not in [int, float]:
            raise Exception("Stock price must be numeric.")
        if type(symb) not in [str]:
            raise Exception("Stock symbol must be string.")
        self.price = price # Stock price, no default
        self.symb = symb # Stock symbol, no default

# STEP 2: Create Mutual Fund Class.
class MutualFund():
    def __init__(self, symb):
        if type(symb) not in [str]:
            raise Exception("mutual fund symbol must be string.")
        self.symb = symb # Mutual Fund Symbol.
        self.price = 1 # Buying price, $1/share default.

# STEP 3: Create Portfolio Class. (UNFINISHED).
class Portfolio():
    def __init__(self, balance = 0):
        # Create portfolio of cash balance, stocks, and mutual funds.
        self.holdings = {"balance" : balance, "stocks" : {}, "mutualfunds" : {}}
        # Audit log, initially empty list.
        self.audit_log = [] 
    
    def addCash(self, amt):
        # Ensure `amt` input is U.S. currency form.
        # Must be integer or float.
        if type(amt) not in [int, float]:
            raise Exception("Cannot use non-numeric inputs. Please provide numeric cash deposit.")
        # No 1000th or smaller decimals (I just round it)
        if amt % 1 != 0:
            string_amt = f"{amt}"
            amt_dec = str(int(string_amt.split(".")[1]))
            if len(amt_dec) > 2:
                raise Exception("Cash deposits cannot have more than two decimal places.")
        # `amt` must be positive.
        if amt <= 0:
            raise Exception("Cash deposits must be greater than zero.")
        # Add to balance.
        self.holdings["balance"] += amt
        # Add to audit_log.
        self.audit_log.append(f"${amt} Deposited.\n")

    def withdrawCash(self, amt):
        # Must be integer or float.
        if type(amt) not in [int, float]:
            raise Exception("Cannot use non-numeric inputs. Please provide numeric cash deposit.")
        # No 1000th or smaller decimals (I just round it)
        if amt % 1 != 0:
            string_amt = f"{amt}"
            amt_dec = str(int(string_amt.split(".")[1]))
            if len(amt_dec) > 2:
                raise Exception("Cash deposits cannot have more than two decimal places.")
        # `amt` must be positive.
        if amt <= 0:
            raise Exception("Cash withdrawals must be greater than zero.")
        # Amount withdraw cannot be greater than total balance.
        if amt > self.holdings["balance"]:
            raise Exception("Cash withdrawals cannot exceed total cash balance.")
        
        # Subtract from balance.
        self.holdings["balance"] -= amt
        # Add to audit_log.
        self.audit_log.append(f"${amt} Withdrawn.\n")
        
    def buyStock(self, stock_amt, stock):
        # Ensure stock_amt argument is numeric.
        if type(stock_amt) not in [int, float]:
            raise Exception("Stock amount must be numeric whole number.")
        # Ensure amount bought is whole number.
        if stock_amt % 1 != 0:
            raise Exception("Stocks can only be bought in whole units.")
        # Ensure amount bought is positive number.
        if stock_amt <= 0:
            raise Exception("Amount of stock purchased must be positive number.")
        
        # Subtract stock amount times price from portfolio's cash balance.
        self.withdrawCash(stock_amt*stock.price)
        # Check if stock has not previously been included.
        if stock.symb not in self.holdings["stocks"].keys():
            self.holdings["stocks"][stock.symb] = {"stock_amt" : stock_amt, "price" : stock.price}
        # If stock previously included, then add existing stock inventory to new stocks.
        else:
            self.holdings["stocks"][stock.symb] = {"stock_amt" : self.holdings["stocks"][stock.symb]["stock_amt"] + stock_amt, "price" : stock.price}
        # Add to audit_log.
        self.audit_log.append(f"{stock_amt} of stock {stock.symb} purchased for ${stock_amt*stock.price}.\n")
        
    def sellStock(self, symb, stock_amt):
        # Ensure stock_amt argument is numeric.
        if type(stock_amt) not in [int, float]:
            raise Exception("Stock amount must be numeric whole number.")
        # Ensure amount sold is whole number.
        if stock_amt % 1 != 0:
            raise Exception("Stocks can only be sold in whole units.")
        # Ensure amount sold is positive number.
        if stock_amt <= 0:
            raise Exception("Amount of stock sold must be positive number.")
        # Calculate selling price by sampling from uniform distribution.
        sellprice = uniform(self.holdings["stocks"][symb]["price"] * .5, self.holdings["stocks"][symb]["price"] * 1.5)
        
        # Ensure that removing this from stock inventory doesn't result in negative stock inventory.
        if self.holdings["stocks"][symb]["stock_amt"] - stock_amt < 0:
            raise Exception(f"Not enough stocks in portfolio to sell {stock_amt}")
        # Otherwise remove sold stocks from stock inventory.
        else:
            self.holdings["stocks"][symb]["stock_amt"] -= stock_amt
            
        # Add the money gained from selling stock to balance. Round to ensure only two decimal places.
        self.addCash(round(stock_amt * sellprice, 2))
        
        # Add to audit_log.
        self.audit_log.append(f"{stock_amt} of stock {symb} sold for ${round(stock_amt * sellprice, 2)}.\n")
            
        
    def buyMutualFund(self, mut_amt, mutfund):
        # Ensure mut_amt argument is numeric.
        if type(mut_amt) not in [int, float]:
            raise Exception("Mutual fund amount must be numeric whole number.")
        # Ensure amount bought is positive number.
        if mut_amt <= 0:
            raise Exception("Amount of mutual funds purchased must be positive number.")
        
        # Subtract mutual fund amount times price from portfolio's cash balance.
        mutualfund_price = 1
        self.withdrawCash(mut_amt * mutualfund_price)
        # Check if mutual fund has not previously been included.
        if mutfund not in self.holdings["mutualfunds"].keys():
            self.holdings["mutualfunds"][mutfund.symb] = {"mut_amt" : mut_amt, "price" : mutualfund_price}
        # If stock previously included, then add existing stock inventory to new stocks.
        else:
            self.holdings["mutualfunds"][mutfund.symb] = {"mut_amt" : self.holdings["mutualfunds"][mutfund.symb]["mut_amt"] + mut_amt, "price" : mutualfund_price}
        # Add to audit_log.
        self.audit_log.append(f"{mut_amt} of mutual fund {mutfund.symb} purchased for ${mut_amt*mutualfund_price}.\n")
 
        
    def sellMutualFund(self, symb, mut_amt):
        # Ensure mut_amt argument is numeric.
        if type(mut_amt) not in [int, float]:
            raise Exception("mutual fund amount must be numeric type.")
        # Ensure amount sold is positive number.
        if mut_amt <= 0:
            raise Exception("Amount of mutual fund sold must be positive number.")
        # Calculate selling price by sampling from uniform distribution.
        sellprice = uniform(self.holdings["mutualfunds"][symb]["price"] * .9, self.holdings["mutualfunds"][symb]["price"] * 1.2)
        
        # Ensure that removing this from stock inventory doesn't result in negative stock inventory.
        if self.holdings["mutualfunds"][symb]["mut_amt"] - mut_amt < 0:
            raise Exception(f"Not enough mutual funds in portfolio to sell {mut_amt}")
        # Otherwise remove sold mutual funds from mutual fund inventory.
        else:
            self.holdings["mutualfunds"][symb]["mut_amt"] -= mut_amt
            self.holdings["mutualfunds"][symb]["mut_amt"] = round(self.holdings["mutualfunds"][symb]["mut_amt"], 2)
            
        # Add the money gained from selling stock to balance. Round to ensure only two decimal places.
        self.addCash(round(mut_amt * sellprice, 2))
        
        # Add to audit_log.
        self.audit_log.append(f"{mut_amt} of mutual fund {symb} sold for ${round(mut_amt * sellprice, 2)}.\n")
            
    
    def __str__(self): #Print function.
        # Add header
        print_string = "Portfolio Inventory:\n"
        # Add information about cash balance.
        print_string += f"Cash Balance: {self.holdings['balance']}\n"
        # Add information about stocks.
        for i, j in self.holdings["stocks"].items():
            stock_amt = j["stock_amt"]
            print_string += f"{i}: {stock_amt}\n"
        # Add information about mutual funds.
        for i, j in self.holdings["mutualfunds"].items():
            mut_amt = j["mut_amt"]
            print_string += f"{i}: {mut_amt}\n"
        
        # Return resulting massive string.
        return print_string
        
    def history(self):
        # Join together audit_log.
        output = "".join(portfolio.audit_log)
        print(output)
    






# Must be functional commands.
portfolio = Portfolio() #Creates a new portfolio
portfolio.addCash(300.50) #Adds cash to the portfolio
s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
portfolio.buyStock(5, s) #Buys 5 shares of stock s
mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
print(portfolio) #Prints portfolio
                 #cash: $140.50
                 #stock: 5 HFH
                 #mutual funds: 10.33 BRT
                 #              2     GHT
portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
portfolio.withdrawCash(50) #Removes $50
portfolio.history() #Prints a list of all transactions
                    #ordered by time

