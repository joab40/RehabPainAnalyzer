
rownr = 5
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

for colum in range(partlen):
    print "COLUM NAME: ", headlist[colum]
    check_empty_data = True
    with open('test.csv') as inf:
        for line in inf:
            parts = line.split(",") # split line into parts
            if len(parts) > 1:   # if at least 2 parts/columns
                if not head:
                    head = parts[colum]
                else:
                    print parts[colum]   # print column 2
            if parts[colum] == headlist[colum]:
                print "header TOP"
            elif parts[colum] != '"0"':
                print "parts have value: ", parts[colum]
                check_empty_data = False
    if not check_empty_data:
        print "DATA in: ", headlist[colum]
    else:
        print "EMPTY IN: ", headlist[colum]
