import collections
n=int(input())
values=list(map(int,input().split()))
num=int(input())
dummy=collections.deque([int(i) for i in range(num)])
index=0
ans=list()
dummy=collections.deque(sorted(dummy,key=lambda x:values[x],reverse=True))
def first(dummy,lower,upper,values):
   while(True):
    if(dummy[0]>=lower and dummy[0]<=upper):
         return(values[dummy[0]])
    else:
        dummy.popleft()
def execution(dummy,lower,upper,values):
        upper-=1
        while(True):
          if(len(dummy)>0):
              #print(dummy,dummy[len(dummy)-1],upper)
              if((values[dummy[len(dummy)-1]]<values[upper]) or dummy[len(dummy)-1]<=lower):
                  dummy.pop()
              else:
                  break
          else:
              break
        dummy.append(upper)    

for i in range(len(values)-num+1):
        ans.append(first(dummy,index,index+num-1,values))
        index+=1
        if(i!=len(values)-num):
            execution(dummy,index-1,index+num,values)
print(" ".join(str(i) for i in ans))
