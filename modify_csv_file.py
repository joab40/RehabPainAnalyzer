
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
new_cvs_file_list = []
#new_cvs_file_list.append("empty")
colum_with_values = []
colum_with_no_values = []

replace_append_data = ''

for colum in range(partlen):
    print "COLUM NAME: ", headlist[colum]
    check_empty_data = True
    countlines = 0
    with open('test.csv') as inf:
        for line in inf:
            parts = line.split(",") # split line into parts
            if len(parts) > 1:   # if at least 2 parts/columns
                #print "NEW_CVS_FILE_LIST: ", new_cvs_file_list, " fethcning value: ", colum
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
        colum_with_values.append(headlist[colum])
    else:
        print "EMPTY IN: ", headlist[colum]
        colum_with_no_values.append(headlist[colum])

print "These columes have legit valuse: ", colum_with_values
for colum in range(partlen):
    print "COLUM NAME: ", headlist[colum]
    check_empty_data = True
    countlines = 0
    with open('test.csv') as inf:
        for line in inf:
            parts = line.split(",") # split line into parts
            if len(parts) > 1:   # if at least 2 parts/columns
                if colum == 0:
                    new_cvs_file_list.append(parts[colum])
                    #print "NEW_CVS_FILE_LIST: ", new_cvs_file_list, " fethcning value: ", colum
                #elif headlist[colum] != parts[colum] and headlist[colum] in colum_with_values:
                elif headlist[colum] in colum_with_values:
                    if colum != 0:
                        # reading new file structure
                        read_copy_of_row = new_cvs_file_list[countlines]
                        new_cvs_file_list[countlines] = read_copy_of_row + ',' + parts[colum]
                        countlines +=1

                    print headlist[colum]," -> ", parts[colum]

for row in new_cvs_file_list:
    print row

print "column with missing valuse: ", colum_with_no_values