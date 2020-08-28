import collections
m=int(input())
values=[collections.deque([]) for i in range(m)]
x=263
p=1000000007
ans=[]
def hash(string,m):
    sum=0
    index=0
    for i in string:
        sum+=(ord(i))*(x**index)
        index+=1
    sum=(sum%p)%m
    return(sum)
def add(string,values,m):
    key=find(string,values,m)
    if(key=="not included"):
        values[hash(string,m)].appendleft(string)
def delete(string,values,m):
    key=find(string,values,m)
    # print(hash(string,m),string)
    if(key!="not included"):
        values[hash(string,m)].remove(key)
def find(string,values,m):
    try:
     for i in values[hash(string,m)]:
         if(i==string):
             return(string)
     return("not included")
    except:
         return("not included")
def check(num,values,ans,m):
        if len(values[int(num)])!=0:
            ans.append(" ".join(str(i) for i in values[int(num)]))
        else:
            ans.append("")
num_1=int(input())
for i in range(num_1):
  #  print(values)
    values_1=list(input().split())
    if(values_1[0]=="add"):
        add(values_1[1],values,m)
    elif(values_1[0]=="check"):
        check(values_1[1],values,ans,m)
    elif(values_1[0]=="find"):
        q=find(values_1[1],values,m)
        if(q=="not included"):
            ans.append("no")
        else:
            ans.append("yes")
    elif(values_1[0]=="del"):
        delete(values_1[1],values,m)
for i in ans:
   print(i)

