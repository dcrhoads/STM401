
fh = open('mbox.txt')
print(fh)

for lx in fh:
    ly = lx.rstrip()
    print(ly.upper())
    