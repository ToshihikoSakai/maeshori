from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn import datasets
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import collections
import sys

args = sys.argv


#全てのデータをとってくる
#data = datasets.fetch_20newsgroups(subset='all',categories=['alt.atheism'])
data = datasets.fetch_20newsgroups(subset='all',categories=[args[1]])
#data = datasets.fetch_20newsgroups(subset='all')

#文を渡すと前処理後の単語(13413個)を含む単語リストを返す関数
#入力：文
#sentence = 'This is a sample sentence, showing off the stop words filtration.'
#出力:前処理後の単語のリスト
#  ['adam','clinton',....'good']
def maeshori(sentence):
        
    #NLTKのtokenizeで英文の単語分割
    word_tokens = word_tokenize(sentence)
    filtered_sentence = []
    
    for w in word_tokens:
        
        #アルファベットの小文字化 w.lower()    
        w = w.lower()
        
        for maew in maeshoriwords:
            if(w == maew):
                w = w.strip()
                print(w,end="")
                print(' ',end='')
        

path='/Users/sakai/scikit_learn_data/20news-bydate/matlab/word_freq_DF_news20_all'

maeshoriwords = [] #前処理後の単語リスト

#全てのデータをとってくる
with open(path) as f:
    for line in f:
        line = line.strip()
        temp = line.split(':')
        maeshoriwords.append(temp[0])
        
    
for num in range(0,data.target.shape[0],1):
    print(data.target_names[data.target[num]],end='')
    print(' ',end='')
    
    sen = data.data[num]
    
    #senの中身
    #From: will@futon.webo.dg.com (Will Taber)
    #Subject: [soc.religion.christian] Re: The arrogance of Christians
    #Lines: 50
    #In a previous message  aa888@freenet.carleton.ca (Mark Baker) writes:
    #print(sen)
    maeshori(sen)
    print() #改行
    



    
