from datetime import date

def add_product(stock):
    today = date.today().isoformat()
    day = input(f"Input date (YYYY-MM-DD, Enter = {today}) : ") or today
    name = input("Input product name : ")
    try:
        price = float(input("Input product price : "))
        qty = int(input("Input product quantity : "))
    except ValueError:
        print("Price and quantity must be numbers.\n")
        return

    with open(stock, "a", encoding="UTF_8") as f:
        f.write("\n" + f"{day},{name},{price},{qty}")
    print(f"Saved: {name} x {qty} = {price * qty:.2f} baht on {day}\n")


def show_product(stock):
    try:
        qty_sum = {}
        price_of = {}
        with open(stock, "r", encoding="UTF_8") as f:
            for row in f:
                parts = row.strip().split(",")
                if len(parts) != 4:
                    continue
                day, name, price, qty = parts
                key = (day, name)
                qty_sum[key] = qty_sum.get(key, 0) + int(qty)
                price_of[key] = float(price)

        line = "=" * 78
        print(f"{line}\n|{'Current Products':^76}|")
        print(f"{line}\n| {'Date':<10} | {'Name':<20} | {'Price per piece':>15} | {'Qty':>6} | {'Total price':>11} |\n{line}")
        for (day, name), qty in sorted(qty_sum.items()):
            price = price_of[(day, name)]
            print(f"| {day:<10} | {name:<20} | {price:>15.2f} | {qty:>6} | {price * qty:>11.2f} |")
        print(line + "\n")
    except FileNotFoundError:
        print("No product data found. Please input product first.\n")


def Sales(stock):
    pass


def Daily_Sales(stock):
    pass


def report_sales(stock):
    pass