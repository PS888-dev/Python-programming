try:
    filename = input("Enter file name : ")
    fin = open(filename, encoding="utf-8")
    data = fin.read()
    print(data)
    fin.close()
except FileNotFoundError:
    print(f"File {filename} Not open, this file not found.")
else:
    print("Work Complete.")
finally:
    print("End Program.")