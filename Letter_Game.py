



str_A=input()
ind_B=input().split()



new_A=""
new_A2=""
str_B=input()
ind_A=input().split()
new_B=""
new_B2=""


for i in  ind_B:
    new_A+=str_A[int(i)]
    
for i in str_A:
    if i not in new_A:
        new_A2+=i
        
for i in  ind_A:
    new_B+=str_B[int(i)]
    
for i in str_B:
    if i not in new_B:
        new_B2+=i

A_point=0
B_point=0
ord_A=[]
ord_B=[]

for i in new_A2:
    ord_A.append(ord(i))
    
for j in new_B2:
    ord_B.append(ord(j))
    
    
for i in range(len(ord_A)):
    if ord_A[i]>ord_B[i]:
        A_point+=(ord_A[i]-ord_B[i])
    if ord_A[i]<ord_B[i]:
        B_point+=(ord_B[i]-ord_A[i])
        
result=dict(A=A_point,B=B_point)

print(result)    