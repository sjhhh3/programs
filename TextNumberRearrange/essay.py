
import re
f = open('2.txt', 'r')
s = f.read()
i = 0
def change1(matchobj):
    global i
    i += 1
    return f"[{i}]"

outp = re.sub('\[\d*\]\s*', "", s)
fn = open('3.txt', 'w')
fn.write(outp)
print(outp)