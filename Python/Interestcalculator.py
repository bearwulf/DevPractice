###########################################
# COMPUOUND INTEREST CALUCLATOR BECAUSE FUCK THAT FUCKING GUY AND HIS CHEAP ASS FUCKING EXAMPLES
# Zak Seipel
#
#
# V 1
# Use While to loop over a set period of time to determine the compuound interest over time
#
#
##########################################
# Compund interest is calulated by taking the initial principle
# A = P(1+(r/t)^nt
# A = Final amount
# P = Principle
# r = interest rate
# n = number of times interest is applied
# t = number of periods elapsed
############################################
# Variable Declaration and aqusition
############################################
initial_principle = float(input("Enter the initial investment: "))

interest_rate = float(input("Enter the interest Rate in decimalized percentage: "))

period_rate = input(
    "Select one of the following periodicity's \nYearly \nMonthly \nDaily \nHourly \nEnter the periodicity: ")

period_quantity = float(input("Enter the number of periods to calculate as a whole intiger > 0: "))

#print("Initial Investment: ", initial_principle)
#print("Interest Rate:", interest_rate)
#print("Periodicity:", period_rate)
#print("Number of Periods", period_quantity)

###########################################
# Initial Calculations
###########################################
periodicity = 0
# Determining periodicity based on string input
if period_rate == "Yearly":
    periodicity = 1
elif period_rate == "Monthly":
    periodicity = 12
elif period_rate == "Daily":
    periodicity = 365
elif period_rate == "Hourly":
    periodicity = 8760
else:
    print("Hey fucktwat get your shit together and do this right now. I am not going to fuck around. EXITING")
    # Exit if periodicity is incorrect to be a dick
    exit(0)
print("Periodicity: ", periodicity)

#############################################
# Calculating total interest for a given time
#############################################


#############################################
# Loop to show change over time
#############################################
#period_quantity is the x value for the loop (number of loops
counter = 0
while counter <= period_quantity:
    total = (initial_principle * (1 + (interest_rate / periodicity)) ** (periodicity * counter))
    print("The total compound interest over", counter, "with a periodictiy of", period_rate, "is", total)
    counter = counter + 1