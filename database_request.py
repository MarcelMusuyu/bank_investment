import sqlite3
# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime
import tkinter as tk
current_date_and_time = datetime.now()
DATABASE_NAME = "bank_investment.db"


def connect_db(database_name):
    """Create a Sqlite3 Database
    and return a cursor Object.

    Parameter database_name: the name of the database to exploit
    Return: a connection object
    """
    #Databases
    try:
        #Create a database
        conn = sqlite3.connect(database=database_name)
        
        #Create a cursor
        
    
        return conn
    except Exception as e:
        try:
            with open("db_files.log","at") as log:
                log.write(f'{current_date_and_time},{str(e)}')
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {log}"
                " because you don't have permission.")
        conn.rollback()
        conn.close()

        
def create_tables(database_name):
    """Create tables to our existing database
    and return boolean value True if success and False if not .

    Parameter database_name: the name of the database where we want create or alter tables
    Return: a boolean value
    """
    conn=connect_db(database_name)
    cursor_ob= conn.cursor() 
    try:
       
            
        #Create Clients table

        cursor_ob.execute("""CREATE TABLE Clients (
                    clientNumber integer PRIMARY KEY AUTOINCREMENT,
                    lastName text,
                    firstName text,
                    address text,
                    phoneNumber text,
                    email text,
                    dateOfBirth DATE,
                    identificationDocument text
        )""")
            
        cursor_ob.execute("""CREATE TABLE Accounts (
                    accountNumber integer PRIMARY KEY,
                    accountType text,
                    bank_name text,
                    balance DECIMAL(10,2),
                    currency text,
                    bic_code text,
                    openingDate DATE,
                    clientNumber integer,
                    FOREIGN KEY (clientNumber) REFERENCES Clients(clientNumber))
        """)
            
        cursor_ob.execute("""CREATE TABLE Transactions (
                    transactionNumber integer PRIMARY KEY AUTOINCREMENT,
                    transactionDate DATE,
                    transactionType text,
                    amount DECIMAL(10,2),
                    accountNumber integer,
                    FOREIGN KEY (accountNumber) REFERENCES Accounts(accountNumber))
        """)
            
        cursor_ob.execute("""CREATE TABLE Investments (
                    investmentNumber integer PRIMARY KEY AUTOINCREMENT,
                    investmentType text,
                    investedAmount DECIMAL(10,2),
                    purchaseDate DATE,
                    accountNumber integer,
                    FOREIGN KEY (accountNumber) REFERENCES Accounts(accountNumber))
        """)
            
        cursor_ob.execute("""CREATE TABLE Stocks (
                    StockID integer PRIMARY KEY AUTOINCREMENT,
                    date text,
                    stockSymbol text,
                    companyName text,
                    market text,
                    Volume integer,
                    currentPrice DECIMAL(10,2),
                    highPrice DECIMAL(10,2),
                    currency text)
        """)
        cursor_ob.execute("""CREATE TABLE StockTrades (
                    tradeID integer PRIMARY KEY AUTOINCREMENT,
                    accountNumber integer,
                    stockID integer,
                    tradeType text,
                    tradeDate DATE,
                    quantity integer,
                    pricePerShare DECIMAL(10,2),
                    FOREIGN KEY (accountNumber) REFERENCES Accounts(accountNumber),
                    FOREIGN KEY (stockID) REFERENCES Stocks(stockID))
        """)
        cursor_ob.execute("""CREATE TABLE StockPortfolios (
                    portfolioID integer PRIMARY KEY AUTOINCREMENT,
                    accountNumber integer,
                    stockID integer,
                    sharesHeld integer,
                    averageCostPerShare DECIMAL(10,2),
                    unrealizedGainLoss DECIMAL(10,2),
                    FOREIGN KEY (accountNumber) REFERENCES Accounts(accountNumber),
                    FOREIGN KEY (stockID) REFERENCES Stocks(stockID))
                            
        """)
        conn.commit()
       
        return True
        
    except Exception as e:
        
        try:
            with open("db_files.log","at") as log:
                log.write(f'{current_date_and_time},{str(e)}')
                 
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {log}"
                " because you don't have permission.")
        conn.rollback()
        conn.close()
        return False
           
    finally:
        
        conn.close()
    
    
