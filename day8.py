# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
d = {}
for i in xrange(int(raw_input())):   
    key,val = map(str,sys.stdin.readline().split())
    #key = raw_input().strip()
    #val = int(raw_input())
    d[key]=val
while(True):
    k = raw_input().strip()            
    if k!='':
        if d.has_key(k): print k + '=' + str(d[k])
        else: print "Not found"
    else: break