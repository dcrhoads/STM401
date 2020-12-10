g = input("Enter Grade: ")
try:
    fg = float(g)
except:
    print("Bad Score")
    quit()
if fg > 1.0 :
    print("Bad Score")
    quit()
if fg < 0.0 :
    print("Bad Score")
    quit()
if fg >= 0.9 :
    print("A")
    quit()
if fg >= 0.8 :
    print("B")
    quit()
if fg >= 0.7 :
    print("C")
    quit()
if fg >= 0.6 :
    print("D")
    quit()
if fg < 0.6 :
    print("F")
    quit()
