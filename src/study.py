#test list a
a=[1,2,3,4,5]
print a
#append
a.append(22)
print a
#pop
a.pop()
print a
#remove
a.remove(4)
print a
a.remove(1)
print a
#reverse
a.reverse()
print a
#sort
a.sort()
print a
#*
b=a*3
c=a*3
print b
print c

#slice operation
print b[1],b[-1],b[0]
print b[1:4]
b[1:5]=[1,2,3,4,6555,777]
print b
#nested
b[1]=c
print b
b[1]=b
print b
print b[1][1][2]
#print
print len(c)


