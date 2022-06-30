#!/usr/bin/env python
# coding: utf-8

# In[ ]:


###############TASK-1#################

f = open('input.txt',mode = 'r')
lines = f.readlines()
f2 = open('output.txt',mode = 'w')

pal = 0
oddparity = 0
evenparity = 0
noparity = 0
total = 0

for i in lines:
    x,y = i.split(' ')
    z = y.strip()

    if x.isdigit():
        if int(x)%2==0 and z == z[::-1]:
            str1 = f'{x} has even parity and {z} is a palindrome\n' 
            f2.write(str1)
            evenparity += 1
            pal += 1
            total += 1
        elif int(x)%2 != 0 and z == z[::-1]:
            str2 = f'{x} has odd parity and {z} is a palindrome\n'
            f2.write(str2)
            oddparity += 1
            pal += 1
            total += 1
        elif int(x)%2 == 0 and z != z[::-1]:
            str3 = f'{x} has even parity and {z} is not a palindrome\n'
            f2.write(str3)
            evenparity += 1
            total += 1
        elif int(x)%2 != 0 and z != z[::-1]:
            str4 = f'{x} has odd parity and {z} is not a palindrome\n'
            f2.write(str4)
            oddparity += 1
            total += 1
    else:
        if z != z[::-1]:
            str5 = f'{x} cannot have parity and {z} is not a palindrome\n'
            f2.write(str5)
            noparity += 1
            total += 1

        elif z == z[::-1]:
            str6 = f'{x} cannot have parity and {z} is  a palindrome\n'
            f2.write(str6)
            noparity += 1
            total += 1
            pal += 1

f3 = open('record.txt',mode = 'w')

st1 = f'percentage of odd parity:{(oddparity/total)*100}%\n'
st2 = f'percentage of even parity:{(evenparity/total)*100}%\n'
st3 = f'percentage of no parity:{(noparity/total)*100}%\n'
st4 = f'percentage of palindrome:{(pal/total)*100}%\n'
st5 = f'percentage of no palindrome:{((total-pal)/total)*100}%\n'

f3.write(st1)
f3.write(st2)
f3.write(st3)
f3.write(st4)
f3.write(st5)

f2.close()
f3.close()

