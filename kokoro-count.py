from janome.tokenizer import Tokenizer
import zipfile
import os.path, urllib.request as req

url = "https://www.aozora.gr.jp/cards/000148/files/773_ruby_5968.zip"
local = "773_ruby_5968.zip"
if not os.path.exists(local):
    print("ZIPファイルをダウンロード")
    req.urlretrieve(url, local)

# zipファイル内のテキスト読み込む
zf = zipfile.ZipFile(local, 'r')
fp = zf.open('kokoro.txt', 'r')
bindata = fp.read()
txt = bindata.decode('shift_jis')

# 形態素解析オブジェクト
t = Tokenizer()

# テキストの処理
word_dic = {}
lines = txt.split("\r\n")
for line in lines:
    malist = t.tokenize(line)
    for w in malist:
        word = w.surface
        ps = w.part_of_speech
        if ps.find('名詞') < 0: continue
        if not word in word_dic:
            word_dic[word] = 0
        word_dic[word] += 1

keys = sorted(word_dic.items(), key = lambda x:x[1], reverse=True)
for word, cnt in keys[:50]:
    print("{0}({1})".format(word, cnt), end="")