def get_balance(account_number):
    """Get the balance of the account from the bank."""
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor() 
    try:
       balance= cursor_ob.execute("""SELECT balance FROM Accounts WHERE accountNumber = ?""",(account_number,))
       return balance.fetchone()[0]
    except Exception as e:
       
        try:
            with open("db_files.log","at") as log:
                log.write(f' {current_date_and_time} {str(e)}')
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {log}"
                " because you don't have permission.")
        conn.rollback()
        conn.close()
        return None   
def debit_account(account_number, amount):
    """Debit an account."""
    # Get the balance of the account
    balance = get_balance(account_number)
    if balance is None:
        tk.messagebox.showerror("Account Not Found", "The account number you entered was not found.")
        return 0
    # Check if the account has enough money
    if balance < amount:
        tk.messagebox.showerror("Insufficient Funds", "You don't have enough money in your account.")
        return 0
    if amount < 0:
        tk.messagebox.showerror("Bad Number", "You need to choose a greater number.")
        return 0
    # Debit the account
    new_balance = balance - amount
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor() 
    try:
        cursor_ob.execute("""UPDATE Accounts SET balance = ? WHERE accountNumber = ?""", (new_balance, account_number))
        conn.commit()
        return 1
    except Exception as e:
        
        try:
            with open("db_files.log","at") as log:
                log.write(f'{current_date_and_time} {str(e)} ')
                log.write("\n")
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                " because you don't have permission.")
        conn.rollback()
        conn.close()
        return 0
def credit_account(account_number, amount):
    """Credit an account."""
    # Get the balance of the account
    balance = get_balance(account_number)
    if balance is None:
        tk.messagebox.showerror("Account Not Found", "The account number you entered was not found.")
        return 0
    # Credit the account
    if amount <= 0:
        return 0
    new_balance = balance + amount
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor() 
    try:
        cursor_ob.execute("""UPDATE Accounts SET balance = ? WHERE accountNumber = ?""", (new_balance, account_number))
        conn.commit()
        return 1
    except Exception as e:
        
        try:
            with open("db_files.log","at") as log:
                log.write(f'{str(e)}')
                log.write("\n")
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                " because you don't have permission.")
        conn.rollback()
        conn.close()
        return 0

        

def buy_stock(account_number, stock_symbol, quantity, price_per_share):
    balance = get_balance(account_number)
    if balance is None:
        tk.messagebox.showerror("Account Not Found", "The account number you entered was not found.")
        return 0
    total_cost = quantity * price_per_share
    if balance < total_cost:
        messagebox.showerror("Insufficient Funds", "You don't have enough money in your account.")
        return
    new_balance = balance - total_cost
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        debit_account(account_number, total_cost)
        cursor_ob.execute("""SELECT StockID FROM Stocks WHERE StockSymbol = ?""", (stock_symbol,))
        stock_id = cursor_ob.fetchone()[0]
        cursor_ob.execute("""INSERT INTO StockTrades (accountNumber, stockID, tradeType, tradeDate, quantity, pricePerShare) VALUES (?, ?, ?, ?, ?, ?)""", (account_number, stock_id, "Buy", current_date_and_time, quantity, price_per_share))
        conn.commit()
        return 1
    except Exception as e:
            
        try:
            with open("transact_files.log","at") as log:
                   
                log.write(f'{str(e)} {current_date_and_time} {account_number} {stock_id} {quantity} {price_per_share}')
                log.write("\n")       
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {log}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        return 0
    
def sell_stock(account_number, stock_symbol, quantity, price_per_share):
    balance = get_balance(account_number)
    if balance is None:
        tk.messagebox.showerror("Account Not Found", "The account number you entered was not found.")
        return 0
    total_cost = quantity * price_per_share
    new_balance = balance + total_cost
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        credit_account(account_number, total_cost)
        cursor_ob.execute("""SELECT StockID FROM Stocks WHERE StockSymbol = ?""", (stock_symbol,))
        stock_id = cursor_ob.fetchone()[0]
        cursor_ob.execute("""INSERT INTO StockTrades (accountNumber, stockID, tradeType, tradeDate, quantity, pricePerShare) VALUES (?, ?, ?, ?, ?, ?)""", (account_number, stock_id, "Sell", current_date_and_time, quantity, price_per_share))
        conn.commit()
        return 1
    except Exception as e:
            
        try:
            with open("transact_files.log","at") as log:
                   
                log.write(f'{str(e)} {current_date_and_time} {account_number} {stock_id} {quantity} {price_per_share}')
                log.write("\n")   
                        
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {log}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        return 0
    
