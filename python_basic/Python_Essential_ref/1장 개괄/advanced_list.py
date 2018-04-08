# coding: utf-8

import sys
if len(sys.argv) !=2: 
    print("Plase supply a filename")
    raise SystemExit(1)
f = open(sys.argv[1])  
lines = f.readlines() 
f.close()

fvalues = [float(line)  for line in lines]  

print("The minimum value is ", min(fvalues))
print("The maximum value is ", max(fvalues))