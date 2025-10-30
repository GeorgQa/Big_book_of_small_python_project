



precondition_str = "AAAAABBBBBCDDDDEEEF"
z = 0
y  = []


for  i in range(len(precondition_str)):
    if i == 0 :
        y.append(precondition_str[i])
    elif precondition_str[i] not in y:
        y.append(z)
        y.append(precondition_str[i])
    else:
        z+= 1
