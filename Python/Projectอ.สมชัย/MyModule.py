from datetime import date

def add_product(stock):
    print("Enter data product.")
    today = date.today().isoformat()
    day = input(f"Input date (YYYY-MM-DD, Enter = {today}) : ").strip() or today
    prod_name = input("Input product name : ")
    prod_price = input("Input product price : ")
    prod_qty = input("Input product quantity : ")
    
    try:
        float(prod_price)
        int(prod_qty)
    except ValueError:
        print("Price and quantity must be numbers.\n")
        return
    
    try:
        with open(stock, "a", encoding="UTF_8") as fout:
            fout.write(day + "," + prod_name + "," + prod_price + "," + prod_qty + "\n")
    except FileNotFoundError:
        print(f"Error: Cannot save to '{stock}'. Please check the file path.")
    else:
        print("Save Data Product already.\n")

        total_now = float(prod_price) * int(prod_qty)
        print("-" * 40)
        print(f"Added on {day}")
        print(f"Product  : {prod_name}")
        print(f"Quantity : {int(prod_qty)}")
        print(f"Price    : {float(prod_price):.2f} baht per piece")
        print(f"Total    : {total_now:.2f} baht")
        print("-" * 40 + "\n")

        # รวมสินค้าชื่อเดียวกันของวันนั้น
        items = {}
        with open(stock, "r", encoding="UTF_8") as fin:
            for row in fin:
                parts = row.strip().split(",")
                if len(parts) != 4:
                    continue
                d, name, price, qty = parts
                if d != day:
                    continue
                price = float(price)
                qty = int(qty)
                if name in items:
                    items[name]["qty"] += qty
                    items[name]["total"] += price * qty
                else:
                    items[name] = {"price": price, "qty": qty, "total": price * qty}

        line = "=" * 78
        print(f"Products received on {day}")
        print(line)
        print(f"| {'Date':<10} | {'Name':<20} | {'Price per piece':>15} | {'Qty':>6} | {'Total price':>11} |")
        print(line)
        for name, data in items.items():
            print(f"| {day:<10} | {name:<20} | {data['price']:>15.2f} | {data['qty']:>6} | {data['total']:>11.2f} |")
        print(line + "\n")
        

def Sales(stock):
    pass


def Daily_Sales(stock):
    pass


def report_sales(stock):
    pass