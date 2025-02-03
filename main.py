# *****************************************************************************
# Declare constant representing increase of 3%
RATE = 1.03

def main():
    # Declare variable for current cost
    total = 8000.0

    # Print welcome message
    print("This program will display rising tuition costs over the next five y"
    "ears.\n")
    print("Current full-time tuition is $8000.00 per semester. It will increas"
    "e by 3% per year.")

    # Loop to display the next five years of costs
    for count in range(1, 6):
        if count == 0:
            print("Next year: $", str(format(total * RATE, ".2f")), sep = "")
        else:
            print("In ", str(count), " years: $", str(format(total * RATE, ".2"
            "f")), sep = "")
        total = total * RATE
    
    # Print goodbye message
    print("\nMake sure to take this into account!")
main()