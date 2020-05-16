# Room Area
f = input("Enter the room shape ([t]riangle|[r]ectangle|[c]circle):")
s = 0
if f in ["triangle", "t"]:
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**.5
if f in ["rectangle", "r"]:
    a = int(input())
    b = int(input())
    s = a*b
if f in ["circle", "c"]:
    r = int(input())
    s = 3.14*r**2
if (s != 0):
    print(s)
else:
    print("Undefined shape of the room!")