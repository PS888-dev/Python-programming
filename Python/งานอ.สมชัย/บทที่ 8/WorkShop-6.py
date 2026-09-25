datas = {}
for n in range(5):
    name = input(f"Enter name %d : "%n)
    datas[n] = name

print()
print(datas)
# for n in datas:
#     print(f"datas[{n}] = {datas[n]}")

for key in datas.items():
    print(f"datas[{key}] = {datas}")