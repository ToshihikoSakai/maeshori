# 概要
20news-bydate-matlab.tgzの前処理を実施
以下の前処理を実施
* stopwordsを除外
* アルファベット以外を除外
* アルファベットを小文字に統一
* 文書群での総出現回数が20回以下の単語及び全体の30%以上の文書に出現する単語の除外

単語集合の作成
* カテゴリ単語順序対集合の作成

# 利用しているデータ
20newsgroup datasetsの20news-bydate-matlab.tgzをとってくる

```bash
wget http://qwone.com/~jason/20Newsgroups/20news-bydate-matlab.tgz
```
今回はダウンロード済みのものをdataディレクトリに格納済み。

# データの加工
```bash
python3 datatoarrange.py
```
上記を実行するとnews20とnews20.tが作成される。
プログラムはhttp://aidiary.hatenablog.com/entry/20100618/1276877116　を参考。
news20とnews20.tの形式は以下。
alt.atheism archive:4 name:2 atheism:10 ...
comp.graphics name:1 last:1 modified:1 addresses:2 of:14 ...
talk.religion.misc of:4 and:4 other:1 are:2 the:14 in:5 ...

* news20とnews20.tを連結したファイルの作成
```bash
cat news20 news20.t > news20_all
```
すでにnews20,news20.t,news20_allを格納済み。

# 前処理の実施
```bash
python3 maeshori.py > word_freq_DF_news20_all
```
中身は以下
単語:freq:DF
crystal:79:55
trip:147:117
largely:115:101

前処理後は単語数は13413となった。この単語リストを前処理後の単語リストと呼ぶ。
```bash
wc -l word_freq_DF_news20_all 
  13413 word_freq_DF_news20_all
```

 * データから前処理後の単語リストに当てはまらないものを除外(30分くらいかかる)
 ```bash
  python3 test.py > news20_maeshori
```

# 前処理後の単語リストを基に、もともとのデータに対して前処理を実施
データ：20newsgroup datasetの各カテゴリの文書
出力：13413単語にしぼり単語を限定した文書
 ```bash
sh test.sh
```

* 全カテゴリの文書を一つのファイルにまとめる
 ```bash
cat alt.atheism.maeshori.txt comp.graphics.maeshori.txt... >  all_maeshori.txt 
 ```
 
* 18846文書から70%=13192.2なので、13193文書を学習データ、5653文書をテストデータとして準備
 ```bash
python3 random_extract.py
 ```
 all_maeshori_train.txtとall_maeshori_test.txtができる。
 
# カテゴリ単語順序対集合の作成
```bash
python3 C_create.py > category_word_set.txt
 ```
例） alt.atheism subject alt.atheism visit alt.atheism jehovah alt.atheism witnesses alt.atheism lippard alt.atheism james alt.atheism
 
* corporaのfileter_extremes関数を使ってみた
 結果、11466単語となった ファイル名：dic.py
 ```bash
 python3 dic.py
 head dic.txt 
 18846
 514	a	3975
 2083	aa	249
 2872	aaa	49
 ```