def get_stock_trades(account_number):
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        cursor_ob.execute("""SELECT tradeDate, tradeType, quantity, pricePerShare FROM StockTrades WHERE accountNumber = ?""", (account_number,))
        trades = cursor_ob.fetchall()
        return trades
    except Exception as e:
        try:
            with open("transact_files.log","at") as log:
                   
                    log.write(f'{str(e)} {current_date_and_time} {account_number}')
                    log.write("\n")
               
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {lperm_err}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        
        return []
    
def get_investment_report(account_number):
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        cursor_ob.execute("""SELECT purchaseDate, investmentType, investedAmount FROM Investments WHERE accountNumber = ?""", (account_number,))
        trades = cursor_ob.fetchall()
        return trades
    except Exception as e:
        try:
            with open("transact_files.log","at") as log:
                   
                    log.write(f'{str(e)} {current_date_and_time} {account_number}')
                    log.write("\n")
               
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {lperm_err}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        
        return []
    

    
def get_stock_prices(stock_symbol):
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        cursor_ob.execute("""SELECT tradeDate, pricePerShare FROM StockTrades WHERE StockSymbol = ?""", (stock_symbol,))
        prices = cursor_ob.fetchall()
        return prices
    except Exception as e:
        try:
            with open("transact_files.log","at") as log:
                   
                log.write(f'{str(e)} {current_date_and_time} {stock_symbol}')
                log.write("\n") 
                        
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {log}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        return 0
    
def get_stock_price(stock_symbol):
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        cursor_ob.execute("""SELECT currentPrice FROM Stocks WHERE stockSymbol = ?""", (stock_symbol,))
        price = cursor_ob.fetchone()
        return price[0]
    except Exception as e:
        try:
            with open("transact_files.log","at") as log:
                   
                log.write(f'{str(e)} {current_date_and_time} {stock_symbol}')
                log.write("\n") 
                        
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        return 0

