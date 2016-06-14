
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
new_cvs_file_list = [365]
new_cvs_file_list[0] = "empty"

replace_append_data = ''

for colum in range(partlen):
    print "COLUM NAME: ", headlist[colum]
    check_empty_data = True
    countlines = 0
    with open('test.csv') as inf:
        for line in inf:
            parts = line.split(",") # split line into parts
            if len(parts) > 1:   # if at least 2 parts/columns
                if colum == 0:
                    print "start: count lines = 0"
                    new_cvs_file_list[colum] = parts[colum]
                else:
                    print "countlines: ", countlines
                    replace_append_data = new_cvs_file_list[colum]
                    new_cvs_file_list[colum] = replace_append_data + parts[colum]

                if not head:
                    head = parts[colum]
                else:
                    print parts[colum]   # print column 2
            if parts[colum] == headlist[colum]:
                print "header TOP"
            elif parts[colum] != '"0"':
                print "parts have value: ", parts[colum]
                check_empty_data = False
            countlines +=1
    if not check_empty_data:
        print "DATA in: ", headlist[colum]
    else:
        print "EMPTY IN: ", headlist[colum]
