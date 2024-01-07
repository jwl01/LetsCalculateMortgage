# %%
#A Simple Mortgage Calculator for Monthly Payments
# I will be using  30-year fixed rates from myFICO as of January 04, 2024 in Minnesota.

# %%
#Loan amount = ln_amt, loan duration = ln_dur, monthly payments = mthlypmts
try:
    ln_amt = float(input("Please enter loan amount:"))
    ln_dur = float(input("Please enter loan duration (in years):"))
    FICO = float(input("Please enter your FICO score here:"))
except ValueError:
    print("This input is invalid. Please try again.")
except ZeroDivisionError:
    print("There seems to be an error. Please try again.")

def mthlypmts():
    n = ln_dur * 12 #Number of monthly payments over duration of the loan.
    if 620 <= FICO <= 639:
        r = 0.0814 #r refers to the fixed rates 
    elif 640 <= FICO <= 659:
        r = 0.07584
    elif 660 <= FICO <= 679:
        r = 0.07147
    elif 680 <= FICO <= 699:
        r = 0.06929
    elif 700 <= FICO <= 759:
        r = 0.06749
    elif 760 <= FICO <= 850:
        r = 0.06523
    mpmt = ln_amt*(((r/12)*((1+r/12)**n))/(((1+r/12)**n)-1))
    return mpmt

#Trying out the calculator.
#I was researching houses on Zillow for fun and selected a house that I liked. I will be using the 20% of the price as the principal loan amount. 
#I will use the average FICO score in the US: 718.
#The loan duration is 30 years.

print(mthlypmts())


