import random
f=open("all_maeshori.txt","r")
line=f.readlines()

sen=random.sample(line,13193)

train = 'all_maeshori_train.txt'
test = 'all_maeshori_test.txt'

#train用データ 13193行
with open(train,mode='w') as f:
    for s in sen:
        #print (s,end='')
        f.write(s)
        line.remove(s)

#test用データ　5653行
#train+test=合計18846行
with open(test,mode='w') as ff:
    for s in line:
        ff.write(s)
