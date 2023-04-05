print(6%4)

n = int(input().strip())
rest = (n % 2)
range1 = (1, 6)
range2 = (5, 21)

print(2 in range1)
print(2 in range1)

if (rest==1):
    print("Weird")
elif (rest==0) and (n in range1):
    print("Not Weird")
elif (rest==0) and (n in range2):
    print("Weird")
elif (rest==0) and (n >20):
    print("Not Weird")



