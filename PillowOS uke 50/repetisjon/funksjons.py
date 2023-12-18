def sumer(x, y):
    return x + y
def gjen(list):
    return sum(list) / len(list)

uIn = input("Enter Numbers with coma as delimeter\nEnter: ")

uIn.replace(" ", "")
l = uIn.split(",")
print(sumer(float(l[0]), float(l[-1])))

uIn2 = input("Enter Numbers with coma as delimeter\nEnter: ")

uIn2.replace(" ", "")
myList = uIn2.split(",")
Intlist = [float(i) for i in myList]
print(gjen(Intlist))