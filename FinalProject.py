#!/usr/bin/env python
# coding: utf-8

# In[1]:


from program_gui import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QWidget
import pandas as pd


def signals(self):
    self.B_Cal.clicked.connect(self.calc)  # Connect buttonCalc clicked signal to the calc function
    self.B_Cal.clicked.connect(self.plot_data)
    
def calc(self):  # Do the calculation
    Cost1 = int(self.L_Cost1.text())
    Cost2 = int(self.L_Cost2.text())
    Year1 = int(self.L_Year1.text())
    Year2 = int(self.L_Year2.text())
    AgeUser = int(self.L_AgeUser.text())
    Down = int(self.L_Down.text())
    CreditScore = int(self.L_CreditScore.text())
    LoanPer = int(self.L_LoanPer.text())

    
    
        ### Creating a formula for monthly payments for Car 1
    interest = 0

    monthly_1 = (Cost1 - Down)/LoanPer

    if LoanPer <= 36:
        interest = 3
    elif 48 <= LoanPer < 36:
        interest = 2.5
    else:
        interest = 2

    if CreditScore <= 600:
        interest = interest * 2
    elif 650 < CreditScore <= 700:
        interest = interest * 1.5
    elif 700 < CreditScore <= 750:
        interest = interest * 1.25
    elif CreditScore <750:
        interest = interest 

    monthly_1 = (monthly_1 * ((interest * 0.01)/12)) + monthly_1 
    monthly_1 = round(monthly_1,2)



    ### Creating a formula for monthly payments for Car 2

    monthly_2 = (Cost2 - Down)/LoanPer

    if LoanPer <= 36:
        interest = 3
    elif 48 <= LoanPer < 36:
        interest = 2.5
    else:
        interest = 2

    if CreditScore <= 600:
        interest = interest * 2
    elif 650 < CreditScore <= 700:
        interest = interest * 1.5
    elif 700 < CreditScore <= 750:
        interest = interest * 1.25
    elif CreditScore <750:
        interest = interest 

    monthly_2 = (monthly_2 * ((interest * 0.01)/12)) + monthly_2 
    monthly_2 = round(monthly_2,2)


    ### Insurance quote for Car 1

    quote_1 = 100

    if 29> AgeUser >= 25:
        quote_1 = 100
    elif AgeUser >= 30:
        quote_1 = 50
    else:
        quote_1 = quote_1 * 1.5
    if Cost1 < 15000:
        quote_1 = 1.25 * quote_1
    elif Cost1 >= 15000:
        quote_1 = 1.5 * quote_1
    else:
        quote_1 = quote_1
    if Year1 <= 2012:
        quote_1 = quote_1
    else: 
        quote_1 = 2 * quote_1
    if CreditScore >= 700:
        quote_1 = quote_1
    else:
        quote_1 = quote_1 * 1.25

    quote_1 = round(quote_1,2)


    ### Insurance quote for Car 2

    quote_2 = 100

    if 29> AgeUser >= 25:
        quote_2 = 100
    elif AgeUser >= 30:
        quote_2 = 50
    else:
        quote_2 = quote_2 * 1.5
    if Cost2 < 15000:
        quote_2 = 1.25 * quote_2
    elif Cost2 >= 15000:
        quote_2 = 1.5 * quote_2
    else:
        quote_2 = quote_2
    if Year2 <= 2012:
        quote_2 = quote_2
    else: 
        quote_2 = 2 * quote_2
    if CreditScore >= 700:
        quote_2 = quote_2
    else:
        quote_2 = quote_2 * 1.25

    quote_2 = round(quote_2,2)


    ### Depreciation 

    time = [0,1,2,3,4,5,6,7,8,9,10]
    years = [2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031]
    future = []
    future_2 = []

    fig = plt.figure(figsize=(8,5), dpi=90)
    ### Depreciation of first car

    if Year1 < 2021:
        for i in time:
            price = Cost1
            price = price * 0.85**(i)
            price = round(price,2)
            future.append(price)

        plt.plot(years,future,color="red", linewidth=2, linestyle="--", label = 'Car 1')
        plt.xlabel('Years of Ownership')
        plt.ylabel('Price')
    else:
        for i in time:
            price = Cost1
            price = price * (0.90**i)
            price = round(price,2)
            future.append(price)
        plt.plot(years,future,color="red", linewidth=2,linestyle="--", label = 'Car 1')
        plt.xlabel('Years of Ownership')
        plt.ylabel('Price')



    ### Depreciation of second car
    if Year2 < 2021:
        for i in time:
            price = Cost2
            price = price * 0.85**(i)
            price = round(price,2)
            future_2.append(price)

        plt.plot(years,future_2,color="blue", linewidth=2, label = 'Car 2')
    else:
        for i in time:
            price = Cost2
            price = price * (0.90**i)
            price = round(price,2)
            future_2.append(price)
        plt.plot(years,future_2,color="blue", linewidth=2, label = 'Car 2')

    plt.legend(loc='upper right')

    fees = 300
    taxes_1 = Cost1 * 0.04
    taxes_2 = Cost2 * 0.04

    FVM1 = monthly_1 * (1.05)**10
    FVM2 = monthly_2 * (1.05)**10
    FVI1 = quote_1 * (1.05)**10
    FVI2 = quote_2 * (1.05)**10

    Total1 = Cost1 + taxes_1 + fees
    Total2 = Cost2 + taxes_2 + fees

    ownership1 = (FVM1 * LoanPer) + (FVI1 * 12 * 10) + fees
    ownership1 = round(ownership1,2)
    ownership2 = (FVM2 * LoanPer) + (FVI2 * 12 * 10) + fees
    ownership2 = round(ownership2,2)

    Budget1 = monthly_1 + quote_1
    Budget2 = monthly_2 + quote_2

    
    
    
    
    
    self.C1c.setText(str(Total1))
    self.C2c.setText(str(Total2))
    self.C1m.setText(str(monthly_1))
    self.C2m.setText(str(monthly_2))
    self.C1i.setText(str(quote_1))
    self.C2i.setText(str(quote_2))
    self.C1t.setText(str(ownership1))
    self.C2t.setText(str(ownership2))
    
    ##The Three if statments for the three different options (Car 1, Car2, Compare)##
    #if self.CB_Car1.isChecked():
        
    #if self.CB_Car2.isChecked():
        
    #if self.CB_Compare.isChecked():
    
