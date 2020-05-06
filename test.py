path='/Users/sakai/scikit_learn_data/20news-bydate/matlab/news20.t'
#alt.atheism of:7 and:3 other:1 are:7 the:19

path2='/Users/sakai/scikit_learn_data/20news-bydate/matlab/word_freq_DF_news20_all'
#crystal:79:55
#trip:147:117
#largely:115:101

wordlist = []

with open(path2) as f2:
    for line2 in f2:
        line2 = line2.rstrip()
        temp2 = line2.split(':')
        wordlist.append(temp2[0])
        

with open(path) as f:
    for line in f:
        line = line.rstrip()
        temp = line.split()
        print(temp[0],end='')
        print(' ',end='')
        for wfreq in temp[1:]:
            w,count = wfreq.split(':')
            for wl in wordlist:
                if(w == wl):
                    print(w,end='')
                    print(':',end='')
                    print(count,end='')
                    print(' ',end='')
        print()

                        