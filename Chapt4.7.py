def computegrade(grade) :

g = input("Enter Grade: ")
try:
    grade = float(g)
except:
    print("Bad Score")
    quit()
if grade > 1.0 :
    print("Bad Score")
    quit()
if grade < 0.0 :
    print("Bad Score")
    quit()
if grade >= 0.9 :
    print("A")
    quit()
if grade >= 0.8 :
    print("B")
    quit()
if grade >= 0.7 :
    print("C")
    quit()
if grade >= 0.6 :
    print("D")
    quit()
if grade < 0.6 :
    print("F")
    quit()
