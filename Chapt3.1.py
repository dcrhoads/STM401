hrs = input("Enter Hours: ")
pay = input("Pay Rate: ")
fh = float(hrs)
fp = float(pay)
if fh > 40 :
    print("Overtime")
    reg = fh * fp
    otp = (fh - 40) * (fp * 0.5)
    print(reg,otp)
    gross = reg + otp
else:
    print("Regular")
    gross = fh * fp
print("Gross Pay:", gross)
