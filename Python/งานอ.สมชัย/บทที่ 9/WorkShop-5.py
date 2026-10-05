def read_mydata(filename):
    fin = open(filename,encoding="utf-8")
    print("Open file mydata.txt")
    print("Use readline to read data from file.")
    data1 = fin.readline(5)
    data2 = fin.readline()
    print(data1,data2)
    fin.close()
    print("Now closed file.")

def read_myscore(filename):
    fin = open(filename,encoding="utf-8")
    datas = fin.readlines()
    fin.close()
    return(datas)

def main():
    read_mydata("mydata.txt")
    print("Read data from file myscore.txt")
    print(read_myscore("myscore.txt"))

if __name__ == "__main__":
    main()