from sklearn.datasets import fetch_20newsgroups_vectorized
from sklearn import datasets
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import collections
from gensim.corpora import Dictionary
from gensim import corpora

#全てのデータをとってくる
#data = datasets.fetch_20newsgroups(subset='all',categories=['alt.atheism'])
data = datasets.fetch_20newsgroups(subset='all')
stop_words = set(stopwords.words("english"))
#kaisu = []

#文を渡すとstopwordsでフィルタしたあとの文を返す関数
#入力：文
#sentence = 'This is a sample sentence, showing off the stop words filtration.'
#出力:stopwordsでフィルタされた　かつアルファベット以外　かつ　小文字になったあとの単語のリスト
#  ['adam','clinton',....'good']
def stopsen(sentence):
    
    word_tokens = word_tokenize(sentence)
    filtered_sentence = []

    '''
    for w in word_tokens:
        if('.' in w):
            te = w.split('.')
            print(w,end='')
            for t in te:
                kaisu.append(t)
                word_tokens.append(t)
    '''
            
    for w in word_tokens:
        if w not in stop_words:
            
            #アルファベット以外の文字を削除
            w = re.sub(r'[^a-zA-Z]+',"",w)
            #''以外
            if(w != ''):
                #アルファベットの小文字化 w.lower()
                filtered_sentence.append(w.lower())
    
    return filtered_sentence

documents = []

for sen in data.data:
    #senの中身
    #From: will@futon.webo.dg.com (Will Taber)
    #Subject: [soc.religion.christian] Re: The arrogance of Christians
    sent = stopsen(sen)
    #末尾に要素を追加: append()
    documents.append(sent)
    
    
dic = corpora.Dictionary(documents)
# 「出現頻度が21未満の単語(20回以下)」と「30%以上の文書で出現する単語」を排除
dic.filter_extremes(no_below = 21, no_above = 0.3)

#文書データの前処理の単語の種類
print(len(dic))

#print(len(kaisu))

dic.save_as_text('dic.txt')

