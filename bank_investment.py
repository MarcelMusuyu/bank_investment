# Copyright 2024, Brigham Young University-Idaho- Nyembo Musuyu Marcel. All rights reserved.
"""
    IN OUR APPLICATION WE TAKE CARE TO CREATE VIRTUAL ENVIRONMENT, THIS VE names venv HOLDS ALL MODULES
    AND PACKAGES REQUIRED TO RUN THIS APPLICATION. YOU DON'T NEED TO INSTALL THEM
    HERE WE CHOOSE TO USE SQLITE3 DATABASE, IS AN EMBEDDED DATABASE WITH .db extenstion.
    
    IN ORDER TO HAVE A GRAPHICAL VIEW OF HOW REALLY LOOKS THE bank_investment.db DATABASE AND THE DATA INSIDE IT, 
    
    YOU NEED TO INSTALL A DATABASE MANAGEMENT SYSTEM, IN OUR CASE IS SQLITE STUDIO https://sqlitestudio.pl/
    UPON COMPLETION OF THE DATABASE MANAGEMENT SYSTEM,
        1 CLICK DATABASE
        2 SELECT ADD DATABASE
        3 A NEW WINDOW WILL BE OPENED, BROWSE IN ORDER TO LOCATE THE bank_investment.db FILE THAT IS WITHIN THIS PROJECT
        4 SELECT THE FILE AND CLICK OK, THEN YOU WILL BE TO SEE ALL TABLES AND DATA WHICH ARE IN OUR bank_investment.db DATABASE
        
        TAKE A LOOK TO SOME PICTURES PROVIDED IN THE ROOT DIRECTORY OF THE PROJECT, THEY WILL GIVE YOU AN INSIGHT OF THE PROJECT
        
    THE database_request.py IS OUR CUSTOMIZED MODULE WHERE WE WRITE REQUESTS AND FUNCTIONS RELATED TO OUR DATABASE
    
    THE  bank_investment.py IS FILE THAT CONTAINS THE MAIN FUNCTION TO START OUR PROGRAM
"""
from tkinter import *
import tkinter as tk

from CTkPieChart import *
import os
import tkinter.messagebox
import customtkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk, Image
from number_entry import IntEntry
import math
import csv
import sqlite3
import matplotlib.pyplot as plt
# Import the datetime class from the datetime
# module so that it can be used in this program.

from datetime import datetime
# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.

# Import a database_request module
from database_request import *
from tkinter.ttk import Treeview,Sizegrip


import re



current_date_and_time = datetime.now()

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
global img1,img2,img3,img4,img5,img6,img8,img9,img10,img11,img12,img13,img14,img15,stock_order_img, bank_img,account_img,client_img
global count
count=0
global image_path
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "icons")
DATABASE_NAME = "bank_investment.db"
STOCK_MARKET_FILE_DATA="dataSetEuronext_Equities.csv"

