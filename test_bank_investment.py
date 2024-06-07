import pytest
from pytest import approx
from database_request import get_balance, credit_account,debit_account
from tkinter import *
import tkinter as tk


import tkinter.messagebox
import customtkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
import csv
import sqlite3

""" You need to install the SQLLITE STUDIO in order to have a graphical view
    of sqlite database, so that you could retrieve the bank account number and the current balance
    to subsitute them on the test. here is the link https://sqlitestudio.pl/
    
    Note: Due to some future manupilation, data in the database will be impacted or updated
    reason why those values below are not sustain and need to be taken in the database for the while
    you need to test functions
"""

def test_get_balance():
    assert get_balance(5000803484543) == 18592
    assert get_balance(5000803598838) == 50000
    assert get_balance(5000803838423) == 5000
 
def test_debit_account():
    assert debit_account(9438443843283,100) == 1
    assert debit_account(5000803838423,1000000) == 0
    assert debit_account(8473483764374,-100) == 0
        
def test_credit_account():
    assert credit_account(9438493949323,100) == 1
    assert credit_account(9438493949323,0) == 0
    assert credit_account(9438493949323,-100) == 0

 
"""   
def test_transfer_money():
    assert transfer_money(100,100,100) == (200,0)
    assert transfer_money(0,100,100) == (100,0)
    assert transfer_money(-100,100,100) == (0,0)
    assert transfer_money(100,0,100) == (100,0)
    assert transfer_money(100,-100,100) == (0,0)
    assert transfer_money(100,100,0) == (100,100)
    assert transfer_money(100,100,-100) == (100,100)
    assert transfer_money(100,0,0) == (100,0)
"""
   
# Run the test
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])