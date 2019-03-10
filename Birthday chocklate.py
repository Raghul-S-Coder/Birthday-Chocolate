def birthday(s,d,m):
    value=0
    if(m==1):
        for i in range(0,len(s)):
            if(d==s[i]):
                value=value+1
    else:
        
        for j in range(0,len(s)):
            i=0
            h=j
            
            val=0
            while(i<m):
                
                if(j<len(s)):
                    val=val+s[j]
                    
                    j=j+1
                i=i+1
                if(i==m):
                    if(val==d):
                        value=value+1
            j=h
    return value;

n=input()
s=list(map(int,input().split()))
d,m=(input().split())
d=int(d)
m=int(m)
result = birthday(s, d, m)
print("Ans",result)
