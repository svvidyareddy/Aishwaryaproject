print("*" * 100)
#method1
print("numbers from 1 to 100 divisible by 3 and 9")
num_div_3_9=[num for num in range(1,100) if num%3==0 and num%9==0]
print(num_div_3_9)

print("*" * 100)


#method2
num_div_3_9=[]
for num in range(1,100):
    if num%3==0 and num%9==0:
        num_div_3_9.append(num)
print("Numbers from 1-100 divisible by 3 and 9:",num_div_3_9)        

print("*" * 100)

#method3
num_div_3_9=[]
for num in range(1,100):
    if num%3==0 and num%9==0:
        num_div_3_9.append(num)
        print("Numbers from 1 - 100,divisible by 3 and 9:",num_div_3_9)
print("*" * 100)
