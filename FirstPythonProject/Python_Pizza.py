print("welcome to the python pizza deliveries!")
size = input("What size do you want? S, M or L: ")
pepperoni = input("Do you want to add pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size == "S" or size == "s":
    bill += 15
elif size == "M" or size == "m":
    bill += 20
elif size == "L" or size == "l":
    bill += 25
else:
    print("choose size of pizza S M or L:")
if pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: Rs{bill}.")
