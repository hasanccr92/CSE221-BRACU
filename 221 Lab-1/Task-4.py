#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##############TASK-5################
f1 = open('matInp.txt',mode = 'r')

n = int(f1.readline())


matA = []
for i in range(n):
    elm = f1.readline().split()
    matA.append(elm)

matB = []
for i in range(n):
    elm = f1.readline().split()
    matB.append(elm)

matC = [[0]*n for i in range(n)]

for i in range(len(matA)):
    for j in range(len(matB[0])):
        for k in range(len(matB)):
            matC[i][j] += int(matA[int(i)][int(k)]) * int(matB[int(k)][int(j)])

f2 = open('matOut.txt',mode = 'w')
for i in matC:
    str1 = str(i)+'\n'
    f2.write(str1)

f1.close()
f2.close()

