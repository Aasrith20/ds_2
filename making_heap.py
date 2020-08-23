n=int(input())
values=list(map(int,input().split()))
ans=list()
def shiftdown(values,index,ans):
     a=(index)*2+1
     b=(index)*2+2
     n=len(values)
    #  print("a="+str(a)+" b="+str(b)+" n="+str(n))
     if(a<n and b<n):
        #  print("first")
         if(values[a]<values[b]):
             if(values[index]>values[a]):
                 values[index],values[a]=values[a],values[index]
                 ans.append([index, a])
                 shiftdown(values,a,ans)
         else:
             if(values[index] > values[b]):
                 values[index], values[b] = values[b], values[index]
                 ans.append([index, b])
                 shiftdown(values,b,ans)
     elif(a<n and b>=n):
            #  print("second")
             if(values[index] > values[a]):
                 values[index], values[a] = values[a], values[index]
                 ans.append([index, a])
                 shiftdown(values,a,ans)
     elif(a>=n and b<n):
            # print("third")
            if(values[index] > values[b]):
                 values[index], values[b] = values[b], values[index]
                 ans.append([index, b])
                 shiftdown(values, b,ans)
n=len(values)
index=(n-1)//2
while(index>=0):
    # a=check(values,index,ans)
    # if(a!=-1):
    shiftdown(values,index,ans)
    index-=1
print(len(ans))
for i in ans:
    print(" ".join(str(j)for j in i))
#         1
#      2     4
#   3    6  5   8
# 10  7 9
