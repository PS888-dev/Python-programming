cash=int(input("Enter number money withdraw : "))

cash1=float(cash//1000)
cash=cash%1000

cash2=float(cash//500)
cash=cash%500

cash3=float(cash//100)

print()
print("Cash B1000 : ",cash1)
print("Cash B500 : ",cash2)
print("Cash B100 : ",cash3)