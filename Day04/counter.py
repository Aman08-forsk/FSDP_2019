# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 12:16:08 2019

@author: Hp
"""

file=open('romeo.txt','rt')
words=file.read()
count_char={}
for i in words:
    if i in count_char:
        count_char[i]+=1
    else:
        count_char[i]=1
print("number of characters"+ str(count_char))
file.close()
file=open('romeo.txt','rt')
words1=file.read().split()
count_word={}
for i in words1:
    if i in count_word:
        count_word[i]+=1
    else:
        count_word[i]=1
print("number of words:"+ str(count_word))
file=open('romeo.txt','rt')
word2=file.readlines()
print("number of lines:"+ str(len(word2)))
file=open('romeo.txt','rt')
word3=file.read().split()
print("number of unique words:"+ str(len(word3)))