def calc_dollars():
    piggyBank = {
        "pennies": 342,
        "nickels": 9,
        "dimes": 32,
        "quarter": 15
    }
    pennies_amount_in_dollars = piggyBank["pennies"] * .01 
    nickels_amount_in_dollars = piggyBank["nickels"] * .05 
    dimes_amount_in_dollars = piggyBank["dimes"] * .1 
    quarters_amount_in_dollars = piggyBank["pennies"] * .25 

    dollarAmount = pennies_amount_in_dollars + nickels_amount_in_dollars + dimes_amount_in_dollars + quarters_amount_in_dollars
    print(dollarAmount)

calc_dollars()


# dollarAmount