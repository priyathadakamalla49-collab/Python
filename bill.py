bill = int(input("Enter Bill Price: "))
payment =input("Enter Payment Method: ") #Credit,Cash,Debit,Netbanking
if payment == "credit":
    bank = input("Enter Bank name: ") #HDFC,SBI
    if bank == "HDFC":
        total = bill - (bill * 10/100)
        print("The final amount is ",total)
    elif bank == "SBI":
        total = bill - (bill * 5/100)
        print("The final amount is ",total)
    else:
        total = bill - (bill * 2/100)
        print("The final amount is ",total)
elif payment == "cash":
    total = bill - (bill * 1/100)
    print("The final amount is ",total)
else:
    print("No discount")