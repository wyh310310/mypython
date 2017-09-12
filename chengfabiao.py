# -*- coding: UTF-8 -*-
print("九九乘法表");
for x in range(1,10):
    result = "";
    for y in range (1,x+1):
        result += str(x)+ "*"+str(y)+"="+str(x*y)+"\t";
    print result