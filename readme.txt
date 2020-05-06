・もともとのデータ
test.data
test.label
test.map
train.label
train.data
train.map
vocabulary.txt

・データを加工
datatoarrange.py
news20
news20.t
・news20とnews20.tを連結したファイル
#cat news20 news20.t > news20_all
news20_all

・news20のhead部分のみ抽出
#head news20 > new20_head
new20_head 

・前処理を行うプログラム
maeshori.py
#python3 maeshori.py > word_freq_DF_news20_all
#単語:freq:DF
#crystal:79:55
word_freq_DF_news20_all

#単語の頻度のみ
word_freq_news20_all

・加工データを前処理した後のファイル
#python3 test.py > news20_maeshori
test.py
#学習データの前処理
news20_maeshori
#テストデータの前処理
#python3 test.py > news20.t_maeshori


