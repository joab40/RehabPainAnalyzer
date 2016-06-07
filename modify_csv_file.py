
rownr = 0
head = False
headlist = False
columns = False
with open('test.csv') as inf:
    for line in inf:
        parts = line.split(",")
        partlen = len(parts)
        #print "partlen: ",partlen, " parts: ", parts
        if not headlist:
            headlist = parts
        elif not columns:
            columns = parts

print "headlist: ", headlist
print "columns : ", partlen

with open('test.csv') as inf:
    for line in inf:
        parts = line.split(",") # split line into parts
        if len(parts) > 1:   # if at least 2 parts/columns
            if not head:
                head = parts[rownr]
            else:
                print parts[rownr]   # print column 2
    rownr +=1
print "head: ", head