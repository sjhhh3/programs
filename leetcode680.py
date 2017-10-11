
'''
def validPalindrome(ques):
    if not ques:
        return None
    a = list(ques)
    for i in range(0, int(len(ques) / 2) + 1):  # int(len(ques)/2)+1
        if ques[i] == ques[-i - 1]:
            continue
        elif ques[i + 1] == ques[-i - 1]:
            a=ques[0:i]+ques[i+1:]
            print(a)
            break
        elif ques[i] == ques[-i -2]:
            a=ques[0:-i]
            print(a)
            break

    ans = ''.join(a)
    print(ans)
    for i in range(0, int(len(ans) / 2) + 1):
        if ans[i] == ans[-i - 1]:
            continue
        else:
            return False
    return True

print(validPalindrome(ques))
'''

count = 0
def do(a):
    global count
    if not a:
        return None
    while count<2:
        if len(a) <= 2:
            return True
        elif a[0] == a[-1]:
            a = a[1:-1]
            continue
        elif a[1] == a[-1] and a[0] == a[-2]:
            count += 1
            if do(a[1:]) or do(a[0:-1]):
                return True
        elif a[1] == a[-1]:
            a = a[1:]
            count += 1
            do(a)
        elif a[0] == a[-2]:
            a = a[0:-1]
            count += 1
            do(a)
        else:
            return False
    return False
#ques = "ececaacec"
ques = "icviyyvici"
a = list(ques)
print(do(a))