"""
A common task for many knowledge investissor 
is to analyze the market trend and to invest in the best opportunities.
This application is a simple tool to help you to manage your investment.
The application is divided in 4 main sections:
- Portfolio: to see the evolution of your investment
- Trading History: to see the history of your trading
- Market Analysis: to see the evolution of the market
- Investment: to invest in the best opportunities
It also includes a bank section to manage your bank account:
- Bank: to manage your bank account,to transfer money to another account,to see the balance of your account

"""
def main():
    # Create the main window. In tkinter,
    # a window is also called a frame.
    #customerkinter is a library that provides a set of widgets that are not available in the standard tkinter library.
    # Also provides a set of themes and appearance modes to customize the appearance of the widgets.
    #We create a customtkinter Object in order to call its methods
    app = App()
    app.mainloop()
    
    
    """Database and tables code of creation, You can another Database with a choise name  like 
    Stockexchange.db or traadingbank.db by passing if in create_tables() function on these lines of code
    if create_tables(DATABASE_NAME):
        print("Database creation Success")
    else:
        print("Database creation Failure")
    """  
   
    """The lines of code get data from a csv file and  it into a database table
    stock_data= get_stock_Market_data(STOCK_MARKET_FILE_DATA)
    for data in stock_data:
        result= _stock_data(data)
        if result:
            print("Data ion Success")
        else:
            print("Data ion Failure")
    """
    """
    Those requests tested the _client function
    users_files= os.path.join(os.path.dirname(os.path.realpath(__file__)), "users_files")
    clients=[["France","Musala","Kolwezi Town, Manika street 1","+243 999 876 373","francemusala@gmail.com",datetime.strptime("12-09-2000",'%d-%m-%Y'),users_files+"idenification_doc.pdf"],
             
            ["Joel","Mbikay","Lubumbashi Town, Makomeno street 154","+243 999 876 373","joelmbikay@gmail.com",datetime.strptime("12-08-1999",'%d-%m-%Y'),users_files+"idenification_doc.pdf"],     
            ["Emmanuel","Kasongo","Goma Town, Manika street 53","+243 999 876 373","emmanuelkas@gamil.com",datetime.strptime("12-09-1999",'%d-%m-%Y'),users_files+"idenification_doc.pdf"],
            ["Brigham","Young University-Idaho","Rexburg, Idaho, USA","+1 208 496 1411","brigham@byui.edu",datetime.strptime("20-09-1887",'%d-%m-%Y'),users_files+"ibyu_idaho.pdf"]]
   
    for client in clients:
        
        if _client(client):
            print("Client ion Success")
        else:
            print("Client ion Failure")   
    """
    """
    These requests are written to test the _account function
    accounts= [
       [9438493949323,"investment","Trust Merchant Bank",1000,"USD","BCDCCDKI",datetime.strptime("12-09-2023",'%d-%m-%Y'),1],
       [5000803838423,"saving","United Africa Bank",5000,"USD","UBACDO",datetime.strptime("25-09-2023",'%d-%m-%Y'),2],
       [5000803484543,"investment","United Africa Bank",20000,"USD","UBACCDO",datetime.strptime("30-09-2023",'%d-%m-%Y'),3],
       [5000803598838,"saving","United Africa Bank",50000,"USD","UBACDO",datetime.strptime("25-03-2024",'%d-%m-%Y'),4],
       [8473483764374,"checking","Trade Bank",1000,"USD","TRADCDKI",datetime.strptime("12-09-2023",'%d-%m-%Y'),5],
       [5000803838423,"saving","United Africa Bank",5000,"USD","UBACDO",datetime.strptime("25-09-2023",'%d-%m-%Y'),1],
       [5000808973723,"investment","United Africa Bank",20000,"USD","UBACCDO",datetime.strptime("30-09-2023",'%d-%m-%Y'),2],     
    ]
       
    for account in accounts:
        if _account(account):
            print("Account ion Success")
        else:
            print("Account ion Failure") 
    """
    
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        

        # configure window
        self.title("Bank Investment")
        self.geometry(f"{1180}x{580}")
        self.resizable(False, False)
        
        
        #setup menu
        set_menu(self)
        #self.iconbitmap("icons/emblem-advertisement-dollar.ico")
        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Bank Investment", font=customtkinter.CTkFont(size=25, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
      
        try:
            img1=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "portefeuille.png")),size=(48, 48))
            img2=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "history.png")),size=(48, 48))
            img3=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "market.png")),size=(48, 48))
            img4=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "invest.png")),size=(48, 48))
            img5=customtkinter.CTkImage(Image.open(os.path.join(image_path, "bank.png")))
            img8=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "transfer.png")))
            img9=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "balance.png")))
            img10=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "increase_50px.png")))
            img11=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Blue_Pay-64.webp")),size=(64, 64))
            img12=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Mastercard-64.webp")),size=(64, 64))
            img13=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Paypal-39-64.webp")),size=(64, 64))
            img14=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "Visa-64.webp")),size=(64, 64))
        except FileNotFoundError as not_found_err:
            print(f"Error: cannot open image file because it doesn't exist.")
        except PermissionError as perm_err:
            print(f"Error: cannot read image file because you don't have permission.")
        #img5=customtkinter.CTkImage(dark_image=img4)
        
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame,image=img1,text="Portfolio", fg_color="transparent",font=customtkinter.CTkFont( weight="bold"), command=self.sidebar_button_event,compound="left")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame,image=img4,text="Investment", fg_color="transparent",font=customtkinter.CTkFont(weight="bold"), command=self.sidebar_button_event2,compound="left")
        self.sidebar_button_4.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame,image=img2,text="Trading \n History", fg_color="transparent",font=customtkinter.CTkFont(weight="bold"), command=self.sidebar_button_event,compound="left")
        self.sidebar_button_2.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,image=img3,text="Market \n Analysis", fg_color="transparent",font=customtkinter.CTkFont(weight="bold"), command=self.sidebar_button_event,compound="left")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
        self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # create textbox
        #self.textbox = customtkinter.CTkTextbox(self, width=250)
        #self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=750)
        self.tabview.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew",columnspan=3)
        self.tabview.add("Stock")
        self.tabview.add("Banks")
        self.tabview.add("Companies")
        self.tabview.tab("Stock").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Companies").grid_columnconfigure(0, weight=1)
        
       
       
        index=0
       
        
        def read_data(data):
            """
                This function fills our TreeView widget with data
                Parameters:
                    data: is a compound list that contains our stock market data
                Return:
                    None
            """
            for index, line in enumerate(data):
              
                self.tree.insert('', tk.END, iid = index,text = line[1], values=line[2:],tags=('evenrow',))
        columns = ("Date","Symbol", "Company","Market","Volume","Price","High","Currency")
        
        
        self.scrollable_frame2 = customtkinter.CTkScrollableFrame(self.tabview.tab("Stock"), label_text="Stock Market")
        self.scrollable_frame2.grid(row=0, column=0, padx=(20, 20), pady=(20, 50), sticky="nsew")
        self.scrollable_frame2.grid_columnconfigure(0, weight=1)
        self.tree= Treeview(self.scrollable_frame2, columns=columns,displaycolumns="#all",height=10)
        self.tree.tag_configure('evenrow',background="green")
        self.tree.pack(expand=1,fill='both')
        self.tree.heading('#0', text='Date',anchor=CENTER)
        self.tree.heading('#1', text='Symbol',anchor=CENTER)
        self.tree.heading('#2', text='Company',anchor=CENTER)
        self.tree.heading('#3', text='Market',anchor=CENTER)
        self.tree.heading('#4', text='Volume',anchor=CENTER)
        self.tree.heading('#5', text='Price',anchor=CENTER)
        self.tree.heading('#6', text='High',anchor=CENTER)
        self.tree.heading('#7', text='Currency',anchor=CENTER)
        self.tree.grid(row=0, column=0,padx=20, pady=(10, 10))
        
        #self.style= Style()
        #self.style.configure("Treeview",rowheight=30,bg="green",fg="black",font=("Arial",12))
        read_data(get_all_stock())
        
        # create radiobutton frame
       
        self.radiobutton_frame = customtkinter.CTkFrame(self.tabview.tab("Banks"))
        self.radiobutton_frame.pack(expand=1,fill='both')
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.radiobutton_frame, label_text="Bank")
        self.scrollable_frame.pack(expand=1,fill='both')
        
        
        self.scrollable_frame_switches =[] 
        self.radio_var = tkinter.IntVar(value=0)
        self.label_radio_group = customtkinter.CTkLabel(master=self.scrollable_frame, text="Bank Account:",image=img5,compound="left")
        self.label_radio_group.grid(row=0, column=1, columnspan=1, padx=10, pady=10, sticky="")
        self.scrollable_frame_switches.append(self.label_radio_group)
        banks=get_banks()
        self.input_0 = customtkinter.CTkOptionMenu(self.scrollable_frame, dynamic_resizing=False,
                                                        values=banks,fg_color="#343a40")
        self.input_0.grid(row=1, column=1, pady=5, padx=20, sticky="n")
        self.input_1 = customtkinter.CTkEntry(master=self.scrollable_frame,corner_radius=0,placeholder_text="Account Number/IBAN")
        self.input_1.grid(row=1, column=2, pady=5, padx=20, sticky="n")
        self.input_2 = customtkinter.CTkEntry(master=self.scrollable_frame,corner_radius=0,placeholder_text="BIC Code")
        self.input_2.grid(row=1, column=3, pady=5, padx=20, sticky="n")
        self.radio_button_3 = customtkinter.CTkEntry(master=self.scrollable_frame,corner_radius=0,placeholder_text="Recipient")
        self.radio_button_3.grid(row=2, column=1, pady=5, padx=20, sticky="n")
        self.sidebar_button_2 = customtkinter.CTkButton(self.scrollable_frame,text="Bank Transfer",fg_color="#212529",image=img8, command=self.sidebar_button_event,compound="left")
        self.sidebar_button_2.grid(row=2, column=2, padx=5, pady=5)
        self.sidebar_button_3 = customtkinter.CTkButton(self.scrollable_frame,text="Get balance",fg_color="#212529",image=img9, command=self.open_input_dialog_event)
        self.sidebar_button_3.grid(row=2, column=3, padx=5, pady=10)

        
       
        
        
        # create slider and progressbar frame
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
        self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # create scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Bank Manager")
        self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame_switches = []
        self.options=["Add Stock Order","Add Customer","Add Bank Account","Add Bank"]
        stock_order_img=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "address-book-new.png")),size=(20, 20))
        client_img=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "user-new-3.png")),size=(20, 20))
        account_img=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "kwalletmanager.png")),size=(20, 20))
        bank_img=customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "2830289.png")),size=(20, 20))
        self.icons=[stock_order_img,client_img,account_img,bank_img]
        for i in range(4):
            #switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"{self.options[i]}")
            if i==0:
                param_0=0
                self.button1= customtkinter.CTkButton(master=self.scrollable_frame,text=f"{self.options[i]} ",command=lambda:select_commande(param_0),image=self.icons[i],compound="left")
                self.button1.grid(row=0, column=0, padx=10, pady=(0, 20))
                self.scrollable_frame_switches.append(self.button1)
            elif i==1:
                 param_1=1
                 self.button2= customtkinter.CTkButton(master=self.scrollable_frame,text=f"{self.options[i]} ",command=lambda:select_commande(param_1),image=self.icons[i],compound="left")
                 self.button2.grid(row=1, column=0, padx=10, pady=(0, 20))
                 self.scrollable_frame_switches.append(self.button2)
            elif i==2:
                param_2=2
                self.button3= customtkinter.CTkButton(master=self.scrollable_frame,text=f"{self.options[i]} ",command=lambda:select_commande(param_2),image=self.icons[i],compound="left")
                self.button3.grid(row=2, column=0, padx=10, pady=(0, 20))
                self.scrollable_frame_switches.append(self.button3)
            else:
                param_3=3
                self.button4= customtkinter.CTkButton(master=self.scrollable_frame,text=f"{self.options[i]} ",command=lambda:select_commande(param_3),image=self.icons[i],compound="left")
                self.button4.grid(row=3, column=0, padx=10, pady=(0, 20))
                self.scrollable_frame_switches.append(self.button4)
           

        # create checkbox and switch frame
        self.checkbox_slider_frame = customtkinter.CTkFrame(self)
        self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.button_1 =customtkinter.CTkButton(self.checkbox_slider_frame,text="Bank Transfer",fg_color="transparent",image=img11, command=self.sidebar_button_event,compound="left")
        self.button_1.grid(row=1, column=0, pady=(5, 0), padx=10, sticky="n")
        self.button_2 = customtkinter.CTkButton(self.checkbox_slider_frame,text="Bank Transfer",fg_color="transparent",image=img12, command=self.sidebar_button_event,compound="left")
        self.button_2.grid(row=2, column=0, pady=(5, 0), padx=10, sticky="n")
        self.button_3 = customtkinter.CTkButton(self.checkbox_slider_frame,text="Bank Transfer",fg_color="transparent",image=img13, command=self.sidebar_button_event,compound="left")
        self.button_3.grid(row=1, column=1, pady=5, padx=10, sticky="n")
        self.button_4 = customtkinter.CTkButton(self.checkbox_slider_frame,text="Bank Transfer",fg_color="transparent",image=img14, command=self.sidebar_button_event,compound="left")
        self.button_4.grid(row=2, column=1, pady=5, padx=10, sticky="n")
       

        # set default values
        #self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
        #self.checkbox_3.configure(state="disabled")
        
        self.scrollable_frame_switches[0]
        self.scrollable_frame_switches[3]
        self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        
        
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()
        #self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")
    
        # Bind the format_card_number function to the KeyRelease event of the input_1card widget
        self.input_1.bind("<KeyRelease>", format_card_number)
   

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type account number:", title="Get Balance")
        account_number= dialog.get()
        print(account_number)
        if account_number is None:
            return
        else:
            # Get the balance from the bank
            balance = get_balance(account_number)
            if balance is None:
                tk.messagebox.showerror("Error", "Account number not found.")
                balance=0
            
            # Display the balance to the user
            tk.messagebox.showinfo("Account Balance", f"The balance of account {account_number} is {balance}.")
        
       

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        dialog = customtkinter.CTkInputDialog(text="Account Number:", title="Bank Account")
       
        app = customtkinter.CTk()
        app.geometry("600x320")
        app.title("Portofolio")
        app.resizable(False,False)
        app.grid_columnconfigure(1, weight=1)
        app.grid_columnconfigure((2, 3), weight=0)
        app.grid_rowconfigure((0, 1, 2), weight=1)
        sidebar_frame = customtkinter.CTkFrame(app, width=500, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, rowspan=5,columnspan=3, sticky="nsew")
        sidebar_frame.grid_rowconfigure(5, weight=1)
        account_number=dialog.get_input()
        logo_label = customtkinter.CTkLabel(sidebar_frame, text=f"Portofolio Report", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0,padx=20,columnspan=2, pady=(20, 10))
        balance= get_balance(account_number)
        if balance is None:
            tk.messagebox.showerror("Error", "Account number not found.")
            balance=0
        trades= get_stock_trades(account_number)
       
        if len(trades)==0:
            tk.messagebox.showinfo("Information", "No trades found.")
            app.destroy()
            return
        
        frame=customtkinter.CTkFrame(sidebar_frame)
        frame.grid(row=1, column=0,columnspan=2, padx=20, pady=(20, 0), sticky="nsew")
        logo_label = customtkinter.CTkLabel(frame, text=f"Your Current balance is ${balance}", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        for index,trade in enumerate(trades):
            logo_label = customtkinter.CTkLabel(frame, text=f"{trade[0]} {trade[1]} {trade[2]} {trade[3]} ", font=customtkinter.CTkFont(size=15, weight="bold"),text_color="#0087f2")
            logo_label.grid(row=index+1, column=0, padx=20, pady=(20, 10))
       
      
        app.mainloop()
        
    def sidebar_button_event2(self):
        dialog = customtkinter.CTkInputDialog(text="Account Number:", title="Bank Account")
       
        app = customtkinter.CTk()
        app.geometry("600x320")
        app.title("Investment report")
        app.resizable(False,False)
        app.grid_columnconfigure(1, weight=1)
        app.grid_columnconfigure((2, 3), weight=0)
        app.grid_rowconfigure((0, 1, 2), weight=1)
        sidebar_frame = customtkinter.CTkFrame(app, width=500, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, rowspan=5,columnspan=3, sticky="nsew")
        sidebar_frame.grid_rowconfigure(5, weight=1)
        account_number=dialog.get_input()
        logo_label = customtkinter.CTkLabel(sidebar_frame, text=f"Investment Report", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0,padx=20,columnspan=2, pady=(20, 10))
        balance= get_balance(account_number)
        if balance is None:
            tk.messagebox.showerror("Error", "Account number not found.")
            balance=0
        trades= get_investment_report(account_number)
       
        if len(trades)==0:
            tk.messagebox.showinfo("Information", "No trades found.")
            app.destroy()
            return
        
        frame=customtkinter.CTkFrame(sidebar_frame)
        frame.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="nsew")
        logo_label = customtkinter.CTkLabel(frame, text=f"Your Current balance is ${balance}", font=customtkinter.CTkFont(size=20, weight="bold"))
        logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        for index,trade in enumerate(trades):
            logo_label = customtkinter.CTkLabel(frame, text=f"{trade[0]} {trade[1]} {trade[2]}", font=customtkinter.CTkFont(size=15, weight="bold"),text_color="#1799ff")
            logo_label.grid(row=index+1, column=0, padx=20, pady=(20, 10))
            
        frame2=customtkinter.CTkFrame(sidebar_frame)
        frame2.grid(row=1, column=1, padx=20, pady=(20, 0), sticky="nsew")
        main_button_1 = customtkinter.CTkButton(master=frame2,text="Invest Now",command=commande_0)
        main_button_1.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        main_button_2 = customtkinter.CTkButton(master=frame2,text="Open An Account",command=commande_2)
        main_button_2.grid(row=2, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
        app.mainloop()

def choose_file(label):
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("PDF Files", "*.pdf"), ("All Files", "*.*")]
    )
    if not filepath:
        return
   
    label.delete(0,tk.END)
    label.insert(tk.END, filepath)    
    label.grid(row=4, column=1, padx=20, pady=(20, 10))
        
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        #txt_edit.insert(tk.END, text)