def plot_data(self):
    
    #Initializing Variables
    Cost1 = int(self.L_Cost1.text())
    Cost2 = int(self.L_Cost2.text())
    Year1 = int(self.L_Year1.text())
    Year2 = int(self.L_Year2.text())
    AgeUser = int(self.L_AgeUser.text())
    Down = int(self.L_Down.text())
    CreditScore = int(self.L_CreditScore.text())
    LoanPer = int(self.L_LoanPer.text())
    
    #Clear Plot
    self.MplWidget.canvas.ax.cla()
    
### Depreciation 
    time = [0,1,2,3,4,5,6,7,8,9,10]
    years = [2021,2022,2023,2024,2025,2026,2027,2028,2029,2030,2031]
    future = []
    future_2 = []

    fig = plt.figure(figsize=(8,5), dpi=90)
    
    ### Depreciation of first car
    if Year1 < 2021:
        for i in time:
            price = Cost1
            price = price * 0.85**(i)
            price = round(price,2)
            future.append(price)

        self.MplWidget.canvas.ax.plot(years,future,color="red", linewidth=2, linestyle="--", label = 'Car 1')
    else:
        for i in time:
            price = Cost1
            price = price * (0.90**i)
            price = round(price,2)
            future.append(price)
        self.MplWidget.canvas.ax.plot(years,future,color="red", linewidth=2,linestyle="--", label = 'Car 1')



    ### Depreciation of second car
    if Year2 < 2021:
        for i in time:
            price = Cost2
            price = price * 0.85**(i)
            price = round(price,2)
            future_2.append(price)

        self.MplWidget.canvas.ax.plot(years,future_2,color="blue", linewidth=2, label = 'Car 2')
    else:
        for i in time:
            price = Cost2
            price = price * (0.90**i)
            price = round(price,2)
            future_2.append(price)
        self.MplWidget.canvas.ax.plot(years,future_2,color="blue", linewidth=2, label = 'Car 2')

    self.MplWidget.canvas.ax.legend(loc='upper right')
    self.MplWidget.canvas.ax.set_title('Depreciation (yyyy vs $)')
    self.MplWidget.canvas.draw()
    
Ui_Dialog.signals = signals  # Add new attributes to Ui_MainWindow
Ui_Dialog.calc = calc
Ui_Dialog.plot_data = plot_data


if __name__ == "__main__":  # A library or a stand-alone program
    import sys
    app = QtWidgets.QApplication(sys.argv)  # Must create a QApplication object
                                            # sys.argv allows passing parameters in command line
    MainWindow = QtWidgets.QMainWindow()  # Create a main window instance.
    ui = Ui_Dialog()  # Create a Ui_MainWindow instance
    ui.setupUi(MainWindow)  # Add widgets to the main window
    ui.signals()  # Connect signals with the appropriate functions
    MainWindow.show()  # Show the main window
    sys.exit(app.exec_())  # If a termination signal is captured, exit the program.


# In[ ]:





# In[ ]:




