# Enter your code here. Read input from STDIN. Print output to STDOUT
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
#Take input
a = int(raw_input())
f=factorial(a)
print f