import collections
num=list(map(int,input().split()))
values=[]
for i in range(num[1]):
    values.append(list(map(int,input().split())))
pipe=collections.deque([values[0]])
if num[1]>=1:
    ans=[values[0][0]]
else:
    ans=[]
next_starting_time=collections.deque([values[0][1]])
index=1
for i in range(1,num[1]):
    # print(pipe,next_starting_time,index,ans)
    if len(pipe)<num[0]:
        pipe.append(values[i])
        if next_starting_time[index-1]<values[i][0]:
            ans.append(values[i][0])
        else:
            ans.append(next_starting_time[index-1])
        next_starting_time.append(values[i][1]+next_starting_time[index-1])
        index+=1
    elif len(pipe)==num[0] and next_starting_time[0]<=values[i][0]:
        if next_starting_time[index-1] < values[i][0]:
            ans.append(values[i][0])
        else:
            ans.append(next_starting_time[index-1])
        next_starting_time.append(values[i][1]+next_starting_time[index-1])
        pipe.popleft()
        next_starting_time.popleft()
        pipe.append(values[i])
    else:
        ans.append(-1)    
    # print(time_finished[len(time_finished)-1], pipe[0][1],pipe,time_finished,values[i],sep="_")
# print(time_finished)
print(" ".join(str(i) for i in ans))

