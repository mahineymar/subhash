num1=int(input())
l=list(map(int,input().split()))
num2=[]
num3=1
for x in range(num1):
	val=l[i:]
	ans=len(val)
	for y in range(ans-1):
		if val[y]>0 and val[y+1]<0:
			num3=num3+1
		elif val[y]<0 and val[y+1]>0:
			num3=num3+1
		else:
			break
	num2.append(str(num3))
	num3=1
print(" ".join(num2))
