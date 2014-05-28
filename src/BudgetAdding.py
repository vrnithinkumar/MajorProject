'''
Created on 12-Mar-2014

@author: vr
'''

fname = "Data/Budget.txt"
with open(fname) as f:
    content = f.readlines()
dic = {}
c = 0
for i in content:
	name = i.split()[0]
	budg = i.split()[1]
	if budg != "NIL":
		c = c + 1
	dic[name] = budg
	print budg
print c
