#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
   给定一个源串和目标串，能够对源串进行如下操作：
   1.在给定位置上插入一个字符
   2.替换任意字符
   3.删除任意字符
   写一个程序，返回最小操作数，使得对源串进行这些操作后等于目标串，源串和目标串的长度都小于2000。
 
   输入：两个字符串，一个源串，一个目标串
   输出：最小操作数
'''
sourStr=raw_input("enter a source string:")
targetStr=raw_input("enter a target string:")
slen=len(sourStr)
tlen=len(targetStr)
count=0
if slen == tlen:
    for i in range(0,slen):
       if sourStr[i] == targetStr[i]:
           break
       else:
           count = count + 1
elif slen < tlen:
    for i in range(0,slen):
        if sourStr[i] == targetStr[i]:
            break
        else:
            count = count + 1
    count = count + tlen - slen
else:
    for i in range(0,tlen):
        if sourStr[i] == targetStr[i]:
            break
        else:
            count = count + 1
    count = count + slen - tlen

print "num is :",count
    
