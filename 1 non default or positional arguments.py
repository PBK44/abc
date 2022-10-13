#non-default arguments or positional argument

#1
def display(name,age):
    print(name,age)
display("vishnu",2) 


#2 
def avg(x,y,z):                 #with arguments
    avg=(x+y+z)/3.0
    print("AVERAGE=",avg)       #without return type
avg(10,20,30)    


#3
def avg(n1,n2,n3):              #with arguments
    avg=(n1+n2+n3)/3.0
    return avg                  #with return type
r=avg(10,20,60)
print("average=",r)


#4
def avg(n1,n2,n3):             #with arguments
    return (n1+n2+n3)/3.0      #with return type
r1=avg(1,2,3)
r2=avg(4,5,6)
r3=avg(7,8,9)
print(r1)
print(r2)
print(r3)

#5
def avg(n1,n2,n3):
    return (n1+n2+n3)/3.0
num1=int(input("Enter num1 value:"))
num2=int(input("Enter num2 value:"))
num3=int(input("Enter num3 value:"))

print(avg(num1,num2,num3))


#6
def my_function(x):
    return 5*x
print(my_function(5))
print(my_function(6))
print(my_function(7))


#7
def my_function(fname):
    print(fname+"hi")
my_function("brahma")
my_function("kumar")
my_function("vishnu")


#8
def my_function(fname,lname):
    print(fname+" "+lname)
my_function("brahma","kumar")    

#9 Passing a list as an arguments
def my_function(food):
    print(food)       # it print as alist
    #or u want differently
    for i in food:
        print(i)
fruits=["apple","banana","pomegranate","sapota"]        
my_function(fruits)        







