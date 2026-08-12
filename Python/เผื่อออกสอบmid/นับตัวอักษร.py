'''
นับตัวอักษร
Input
 Banana
Output
B 1 
a 3 
n 2 
'''
text = "KMUTNB KMITL KMUTT"
count = {}
for i in  text:
    count[i] = count.get(i,0)+1
#     print(text)
# print(count)
for key in count:
    print(key, count[key])