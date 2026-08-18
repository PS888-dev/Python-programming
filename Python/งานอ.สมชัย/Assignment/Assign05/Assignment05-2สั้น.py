print("=== ระบบคำนวณเงินหน้าร้าน (POS) ===")
value = int(input("กรุณากรอกสินค้าทั้งหมด(บาท): "))
member = input("ลูกค้าเป็นสมาชิกหรือไม่? (y/n): ") == "y"
print()
bar1, bar2 = "-"*34, "="*34

if value <= 1000: discount1 = 0
elif value <= 5000: discount1 = 2.5
elif value <= 10000: discount1 = 5
elif value <= 19999: discount1 = 7.5
else: discount1 = 10

discount2 = 5 if member else 0
discount3 = discount1 + discount2

Product_discount = value * (discount1/100)
Member_Discount = value * (discount2/100)
Total_discount = Product_discount + Member_Discount
Total_value = value - Total_discount

print(f"{bar1}\nส่วนลดที่ได้รับรวม: {discount3:.1f}% ({Total_discount:,.2f} บาท)")
print(f"จำนวนเงินที่ต้องจ่ายจริง: {Total_value:,.2f} บาท\n{bar1}")

Amount_received = int(input("จำนวนเงินที่ได้รับมา (บาท): "))
print()
print(f"{bar2}\n     สรุปการชำระเงิน\n{bar2}")
print(f"ราคารวมสินค้า   : {value:.2f}\nส่วนลดตามยอดซื้อ ({discount1:.1f}%): {Product_discount:.2f} บาท")
print(f"ส่วนลดสมาชิก  ({discount2:.1f}%):  {Member_Discount:.2f} บาท\nส่วนลดทั้งหมด :  {Total_discount:,.2f} บาท\n{bar1}")
print(f"ยอดเงินที่ต้องจ่ายจริง :  {Total_value:,.2f} บาท")
print(f"จำนวนเงินที่ได้รับมา :  {Amount_received:,.2f} บาท")
print(f"จำนวนเงินทอน     :     {Amount_received - Total_value:,.2f} บาท\n{bar2}")