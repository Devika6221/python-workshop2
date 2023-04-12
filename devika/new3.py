list = []
even = []

for i in range (1,101):
    list.append(i)
    
for i in list:
    if(i%2==0):
        even.append(i)

print(even)