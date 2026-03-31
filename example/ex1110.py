f = open('list.txt','r', encording = 'utf8')
for line in f:
    print(line, end='')
f.close()