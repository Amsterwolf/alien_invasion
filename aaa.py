class AAA:
    def __init__(self):
        self.aaa=1

new_aaa=AAA()
dic={}
dic[new_aaa]=3
print(dic.items())

for i,j in dic.items():
    if i.aaa==1:
        i.aaa=3

print(dic.items())
print(new_aaa.aaa)