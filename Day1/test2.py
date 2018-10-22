Q1 = [1, 4, 6, 3, 5, 6, 7, 3]
big = max(Q1)
print(big)

Q2 = [3, 4, "6", "1", 9]
a = list(map(int, Q2))
print(a)

Q3 = {"K1": "V1", "K2": "V3", "K3": "V3"}
b = {val:key for (key, val) in Q3.items()}
print(b)
#keys need to be unique to switch

Q4 = (1, 2, 3, 4, 5)
Q4 = (4, 3, 2, 1, 3)
print(Q4)

Q5 = [50, 96, 45, 67, 88]
for i in Q5:
    if i < 70:
        print("FAIL", i)
    else:
        print("PASS", i)

