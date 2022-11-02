d = dict()  #алфавит нечетных строк
b = dict()   #алфавит четных строк

mystr = input()
count = 1

while mystr != "":
    if count % 2 == 1:
        for i in mystr:
            if i not in d:
                d[i] = i
        count += 1

    else:
        for i in mystr:
            if i not in b:
                b[i] = i
        count += 1
    print(mystr)
    mystr = input()

if len(d) > len(b):
    print("Mumbo")

if len(d) < len(b):
    print("Jumbo")
 
