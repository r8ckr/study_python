#!/usr/bin/env python3


n = str(input())

a1 = "1"
a2 = a1 + "," + "2" + "," + a1
a3 = a2 + "," + "3" + "," + a2
a4 = a3 + "," + "4" + "," + a3
a5 = a4 + "," + "5" + "," + a4
a6 = a5 + "," + "6" + "," + a5
a7 = a6 + "," + "7" + "," + a6
a8 = a7 + "," + "8" + "," + a7
a9 = a8 + "," + "9" + "," + a8
a10 = a9 + "," + "10" + "," + a9
a11 = a10 + "," + "11" + "," + a10
a12 = a11 + "," + "12" + "," + a11
a13 = a12 + "," + "13" + "," + a12
a14 = a13 + "," + "14" + "," + a13
a15 = a14 + "," + "15" + "," + a14
a16 = a15 + "," + "16" + "," + a15

ans = eval("a" + n)
print(ans.replace(",", " "))
