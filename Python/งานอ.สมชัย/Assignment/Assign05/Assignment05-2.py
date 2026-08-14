print("=== ระบบคำนวณเงินหน้าร้าน (POS) ===")
value = int(input("กรุณากรอกสินค้าทั้งหมด(บาท): "))
member = input("ลูกค้าเป็นสมาชิกหรือไม่? (y/n): ")
discount1 = 0
discount2 = 5
discount3 = 0

if member == "y":
    if value <= 1000:discount1 = 0
    elif value >= 1001 and value <= 5000:discount1 = 2.5
    elif value >= 5001 and value <= 10000:discount1 = 5
    elif value >= 10001 and value <= 19999:discount1 = 7.5
    else:discount1 = 10
    discount3 = discount1 + discount2 
    Member_Discount = value * 0.05
    Product_discount = value * (discount1/100)
    Total_discount = Member_Discount + Product_discount
    Total_value = value - Total_discount
elif member == "n":
    print
print()
print(f"-"*34)
print(f"ส่วนรถที่ได้รับรวม:{discount3:.1f}% ({Total_discount:,.2f})")
print(f"จำนวนเงินที่ต้องจ่ายจริง: {value - Total_discount:,.2f}")
print(f"-"*34)
Amount_received = int(input("จำนวนเงินที่ได้รับมา (บาท)  :  "))
print()
print(f"{"="*34}\n{"สรุปการชำระเงิน":6^}\n{"="*34}") #Fix
print(f"ราคารวมสินค้า   : {value:.2f}")
print(f"ส่วนลดตามยอดซื้อ ({discount1:.1f})%: {Product_discount:.2f} บาท")
print(f"ส่วนลดสามชิก  {discount2:.1f}%:  {Member_Discount}\nส่วนลดทั้งหมด :  {discount3:.2f} บาท")
print(f"-"*34)
print(f"ยอดเงินที่ต้องจ่ายจริง :  {Total_value:,.2f} บาท")
print(f"จำนวนเงินที่ได้รับมา :  {Amount_received:,.2f} บาท")
print(f"จำนวนเงินทอน     : {Amount_received - Total_value:,.2f} บาท")
print(f"="*34)