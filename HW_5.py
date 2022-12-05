f = open('file1.txt', "r")
l = [line.strip() for line in f]
f = open('file2.txt', "r")
m = [line.strip() for line in f]
l_1 = str(l).split(" + ")
m_1 = str(m).split(" + ")
count = 6
new_list=[]
while count>0:
    for i in l_1:
        a = str("x^"+str(count))
        if a in i:
            b = i
            for j in m_1:
            c = str("x^"+str(count)) #здесь выдает ошибку IndentationError: expected an indented block after 'for' statement on line 14, но в 11 строке этой ошибки нет
                if c in j:
                    d = j
                    e = b+d
                    new_list.append (e)

        count=count-1
new_list.append((l[-1]+m[-1]))


print (new_list)