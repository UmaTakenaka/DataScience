from janome.tokenizer import Tokenizer
from gensim.models import word2vec
import re

# テキストファイル読み込み
bindata = open('kokoro.txt.sjis','rb').read()
text = bindata.decode('shift_jis')[0]

# テキストのヘッダ・フッタ削除
text = re.split(r'\-{5,}',text)[2]
text = re.split(r'底本：', text)[0]
text = text.strip()

# 形態素解析
t = Tokenizer()
results = []
lines = text.split('\r\n')
for line in lines:
    s = line
    s = s.replece('|', '')
    s = re.sub(r'《.+?》', '',s)
    s = re.sub(r'[# .+?]', '', s)
    tokens = t.tokenize(s)
    r = []
    for tok in tokens:
        if tok.base_form == "*":
            w = tok.surface
        else:
            w = tok.base_form
        ps = tok.part_of_speech
        hinshi = ps.split(',')[0]
        if hinshi in ['名詞', '形容詞', '動詞', '記号']:
            r.append(w)
    
    r1 = (" ".join(r)).strip()
    results.append(r1)

# ファイルに書き込む
wakati_file = 'kokoro.wakati'
with open(wakati_file, 'w', encoding='utf-8') as fp:
    fp.write("\n".join(results))

# word2vecでモデル作成
data = word2vec.LineSentence(wakati_file)
model = word2vec.Word2Vec(data, size=200, window=10, hs=1, min_count=2, sg=1)
model.save('kokoro.model')
print('ok')