def get_stock_Market_data(filename):
    """Read the contents of a CSV file into a compound
    list and return the list.

    Parameters
        filename: the name of the CSV file to read.
       
    Return: a compound list that contains
        the contents of the CSV file."""
    stock_data=[]
    try:  
         
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row_list in reader:
               
                try:
                 
                    # We choose only needed columns to build a new list
                    
                    new_list=[row_list[9],row_list[0],row_list[2],row_list[3],row_list[11],row_list[6],row_list[5],row_list[4]]
                       
                    stock_data.append(new_list)

                except IndexError as index_err:
                    print(index_err)
                    
            return stock_data
    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {filename}"
                " because it doesn't exist.")
        return stock_data

    except PermissionError as perm_err:
        print(f"Error: cannot read from {filename}"
                " because you don't have permission.")
        return stock_data


# ...
def save_file():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
  
def get_account_balance(account_number, bank_name,sidebar_input_2):
    """Get the balance of the account."""
    # Get the account number from the user
    balance = get_balance(account_number)
    if balance is None:
        tk.messagebox.showerror("Error", "Account number not found.")
        balance=0
   
    
        
    #tk.messagebox.showinfo("Account Balance", f"The balance of account {account_number} is {bank_name}.")
    sidebar_input_2.delete(0,tk.END)
    sidebar_input_2.configure(state="normal")
    sidebar_input_2.insert(0, f'${balance}')
    sidebar_input_2.configure(state="readonly")
    
    
    
    
       
