#Test Case 1:
#input: Yarr Har
#output: 1

#Test case 2:
#Ahoy m'hearties
#Yo ho ho and a bottle of rrrrum
#Tharrrr be th' treasure
#output: 2

#Test case 3:
#input: Hello, how are you?
#output:0


#Test case 4:
#input:
#output: 0

bob = str(input("What is Bob Saying? "))
count = 0
if "rr" in bob.lower():
    count += 1

while bob.lower() != "":
    bob = str(input("What is Bob Saying? "))
    if "rr" in bob.lower():
        count += 1


print(count)
