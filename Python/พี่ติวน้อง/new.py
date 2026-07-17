item1_name, item1_qty, item1_price = "Apple", 3, 45.00
item2_name, item2_qty, item2_price = "Banana", 12, 120.50
item3_name, item3_qty, item3_price = "Coconut Water", 1,35.00

print("-*34")
print(f"{'Produck Name':<15} | {'Quantity':^10} | {'Price':>10}")
print("-"*43)

print(f"{item1_name:<15} | {item1_qty:^10} | {item1_price:>10.2f}")
print(f"{item2_name:<15} | {item2_qty:^10} | {item2_price:>10.2f}")
print(f"{item3_name:<15} | {item3_qty:^10} | {item3_price:>10.2f}")
print("-"*43)