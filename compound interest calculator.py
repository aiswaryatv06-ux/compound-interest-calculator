principle=0
rate=0
time=0
while principle<=0: 
    principle=float(input("ENTER THE PRINCIPLE AMOUNT:"))
    if principle<=0:
        print("Principle amount cant be less than or equal to 0 try again")
while rate<=0: 
    rate=float(input("ENTER THE RATE:"))
    if rate<=0:
        print("Rate cant be less than or equal to 0 try again")
while time<=0: 
    time=int(input("ENTER THE TIME:"))
    if time<=0:
        print("Time cant be less than or equal to 0 try again")
total= principle * pow((1 + rate / 100),time)
print(f"Your new balance is ${total:.2f}")