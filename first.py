#coding=utf-8
import re
a,b = 0,1
while b<10:
    print(b)
    a,b = b,a+b
print(a)
print("-----我是分割线-----")
print(max(a,b))
varl  = 100
if varl:
    print("1- if "+"1111")
    print(varl)
print("-----我是分割线-----")
m = re.match('foo','foo')
if m is not None:
    print(m.group())
print(m)
print("-----我是分割线-----")
pattern = 'afo'
n = re.search(pattern,'seafood')
if n is not None:print(n.group())
print("-----我是分割线-----")
cb = '[cr][23][dp][o2]'
k = re.match(cb,'cr3po')
if k is not None:print(k.group())
NotImplemented