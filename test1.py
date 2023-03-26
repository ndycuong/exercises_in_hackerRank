#List Comprehensions
'''if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
list1 =[]  
for i in range(x+1):
    for a in range(y+1):
        for b in range(z+1):
            if i+a+b !=n: list1.append([i,a,b]) 
print(list1)
#print([[i,a,b] for i in range(0,x+1) for a in range(0,y+1) for b in range(0,z+1) if i+a+b !=n] )
'''
#Runner-up score: 2nd ranking
'''if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
print(list(set(sorted(arr)))[-2])

#a=list(set(sorted(arr)))
#if len(a) >1:
#    print(a[-2]) 
#else: 
#    print ("khong ton tai")
'''

#nested lists
'''
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])
x =[marks for name, marks in marksheet]
if len(set(x))>1:
    second_highest = sorted(list(set(x)))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
else :
    print('nothing')
'''

#finding the percentage:
'''if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
query_scores= student_marks[query_name]
score=0
for i in range(len(query_scores)):score+=query_scores[i]
print(f'{score/len(query_scores):.2f}') #always show 2 decimal place
'''  
#lists performing command from the text board with print, insert, remove,pop,append,
'''
def function1(x,y):
     #x=input(), y = list1   
    b = x.split(' ')
    a= b[0]
    
    if a=='print': 
        print(y)
    elif a=='insert':
        e=int(b[1]); d=int(b[2]) 
        y.insert(e,d)
    elif a=='remove': 
        d=int(b[1])
        if d in y: y.remove(d) 
        
    elif a=='append':
        d=int(b[1])
        y.append(d)
    elif a=='sort': 
        y.sort()
    elif a=='pop':
        if len(y)>1:y.pop()
    elif a=='reverse': 
        y.reverse()
    else :
        return False
if __name__ == '__main__':
    N = int(input())
    list1=[]
    for i in range(N):
        c=input()
        function1(c,list1)
'''
'''
s="insert 2 3".split()
cmd=s[0]
args=s[1:]
cmd+= "("+ ",".join(args) +")"
print(cmd) => insert(2,3)
''' 
'''
x="ha ha he".split() 
args=x[1:]
c=','.join(args) 
print(f"({c})")
'''

#solution2: not correct in all cases
'''
N=int(input())
l=[]
for _ in range(N):
    s=input().split()
    cmd =s[0]

    if cmd !="print":
        args =s[1:]
        c=','.join(args)
        cmd += f"({c})"
        eval('l.'+cmd)
    else :
        print(l)
 '''
