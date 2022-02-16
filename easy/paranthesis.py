open_b = ['(', '{', '[']
close_b = [')', '}', ']']
pair = {"(": ")", "{": "}", "[": "]"}
s = ")"
temp = []
flag = 0
for i in s:
    print(flag, temp, i)
    if flag == 0:
        print(len(temp))

        print("hjhh")
        if i in open_b:
            temp.append(i)
        else:
            if len(temp)!=0:
                if i == pair.get(temp[-1]):
                    temp.pop()
                else:
                    flag += 1
            else:
                print("False")
    else:
        print('False')
print(len(temp) == 0)
