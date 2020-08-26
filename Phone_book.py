n=int(input())
values=[-1]*10**7
def add(number,name,values):
    values[number]=name
def find(number,values):
    if(values[number]==-1):
        print("not found")
        return
    print(values[number])
def delete(number,values):
    if(values[number]!=-1):
        values[number]=-1
for i in range(n):
    values_1=list(input().split())
    if(values_1[0]=="del"):
          delete(int(values_1[1]), values)
    elif(values_1[0]=="add"):
        add(int(values_1[1]),values_1[2],values)
    else:
        find(int(values_1[1]),values)
