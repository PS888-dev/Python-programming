'''
นับตัวอักษร
Input
 KMUTNB KMITL KMUTT
Output
K 3
M 3
U 2
T 4
N 1
B 1
  2
I 1
L 1
'''
text = "KMUTNB KMITL KMUTT"
count = {}
for i in  text:
    count[i] = count.get(i,0)+1
    # print(text)
# print(count)
for key in count:
    print(key, count[key])