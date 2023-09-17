# 1
print("Q1")
age1=int(input("Entrer your age:"))
age2=int(input("Entrer your age:"))
sum=age1+age2
print("Sum of the ages are:", sum)

#2
print("\n")
print("Q2")
no1=int(input("Enter a number:"))
no2=int(input("Enter a number:"))
no3=int(input("Enter a number:"))
mean=(no1+no2+no3)/3
print("Mean of the 3 numbers is", mean)

#3
print("\n")
print("Q3")
L=int(input("Enter the lenght of the cuboid:"))
B=int(input("Enter the breadth of the cuboid:"))
H=int(input("Enter the height of the cuboid:"))
volume=(L*B*H)
print("Volune:",volume)

#4
print("\n")
print("Q4")
n=int(input("Enter the number of sum of natural numbers you want:"))
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)

#5 
print("\n")
print("Q5")
no1=int(input("Enter a number:"))
no2=int(input("Enter a number:"))

small=0
if no1>no2:
    small=no2
elif no1<no2:
    small=no1
elif no1==no2:
    hcf=no1
for i in range(1,small+1):
    if no1%i==0 and no2%i==0:
        hcf=i

print("HCF is:",hcf)

#6
print("\n")
print("Q6")
def factorial():
    n=int(input("Enter the number of which factorial you want:"))
    sum=1
    for i in range(1,n+1):
        sum*=i
    print(sum)
factorial()

#7
print("\n")
print("Q7")
list1=[3,4,5,34,4,43,43,4,53,2,4,5,6,7,8,4,53,23,5,2,6,6,545]
d={}
for i in list1:
  if i in d:
    d[i]+=1
  else:
    d[i]=1
print(d)

#8
print("\n")
print("Q8")
n=int(input("Enter number of * rows you want:"))
for i in range(0,n+1):
    for j in range(0,i):
        print("*", end=' ')
    print('\n')
