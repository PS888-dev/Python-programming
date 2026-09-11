def getRate(total):
    rates = (0.10,0.075,0.05,0.025,0.0)
    totalSales = (20000.0, 10000.0, 5000.0,1000,1.0)
    for n in range(len(totalSales)):
        if total > totalSales[n]:
            return(rates[n])

def inputSales(sales):
    for n in range(1,8):
        sale = float(input(f"Enter sale day {n} : "))
        sales += (sale,)
    return sales

def report(totalSale, rate, commision):
    print(f"\nTotal sale : {totalSale:,.2f}")
    print(f"Commision rate : {rate*100:.2f}%")
    print(f"Total commision : {commision:,.2f}")

sales = ()
sales = inputSales(sales)
totalSale = sum(sales)
rate = getRate(totalSale)
commision = totalSale * rate

report(totalSale, rate ,commision)