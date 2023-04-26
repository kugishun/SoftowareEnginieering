def goukei(sum,id):
    sum += id
    return sum

f = open('id.txt','r')
sum = 0
datalist = f.readlines()
for data in datalist:
    sum = goukei(sum,int(data))
f.close()
f = open('result.txt','w')
f.write(str(sum))
f.close()