def insert_stock_data(stock_data):
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        cursor_ob.execute("""INSERT INTO Stocks (date,stockSymbol, companyName, market, volume, currentPrice, highPrice, currency) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", stock_data)
        conn.commit()
        return 1
    except Exception as e:
        try:
            with open("stocks_Mmarket_files.log","wt") as log:
                   
                log.write(f'{str(e)} {current_date_and_time}')
                log.write("\n")  
                        
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        return 0
        
def insert_stock_trade(trade_data):
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        cursor_ob.execute("""INSERT INTO StockTrades (accountNumber, stockID, tradeType, tradeDate, quantity, pricePerShare) VALUES (?, ?, ?, ?, ?, ?)""", trade_data)
        conn.commit()
        return 1
    except Exception as e:
        try:
            with open("stocks_files.log","at") as log:
                   
                log.write(f'{str(e)} {current_date_and_time} {trade_data}')
                log.write("\n")
                        
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        return 0
    
def insert_stock_portfolio(portfolio_data):
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        cursor_ob.execute("""INSERT INTO StockPortfolios (accountNumber, stockID, sharesHeld, averageCostPerShare, unrealizedGainLoss) VALUES (?, ?, ?, ?, ?)""", portfolio_data)
        conn.commit()
        return 1
    except Exception as e:
        try:
            with open("portofolios.log","at") as log:
                   
                    log.write(f'{str(e)} {current_date_and_time} {portfolio_data}')
                    log.write("\n")
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        return 0
    
        
def insert_account(account_data):
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        cursor_ob.execute("""INSERT INTO Accounts (accountNumber,accountType, bank_name,balance,currency,bic_code ,openingDate, clientNumber) VALUES (?,?,?,?, ?, ?, ?,?)""", account_data)
        conn.commit()
        return 1
    except Exception as e:
        try:
            with open("account_files.log","at") as log:
                   
                log.write(f'{str(e)} {current_date_and_time} {account_data}')
                log.write("\n")
                        
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        return 0
    
def insert_transaction(transaction_data):
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        cursor_ob.execute("""INSERT INTO Transactions (transactionDate, transactionType, amount, accountNumber) VALUES (?, ?, ?, ?)""", transaction_data)
        conn.commit()
        return 1
    except Exception as e:
        try:
            with open("transact_files.log","at") as log:
                   
                    log.write(f'{str(e)} {current_date_and_time} {transaction_data}')
                    log.write("\n")   
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {log}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        return 0
    
def insert_investment(investment_data):
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor()
    try:
        cursor_ob.execute("""INSERT INTO Investments (investmentType, investedAmount, purchaseDate, accountNumber) VALUES (?, ?, ?, ?)""", investment_data)
        conn.commit()
        return 1
    except Exception as e:
        try:
            with open("investment_files.log","at") as log:
                   
                    log.write(f'{str(e)} {current_date_and_time} {investment_data}')
                    log.write("\n")  
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {log}"
                    " because you don't have permission.")
            conn.rollback()
            conn.close()
        return 0
    
def insert_client(client_data):
        conn=connect_db(DATABASE_NAME)
        cursor_ob= conn.cursor()
        try:
            cursor_ob.execute("""INSERT INTO Clients (lastName, firstName, address, phoneNumber, email, dateOfBirth, identificationDocument) VALUES (?, ?, ?, ?, ?, ?, ?)""", client_data)
            conn.commit()
            return 1
        except Exception as e:
            try:
                with open("clients.log","at") as log:
                    log.write(f'{str(e)} {current_date_and_time} {client_data}')
                    log.write("\n")
                               
            except FileNotFoundError as err_file:
                print(err_file)
            except PermissionError as perm_err:
                print(f"Error: cannot write to {perm_err}"
                        " because you don't have permission.")
                conn.rollback()
                conn.close()
            return 0
    
    
def get_all_stock():
    
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor() 
    try:
       balance= cursor_ob.execute("""SELECT * FROM Stocks""")
       return balance.fetchall()
    except Exception as e:
        
        try:
            with open("db_files.log","at") as log:
               log.write(f'{str(e)} {current_date_and_time}')
               log.write("\n")
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                " because you don't have permission.")
        conn.rollback()
        conn.close()
        return 0    
    
def get_stock_symbols():
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor() 
    symbols=[]
    try:
       balance= cursor_ob.execute("""SELECT stockSymbol FROM Stocks""")
    
       tuples= balance.fetchall()
       for value in tuples:
           symbols.append(value[0])
       return symbols
    except Exception as e:
        
        try:
            with open("stocks_files.log","at") as log:
              log.write(f'{str(e)} {current_date_and_time}')
              log.write("\n")
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                " because you don't have permission.")
        conn.rollback()
        conn.close()
        return 0
    
def get_ID_stock(stock_symbol):
    """The specified stock data from symbol."""
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor() 
    symbols=[]
    try:
       stock= cursor_ob.execute("""SELECT DISTINCT StockID FROM Stocks WHERE StockSymbol = ?""", (stock_symbol,))
       tuples= stock.fetchone()[0]
       
       return tuples
    except Exception as e:
        
        try:
            with open("db_files.log","at") as log:
                log.write(f'{str(e)} {current_date_and_time}')
                log.write("\n")
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                " because you don't have permission.")
        conn.rollback()
        conn.close()
        return 0    
def get_stock_from_symbol(stock_symbol):
    """The specified stock data by symbol."""
    conn=connect_db(DATABASE_NAME)
    cursor_ob= conn.cursor() 
    symbols=[]
    try:
       stock= cursor_ob.execute("""SELECT DISTINCT StockID,companyName,market,date,currentPrice,highPrice,currency FROM Stocks WHERE StockSymbol = ?""", (stock_symbol,))
       tuples= stock.fetchone()
       
       return tuples
    except Exception as e:
        
        try:
            with open("db_files.log","at") as log:
                log.write(f'{str(e)} {current_date_and_time}')
                log.write("\n")
        except FileNotFoundError as err_file:
            print(err_file)
        except PermissionError as perm_err:
            print(f"Error: cannot write to {perm_err}"
                " because you don't have permission.")
        conn.rollback()
        conn.close()
        return 0    