def transfer_money(account_number_from, account_number_to, amount):
    """Transfer money from one account to another."""
    # Debit the account from which the money is transferred
    debit_account(account_number_from, amount)
    # Credit the account to which the money is transferred
    credit_account(account_number_to, amount)
    # Display a message to the user
    tk.messagebox.showinfo("Money Transfer", f"Successfully transferred {amount} from account {account_number_from} to account {account_number_to}.")

def select_commande(id):
    if id==0:
        commande_0()
    elif id==1:
        commande_1()
    elif id==2:
        commande_2()
    elif id==3:
        commande_3()    
def commande_0():
    global picture1
    app = customtkinter.CTk()
    app.geometry("600x320")
    app.title("Add Stock Order")
    app.resizable(False,False)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure((2, 3), weight=0)
    app.grid_rowconfigure((0, 1, 2), weight=1)
    sidebar_frame = customtkinter.CTkFrame(app, width=140, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
    sidebar_frame.grid_rowconfigure(5, weight=1)
    logo_label = customtkinter.CTkLabel(sidebar_frame, text="Bank Account", font=customtkinter.CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    
    banks=get_banks()
    menu_option_0 = customtkinter.CTkOptionMenu(sidebar_frame,dynamic_resizing=False,
                                                        values=banks,fg_color="#343a40")
    #menu_option_0.set("Select Bank")
    menu_option_0.grid(row=1, column=0, padx=20, pady=10)
    sidebar_input_1 = customtkinter.CTkEntry(master=sidebar_frame,corner_radius=0,placeholder_text="Account Number")
    sidebar_input_1.configure(require_redraw=True)
    sidebar_input_1.grid(row=2, column=0, padx=20, pady=10)
    
    sidebar_input_2 =customtkinter.CTkEntry(sidebar_frame,corner_radius=0, placeholder_text="balance will dispay here",state="readonly")
    
    sidebar_input_2.grid(row=3, column=0, padx=20, pady=10)
    

    sidebar_input_3 = customtkinter.CTkButton(sidebar_frame,text="Get balance",command=lambda:get_account_balance(sidebar_input_1.get(),menu_option_0.get(),sidebar_input_2),compound="left")
    sidebar_input_3.grid(row=4, column=0, padx=20, pady=10)
    sidebar_frame2 = customtkinter.CTkFrame(app, width=170, corner_radius=0)
   
    sidebar_frame2.grid(row=0, column=1, rowspan=6, sticky="nsew",columnspan=3)
    sidebar_frame2.grid_rowconfigure(6, weight=1)
    logo_label = customtkinter.CTkLabel(sidebar_frame2, text="Stock Trade", font=customtkinter.CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    trades=["Buy","Sell"]
    securities= ["Stocks","Bonds","BitCoin","Ethereum","BitCoin Cash","Litecoin","Gold","DOT-USD","ADA-USD","XRP-USD","ETH-USD","BTC-USD","LTC-USD","BCH-USD","XLM-USD","USDT-USD","DOGE-USD","UNI3-USD","LINK-USD","AAVE-USD","SOL1-USD","ATOM1-USD","FIL3-USD","TRX-USD","XMR-USD","EOS-USD","XTZ-USD","MKR-USD","BSV-USD","CRO-USD","LUNA1-USD","NEO-USD","LEO1-USD","HT-USD","COMP-USD","DASH-USD","VET-USD","ETC-USD","THETA-USD","MIOTA-USD","AVAX-USD","FTT-USD","BTT1-USD","ALGO-USD","HBAR-USD","ZEC-USD","WAVES-USD","DCR-USD","HOT-USD","CHZ-USD","ENJ-USD","MANA-USD","ZIL-USD","SUSHI-USD","YFI-USD","ICP1-USD","GRT2-USD","SNX-USD","STX-USD","AMP-USD","QNT-USD","REN-USD","BAT-USD","CRV-USD","OKB-USD","CEL-USD","KSM-USD","NANO-USD","OMG-USD","FLOW-USD","RSR-USD","ZRX-USD","SC-USD","HNT-USD","ONE2-USD","MATIC-USD","ANKR-USD","LRC-USD","KAVA-USD","ICX-USD","DGB-USD","CVC-USD","RLC-USD","BNT-USD","BAL-USD","SKL-USD","SRM-USD","GNO-USD","RLY-USD","LPT-USD","BTS-USD","STMX-USD","MLN-USD","OXT-USD","BAND-USD","RLC-USD","BNT-USD","BAL-USD","SKL-USD","SRM-USD","GNO-USD","RLY-USD","LPT-USD","BTS-USD","STMX-USD","MLN-USD","OXT-USD","BAND-USD","RLC-USD","BNT-USD"]
    
    menu_option_3 = customtkinter.CTkOptionMenu(sidebar_frame2,dynamic_resizing=False,
                                                        values=trades,fg_color="#343a40")
    #menu_option_3.("Select a Transaction")
    menu_option_4 = customtkinter.CTkOptionMenu(sidebar_frame2,dynamic_resizing=False,values=securities,fg_color="#343a40")
    
    stock_symbols=get_stock_symbols()
    def optionmenu_callback(choice):
        
        values=get_stock_from_symbol(choice)
        
        logo_label = customtkinter.CTkLabel(sidebar_frame2, text=f"Company: {values[1]}", font=customtkinter.CTkFont(size=15, weight="bold",underline=True,slant="italic"),text_color="#1e88e5")
        logo_label.grid(row=2, column=1)
        
        logo_label = customtkinter.CTkLabel(sidebar_frame2, text=f"Market: {values[2]}", font=customtkinter.CTkFont(size=15, weight="normal"))
        logo_label.grid(row=3, column=1)
        logo_label = customtkinter.CTkLabel(sidebar_frame2, text=f"Date:{values[3]}", font=customtkinter.CTkFont(size=15, weight="normal"))
        logo_label.grid(row=4, column=1)
        logo_label = customtkinter.CTkLabel(sidebar_frame2, text=f"Price {values[4]} {values[6]}", font=customtkinter.CTkFont(size=15, weight="normal"))
        logo_label.grid(row=5, column=1)     
        logo_label = customtkinter.CTkLabel(sidebar_frame2, text=f"High {values[5]} {values[6]}", font=customtkinter.CTkFont(size=15, weight="normal"))
        logo_label.grid(row=6, column=1)  
           
                
                
        
    stock_symbols_option=customtkinter.CTkOptionMenu(sidebar_frame2,dynamic_resizing=False,
                                                        values=stock_symbols,fg_color="#343a40",command=optionmenu_callback)
    stock_symbols_option.grid(row=1,column=1, padx=20, pady=10)
    
    
    #menu_option_4.set("Select a Financial Securities")                                                 
    
    #menu_option_3.set("Select a Transaction")
    menu_option_3.grid(row=1, column=0, padx=20, pady=10)
    menu_option_4.grid(row=2, column=0, padx=20, pady=10)
    sidebar_input_4 = customtkinter.CTkEntry(master=sidebar_frame2,corner_radius=0,placeholder_text="Quantity")
    sidebar_input_4.configure(require_redraw=True)
    sidebar_input_4.grid(row=3, column=0, padx=20, pady=10)
    sidebar_input_5 =  customtkinter.CTkEntry(master=sidebar_frame2,corner_radius=0,placeholder_text="Price per Share")
    sidebar_input_5.configure(require_redraw=True)
    sidebar_input_5.grid(row=4, column=0, padx=20, pady=10)
    stock_list=[]
    
    sidebar_button_6 = customtkinter.CTkButton(sidebar_frame2,text="Apply",command=lambda:apply_stock([menu_option_0.get(),menu_option_3.get(),menu_option_4.get(),sidebar_input_4.get(),sidebar_input_5.get(),sidebar_input_1.get(),stock_symbols_option.get()]))
    sidebar_button_6.grid(row=5, column=0, padx=20, pady=10)
    
    
    app.mainloop()

def apply_stock(stock_trade):
   
    bank_name=stock_trade[0]
    trade=stock_trade[1]
    financial_security=stock_trade[2]
    quantity=int(stock_trade[3])
    price_per_share=float(stock_trade[4])
    account_number=int(stock_trade[5])
    stock_symbol=stock_trade[6]
    
    
    if trade == "Buy":
        result=buy_stock(account_number,stock_symbol,quantity,price_per_share)
        if result:
            
            stock_trade=[current_date_and_time.strftime("%a %b %d %X %Y"),financial_security,bank_name,"NASDAQ",quantity,price_per_share,"USD"]
            
            total_cost = quantity * price_per_share
            #Insert Data in the Investment table
            insert_investment([financial_security,total_cost,current_date_and_time.strftime("%a %b %d %X %Y"),account_number])
            #Insert Data in the Transaction table
            #The transaction_type [withdrawal or deposit] is related to the financial securities
            insert_transaction([current_date_and_time.strftime("%a %b %d %X %Y"),"deposit",total_cost,account_number])
            
            Stock_ID= int(get_ID_stock(stock_symbol))
            Stock_Price=float(get_stock_price(stock_symbol))
            average_price= (price_per_share+Stock_Price)/2
            UnrealizedLossGain=price_per_share-Stock_Price
            
            #Insert PortoFolio
            insert_stock_portfolio([account_number, Stock_ID,quantity, average_price,UnrealizedLossGain])
            #insert_stock_trade([account_number,Stock_ID,"Buy",current_date_and_time.strftime("%a %b %d %X %Y"),quantity,price_per_share])
            track_stock("stock_market.csv",stock_trade)
            tk.messagebox.showinfo("Stock Trade", f"Successfully bought {quantity} of {financial_security} at {price_per_share} per share.")
        else:
            tk.messagebox.showerror("Stock Trade", f"Failed to buy {quantity} of {financial_security} at {price_per_share} per share.")

    elif trade == "Sell":
        result=sell_stock(account_number,stock_symbol,quantity,price_per_share)
        if result:
           
            total_cost = quantity * price_per_share
            stock_trade=[current_date_and_time.strftime("%a %b %d %X %Y"),financial_security,bank_name,"NASDAQ",quantity,price_per_share,"USD"]
            
             #Insert Data in the Investment table
            insert_investment([financial_security,total_cost,current_date_and_time.strftime("%a %b %d %X %Y"),account_number])
            #Insert Data in the Transaction table
            #The transaction_type [withdrawal or deposit] is related to the financial securities
            insert_transaction([current_date_and_time.strftime("%a %b %d %X %Y"),"withdrawal",total_cost,account_number])
            Stock_ID= int(get_ID_stock(stock_symbol))
            Stock_Price=float(get_stock_price(stock_symbol))
            average_price= (price_per_share+Stock_Price)/2
            UnrealizedLossGain=price_per_share-Stock_Price
            
            #Insert PortoFolio
            insert_stock_portfolio([account_number, Stock_ID,quantity, average_price,UnrealizedLossGain])
            
            #insert_stock_trade([account_number,Stock_ID,"Sell",current_date_and_time.strftime("%a %b %d %X %Y"),quantity,price_per_share])
            track_stock("stock_market.csv",stock_trade)
            tk.messagebox.showinfo("Stock Trade", f"Successfully sold {quantity} of {financial_security} at {price_per_share} per share.")
        else:
            tk.messagebox.showerror("Stock Trade", f"Failed to sell {quantity} of {financial_security} at {price_per_share} per share.")
    else:
        tk.messagebox.showerror("Stock Trade", f"Invalid trade type.")
def commande_1():
    
    app = customtkinter.CTk()
    app.geometry("600x320")
    app.title("Open A Bank Account")
    app.resizable(False,False)
    app.grid_columnconfigure(1, weight=1)
    app.grid_columnconfigure((2, 3), weight=0)
    app.grid_rowconfigure((0, 1, 2), weight=1)
    sidebar_frame = customtkinter.CTkFrame(app, width=140, corner_radius=0)
    sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
    sidebar_frame.grid_rowconfigure(6, weight=1)
    logo_label = customtkinter.CTkLabel(sidebar_frame, text="Bank Account Data", font=customtkinter.CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    
    banks=get_banks()
    banks_option = customtkinter.CTkOptionMenu(sidebar_frame,dynamic_resizing=False,
                                                        values=banks,fg_color="#343a40")
    #menu_option_0.set("Select Bank")
    banks_option.grid(row=1, column=0, padx=20, pady=10)
    bank_account = customtkinter.CTkEntry(master=sidebar_frame,corner_radius=0,placeholder_text="Account Number")
    bank_account.configure(require_redraw=True)
    bank_account.grid(row=2, column=0, padx=20, pady=10)
    
    balance =customtkinter.CTkEntry(sidebar_frame,corner_radius=0, placeholder_text="balance") 
    balance.configure(require_redraw=True) 
    balance.grid(row=3, column=0, padx=20, pady=10)
    
    currency=["USD","EUR","NOK","GBP","FC","YEN"]
    currency_option = customtkinter.CTkOptionMenu(sidebar_frame,dynamic_resizing=False,
                                                        values=currency,fg_color="#343a40")
    #menu_option_0.set("Select Bank")
    currency_option.grid(row=4, column=0, padx=20, pady=10)
    
    account_type=["saving","checking","investment"]
    account_option = customtkinter.CTkOptionMenu(sidebar_frame,dynamic_resizing=False,
                                                        values=account_type,fg_color="#343a40")
    #menu_option_0.set("Select Bank")
    account_option.grid(row=5, column=0, padx=20, pady=10)
    sidebar_frame2 = customtkinter.CTkFrame(app, width=170, corner_radius=0)
   
    sidebar_frame2.grid(row=0, column=1, rowspan=6, sticky="nsew",columnspan=3)
    sidebar_frame2.grid_rowconfigure(6, weight=1)
    logo_label = customtkinter.CTkLabel(sidebar_frame2, text="Customer Data", font=customtkinter.CTkFont(size=20, weight="bold"))
    logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
                 
            
    first_name = customtkinter.CTkEntry(master=sidebar_frame2,corner_radius=0,placeholder_text="Firstname")
    first_name.configure(require_redraw=True)
    first_name.grid(row=1, column=0, padx=20, pady=10)
    last_name =  customtkinter.CTkEntry(master=sidebar_frame2,corner_radius=0,placeholder_text="Lastname")
    last_name.configure(require_redraw=True)
    last_name.grid(row=1, column=1, padx=20, pady=10)
          
    phone = customtkinter.CTkEntry(master=sidebar_frame2,corner_radius=0,placeholder_text="Phone Number")
    phone.configure(require_redraw=True)
    phone.grid(row=2, column=0, padx=20, pady=10)
    email =  customtkinter.CTkEntry(master=sidebar_frame2,corner_radius=0,placeholder_text="Email")
    email.configure(require_redraw=True)
    email.grid(row=2, column=1, padx=20, pady=10)
    
    address = customtkinter.CTkEntry(master=sidebar_frame2,corner_radius=0,placeholder_text="Address")
    address.configure(require_redraw=True)
    address.grid(row=3, column=0, padx=20, pady=10,columnspan=1)
    
    label_file = customtkinter.CTkEntry(master=sidebar_frame2,corner_radius=0)
   
    
    file = customtkinter.CTkButton(sidebar_frame2,text="Select a file",command=lambda:choose_file(label_file))
    file.grid(row=4, column=0, padx=20, pady=10)
    
    sidebar_button_6 = customtkinter.CTkButton(sidebar_frame2,text="Apply",command=lambda:create_account([banks_option.get(),bank_account.get(),balance.get()
   ,currency_option.get(),account_option.ge()],[first_name.get(),last_name.get(),phone.get(),email.get(),address.get(),label_file.get()]))
    sidebar_button_6.grid(row=5, column=0, padx=20, pady=10)
    
    
    app.mainloop()
def create_account(user,bank_account):
    print("hello")

def commande_2():
   commande_1()
  
def commande_3():
    app = customtkinter.CTk()
    app.geometry("600x500")
    app.title("Add Bank")
    app.mainloop()    
    
def track_stock(filename,data):
    """Write the stock market data to a CSV file.
        Parameters:
            filename: the name of the CSV file to write to.
            data: the stock market data to write to the CSV file.
        Return:boolean
    """
           
    try:  
               
        with open(filename, "at") as csv_file:
            writer = csv.writer(csv_file)
            
            writer.writerow(data)
            return True
                   
    except FileNotFoundError as not_found_err:
        print(f"Error: cannot open {filename}"
                            " because it doesn't exist.")
        return False

    except PermissionError as perm_err:
        print(f"Error: cannot read from {filename}"
                        " because you don't have permission.")
        return False
    
def format_card_number(event):
    """This function is used to format the Bank Account Number
        in other word the function sets the or format the widget input
        Parameter event: the event related to the current widget, an Entry field in our case
        Return: None
    """
    widget = event.widget
    value = widget.get()
    
    # Utilisation d'une expression régulière pour extraire les chiffres du numéro de carte
    card_number = re.sub(r'\D', '', value)
    
    # Formatage du numéro de carte bancaire
    formatted_number = ""
    for i, digit in enumerate(card_number):
        if i > 0 and i % 4 == 0:
            formatted_number += " "
        formatted_number += digit
    
    # Mise à jour du contenu de l'Entry widget
    widget.delete(0, tk.END)
    widget.insert(0, formatted_number)

def get_banks():
    banks=[
        "Trust Merchant Bank",
        "Equity BCDC",
        "RawBank",
        "FirstBank",
        "United Africa Bank",
        "Trade Bank"
    ]
    return banks
def set_menu(window):
    menu_bar = Menu(window)
    window.config(menu=menu_bar)
    # Add the Menu bar to an existing window,
    # a window is also called a frame.
    
    menu_file = Menu(menu_bar, tearoff=0)
    
    menu_file.add_command(label="New",underline=0, accelerator="CTRL+N", command=open_file)
    menu_file.add_command(label="Open",underline=0, accelerator="CTRL+O", command=open_file)
    menu_file.add_command(label="Save",underline=0, accelerator="CTRL+S", command=open_file)
    menu_file.add_separator()
    menu_file.add_command(label="Exit",underline=0, accelerator="CTRL+Q", command=window.quit)
    menu_bar.add_cascade(label="File", menu=menu_file)

    menu_edit = Menu(menu_bar, tearoff=0)
    menu_edit.add_command(label="Undo",underline=0, accelerator="CTRL+Z", command=open_file)
    menu_edit.add_separator()
    menu_edit.add_command(label="Copy",underline=0, accelerator="CTRL+C", command=open_file)
    menu_edit.add_command(label="Cut",underline=0, accelerator="CTRL+X", command=open_file)
    menu_edit.add_command(label="Paste",underline=0, accelerator="CTRL+V", command=open_file)
    menu_bar.add_cascade(label="Edit", menu=menu_edit)

    menu_help = Menu(menu_bar, tearoff=0)
    menu_help.add_command(label="About", command=open_file)
    menu_bar.add_cascade(label="Help", menu=menu_help)


# If this file was executed like this:
# > python bankInvestment.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.

if __name__ == "__main__":
   main()
