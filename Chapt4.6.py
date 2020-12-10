def computepay(hours, pay) :
   # print("In computepay", hours, pay)
    if hours > 40:
        reg = hours * pay
        otp = (hours - 40) * (pay * 0.5)
        print(reg, otp)
        gross = reg + otp
    else:
        gross = hours * pay
   # print("Returning", gross)
    return gross

hrs = input("Enter Hours: ")
pay = input("Pay Rate: ")
fh = float(hrs)
fp = float(pay)

gross = computepay(fh, fp)

print("Gross Pay:", gross)
