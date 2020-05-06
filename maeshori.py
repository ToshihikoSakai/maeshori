from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn import datasets
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import collections
from collections import defaultdict

#stopwords
stop_words = set(stopwords.words("english"))
#print(stop_words)

path='/Users/sakai/scikit_learn_data/20news-bydate/matlab/news20_all'

words = set() #単語集合
categories = set() #カテゴリ集合
wordcount = {}         # wordcount[cat][word] カテゴリでの単語の出現回数
catcount = {}          # catcount[cat] カテゴリの出現回数
wordcount_all = {}  #wordcount[word]　全文書での単語の出現回数

lineword = [] #行ごとの単語 ['from','to',....]
wordlist = [] #文書ごとの単語リスト[['from','to',..]]



#全てのデータをとってくる
with open(path) as f:
    for line in f:
        #print(line)
        line = line.rstrip()
        temp = line.split()
        cat = temp[0]
        categories.add(cat)
        for wfreq in temp[1:]:
            w = wfreq.split(':')
            w = w[0].strip()
            if(w not in stop_words):            
                words.add(w)
                

for w in words:
    wordcount_all[w] = 0
                

for cat in categories:
    wordcount[cat] = defaultdict(int)
    catcount[cat] = 0
        
with open(path) as f:
    for line in f:
        line = line.rstrip()
        temp = line.split()
        cat = temp[0]
        catcount[cat]+=1
        for wfreq in temp[1:]:
            word,count = wfreq.split(':')
            word = word.strip()

            count = int(count)
            #print('word=',word)
            #print('count=',count)
            #print('type(count)=',type(count))
            if(word not in stop_words):
                lineword.append(word)
                wordcount[cat][word] += count
                wordcount_all[word] += count
                #print('wordcount',cat,word,wordcount[cat][word])
        wordlist.append(lineword)
        lineword = []
                
    
#nouns = [['ブドウ','バナナ'],
#        ['レモン','レモン','バナナ','ブドウ'],
#        ['ブドウ']]
def tfdf(nouns):
    tfs = [] # 記事毎のリスト。リスト要素は記事内の単語毎のtf値
    dfs = {} # 単語毎のdf値
    for idx,doc in enumerate(nouns): # idx=記事番号
        tf = {}
        for term in doc:
            TERM_CNT = len(doc) # 記事内の単語数

            # （記事内の）単語毎のtf値
            if term not in tf:
                tf[term] = 0
            tf[term] += 1 / TERM_CNT # コード短縮のため、割り込むと同時に足す

            # 単語毎のdf値
            if term not in dfs:
                dfs[term] = set()
            dfs[term].add(idx) # 集合(set)で記事番号(idx)を保持

        tfs.append(tf)

    # 記事番号の集合の大きさ＝出現数
    for term,doc_set in dfs.items():
        dfs[term] = len(doc_set)


    #print('tfs:',tfs)
    #print('dfs:',dfs)
    return dfs

dfs = tfdf(wordlist)
#print(dfs)
#{'from': 799, 'acooper': 22, 'macccmacalstredu': 22, 'turin': 13, 'turambar': 13, 'me': 18,....}

#print('len(wordlist)=',len(wordlist))
#18774

#30%以上のDF値をもつ単語は除外
keys = [k for k,v in dfs.items() if v < int(len(wordlist)*30/100)]

#全文書での20回以上の出現頻度の単語
tf20over = []

#全文書での20回以上の出現頻度の単語
for w in words:
    if wordcount_all[w] > 20:
        tf20over.append(w) 

#文書全体30%未満のDF値をもつ単語　かつ　全文書での20回以上の出現頻度の単語
new_words = set(keys) & set(tf20over)


#出力イメージ    
#archives:178:92
#wuarchive:89:55
#archive:497:200
#archived:47:30
for w in new_words:
    print(w,end='')
    print(':',end='')
    print(wordcount_all[w],end='')
    print(':',end='')
    print(dfs[w])

'''
for cat in categories:
    if(cat == 'alt.atheism'):
        print(cat)
        for w in new_words:
            if(wordcount[cat][w] != 0):
                print(w,end='')
                print(':',end='')
                print(wordcount[cat][w])
    
'''