# Christian Griessel
# Module 4 Lab for CIS 129
# Calculates employee and store bonuses based on monthly sales at a hypothetical buisiness

def main():
    monthly_sales = getSales("How much sales this month?: ")
    salesIncrease = getIncrease("What percent was the increase?: ")
    storeAmount = calcStoreBonus(monthly_sales)
    empAmount = calcEmpBonus(salesIncrease)


    calcStoreBonus(monthly_sales)
    calcEmpBonus(empAmount)
    printBonus(storeAmount, empAmount)

def getSales(prompt):
    sales =  float(input(prompt))
    return sales

def getIncrease(prompt):
    sales_increase = float(input(prompt))
    sales_increase = sales_increase / 100
    return sales_increase

def calcStoreBonus(monthlySales):
    if monthlySales >= 110_000:
        storeAmount = 6000
    elif monthlySales >= 100_000:
        storeAmount = 5000
    elif monthlySales >= 90_000:
        storeAmount = 4000
    elif monthlySales >= 80_000:
        storeAmount = 3000
    else:
        storeAmount = 0
    return storeAmount

def calcEmpBonus(salesIncrease):
    if salesIncrease >= .05:
        empAmount = 75
    elif salesIncrease >= .04:
        empAmount = 50
    elif salesIncrease >= .03:
        empAmount = 40
    else:
        empAmount = 0
    return empAmount

def printBonus(storeAmount, empAmount):
    print("The store bonus amount is $",storeAmount)
    print("The employee bonus amount is $",empAmount)
    if (storeAmount == 6000) and (empAmount == 75):
        print("Congrats! You have reached the highest bonus amounts possible! ")

main()