file = open("romeo.txt","r")
list = []

for line in file:
    words = line.split(" ")
    for word in words:
        upper = word.upper()
        if upper not in list:
            list.append(upper.strip())

list.sort()
print(list)