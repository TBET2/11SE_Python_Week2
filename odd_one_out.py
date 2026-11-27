## INITIAL PROBLEM CODE
##line1 = raw_input()
##line2 = raw_input()
##line3 = raw_input()
##
##if line1 != line3:
##    if line2 != line3:
##        print line3
##    else:
##    if line1 = line3:
##        print line2
##else:
##    print ’line1’
##
##
##    



## PSUEDO CODE SOLUTION
# Get line1, line2, and line3
# checks if line1 is equal to line2
# if line1 is equal to line2 then print line 3
# checks if line1 is equal to line2
# if line2 is equal to line3 then print line 1
# checks if line1 is equal to line2
# if line1 is equal to line3 then print line 2


line1 = input("Say a line: ")
line2 = input("Say a line: ")
line3 = input("Say a line: ")

if line1 == line2:
    print(line3)
elif line2 == line3:
    print(line1)
elif line1 == line3:
    print(line2)
else:
    print("None of them are the same")
