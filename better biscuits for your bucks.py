
cost1 = float(input("Cost of packet 1? "))
num1 = int(input("Biscuits in packet 1? "))
cost2 = float(input("Cost of packet 2? "))
num2 = int(input("Biscuits in packet 2? "))
pp1 = cost1/num1
pp2 = cost2/num2
stop = ""

while True:
    if pp1 and pp2 != 0:
        if  pp1 > pp2:
            print("packet 1")
        elif pp2 < pp1:
            print("packet 2")
        else:
            print("packet 1 or 2")
    stop = input("Say stop if you wanna stop? ")
    if stop.lower() == "stop":
        break

    cost1 = float(input("Cost of packet 1? "))
    num1 = int(input("Biscuits in packet 1? "))
    cost2 = float(input("Cost of packet 2? "))
    num2 = int(input("Biscuits in packet 2? "))
    pp1 = cost1/num1
    pp2 = cost2/num2


 
