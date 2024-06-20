from function import addtwonumbers
p=int(input("Enter first value"))
q=int(input("Enter second value"))

oper=input("Enter operation that you want")
result=0
if oper== "+":
    print(p+q)
elif oper== "-":
    print(p-q)
elif oper== "*":
    print(p*q)
elif oper== "/":
    print(p/q)
elif oper== "%":
    print(p%q)
else:
    print("Invalid Input")
addtwonumbers()