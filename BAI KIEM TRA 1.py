n=input("nhap vao cac so:").split(',')
file = open ('tuananh.txt','a')
dem=0
for i in n:
    a=int(i)
    if a%2==0:
        dem+=1
        file.write(str(a))
print("so cac so chan la:",(dem))
file.close