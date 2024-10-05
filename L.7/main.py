file=open("L.7/text1.txt", "r")
text=file.read()
numbers=text.split(", ")
sum=0
for i in numbers:
   integers=int(i)
   sum=sum+integers
print(sum)
print(numbers)
