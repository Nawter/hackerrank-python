# Enter your code here. Read input from STDIN. Print output to STDOUT
m = float(raw_input().strip())
t = float(raw_input().strip())
x = float(raw_input().strip())

print "The total meal cost is " + str(int(round(m + ((t*m)/100) + ((x*m)/100)))) + " dollars."