myList = [1, 2, 3, 4, 5]
myTuple = (1, 2, 3, 4, 5)
myDictionary = {1: "Jordan", 2: "dfsd"}

for num in myList:
    print("Number: ", num)

for dict in myDictionary.items():
    print("Dictionary: ", dict)

myTuple[0] = 5
print(myTuple)
