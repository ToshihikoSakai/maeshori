from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn import datasets
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import collections

#全てのデータをとってくる
#data = datasets.fetch_20newsgroups(subset='all',categories=['alt.atheism'])
data = datasets.fetch_20newsgroups(subset='all')


#print(data.target.shape) 
#全ての文書数
#(18846,)


#print(data.target[:10])
#[10  3 17  3  4 12  4 10 10 19]

#print(data.target_names)
#['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 'talk.politics.misc', 'talk.religion.misc']

#print(data.data[1])
#From: will@futon.webo.dg.com (Will Taber)
#Subject: [soc.religion.christian] Re: The arrogance of Christians
#Lines: 50
#In a previous message  aa888@freenet.carleton.ca (Mark Baker) writes:

#print(data.target_names[data.target[0]])
#対象データのカテゴリを出力
#comp.sys.ibm.pc.hardware

#print(data.target[0])
#3

#print(data.target_names[data.target[1]])
#対象データのカテゴリを出力
#rec.sport.hockey
#print(data.target[1])
#10


#逆瀬川さん修論の表6.1 20 newsgroups datasetsの各カテゴリの文書数
#各カテゴリの文書数をとってくる
#data = datasets.fetch_20newsgroups(subset='all',categories=['alt.atheism'])
"""
for cat in data.target_names:
    data = datasets.fetch_20newsgroups(subset='all',categories=[cat])
    print(cat,end="")
    print(data.target.shape)
"""
"""
alt.atheism(799,)
comp.graphics(973,)
comp.os.ms-windows.misc(985,)
comp.sys.ibm.pc.hardware(982,)
comp.sys.mac.hardware(963,)
comp.windows.x(988,)
misc.forsale(975,)
rec.autos(990,)
rec.motorcycles(996,)
rec.sport.baseball(994,)
rec.sport.hockey(999,)
sci.crypt(991,)
sci.electronics(984,)
sci.med(990,)
sci.space(987,)
soc.religion.christian(997,)
talk.politics.guns(910,)
talk.politics.mideast(940,)
talk.politics.misc(775,)
talk.religion.misc(628,)
"""

#stopwords
stop_words = set(stopwords.words("english"))

#文を渡すとstopwordsでフィルタしたあとの文を返す関数
#入力：文
#sentence = 'This is a sample sentence, showing off the stop words filtration.'
#出力:stopwordsでフィルタされた　かつアルファベット以外　かつ　小文字になったあとの単語のリスト
#  ['adam','clinton',....'good']
def stopsen(sentence):
    
    word_tokens = word_tokenize(sentence)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]

    for w in word_tokens:
        if w not in stop_words:
            
            #アルファベット以外の文字を削除
            w = re.sub(r'[^a-zA-Z]+',"",w)

            #''以外
            if(w != ''):
                #アルファベットの小文字化 w.lower()
                filtered_sentence.append(w.lower())

    return filtered_sentence
    
#stopwordsで除外したあとのsentense    
#print(stopsen(sentence))
#print(stopsen(data.data[1]))

#文書の全てを出力
#for w in data.target:
#    print(data.data[w])

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

    return dfs

#単語リスト
words_list = []
#DF計算用のリスト
tfdflist=[]

for sen in data.data:
    #senの中身
    #From: will@futon.webo.dg.com (Will Taber)
    #Subject: [soc.religion.christian] Re: The arrogance of Christians
    #Lines: 50
    #In a previous message  aa888@freenet.carleton.ca (Mark Baker) writes:
    sent = stopsen(sen)

    #出力:stopwordsでフィルタされた　かつアルファベット以外を除き　かつ　小文字になったあとの単語のリスト
    #['from','keith'....]
    
    #末尾に要素を追加: append()
    tfdflist.append(sent)
    #末尾に別のリストやタプルを結合（連結）: extend()
    words_list.extend(sent)

#print(tfdflist)
#[['from','keith'....],['from','kmr',...],['from','my',...],....,['from','as',...]]

dfs = tfdf(tfdflist)
#{'from': 799, 'acooper': 22, 'macccmacalstredu': 22, 'turin': 13, 'turambar': 13, 'me': 18,....}
#print(dfs)


print('文書群の総数',len(tfdflist))
#799：文書群の総数
print('単語の総数',len(dfs))
#14810：単語の総数


#30%以上のDF値をもつ単語は除外
keys = [k for k,v in dfs.items() if v < len(tfdflist)*30/100]
#print(keys)
#print('len(keys)=',len(keys))

#keysは単語リスト（30%未満の文書頻度）
#['a','b',...''d]


#単語のリストを渡し、単語の出現頻度をカウント
c = collections.Counter(words_list)
#word_listは['a','b',...''d]の総文書の総単語
#key：単語、value:出現頻度
#print(c)
#print('len(c)=',len(c))    

#出現頻度20回より多い（20回以下は除外）単語のみ出力
#https://note.nkmk.me/python-collections-counter/
#print([i[0] for i in c.items() if i[1] >= 20])
tf20over = [i[0] for i in c.items() if i[1] > 20]
#print('len(tf20over)=',len(tf20over))    
    
    
new_words = set(keys) & set(tf20over)
    
print('len(new_words)=',len(new_words))
for w in new_words:
    print(w,end='')
    print('出現頻度',c[w],end='')
    print('文書頻度(回数)',dfs[w])
