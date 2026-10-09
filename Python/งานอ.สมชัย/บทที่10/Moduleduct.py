def add_product(filename):
    print("Enter data product.")
    prod_id = input("Input product id : ")
    prod_name = input("Input product name : ")
    prod_price = input("Input product price : ")
    prod_qty = input("Input product quantity : ")
    try:
        fout = open(filename,"a",encoding="UTF_8")
        fout.write(prod_id+","+prod_name+","+prod_price+","+prod_qty+'\n')
        fout.close()
    except FileNotFoundError:
        print(f"{filename} is not found")
    else:
        print("Save Data Product allread.\n")

def report_from_file(filename):
    n = 0
    try:
        with open(filename,encoding="utf-8") as fin:
            for prod in fin:
                n += 1
                prod_list = prod.rstrip("\n").split(",")
                prod_str = ":".join(f"{data:>5}" for data in prod_list)
                print(f"Product {n:2} : " + prod_str + ":")
    except FileNotFoundError:
        print(f"{filename} is nt found")

def read_product(filename):
    product = []
    try:
        with open(filename,encoding="utf-8") as fin:
            for prod in fin:
                prod = prod.rstrip("\n")
                product.append(prod.split(","))
    except FileNotFoundError:
        print(f'{filename} is not found')
    else:
        return(product)

def report_product(products):
    head = "Report Product".center(62) +"\n"
    head += ("-"*62)+"\n"
    head += "| No. |  Id  |  Name     |     Price    |Quantity|     Total     |\n"
    head += ("-"*62)+"\n"
    n = 1
    mess = ""
    try:
        for prod in products:
            price = float(prod[2])
            qty = float(prod[3])
            total = price*qty
            