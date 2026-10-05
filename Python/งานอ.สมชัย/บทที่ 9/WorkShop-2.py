datas1 = ["Possawee","Jindaprasert","\n"]
datas2 = ("Python","File","\n")
datas3 = {"name":"Possawee","surname":"Jindaprasert"}
fount = open("mydata.txt","w")
fount.write("Salary : "+ str(1200.5)+"\n")
fount.writelines(datas1)
fount.writelines(datas2)
fount.writelines(datas3)
fount.close