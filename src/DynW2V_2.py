'''
Dynamic Word2Vec example
by Chengbin Hou
ref: https://rutumulkar.com/blog/2015/word2vec and https://radimrehurek.com/gensim/models/word2vec.html
'''

import gensim
import logging
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]

w2v = gensim.models.Word2Vec(size=5, window=2, sg=1, hs=0, negative=1, ns_exponent=1.0,
                            alpha=0.025, min_alpha=0.0001, min_count=1, sample=0.001, iter=5, workers=4, seed=2019,
                            sentences=None, corpus_file=None, sorted_vocab=1, batch_words=10000, compute_loss=False,
                            max_vocab_size=None, max_final_vocab=None, trim_rule=None)

w2v.build_vocab(sentences=sentences, update=False)
w2v.train(sentences=sentences,total_examples=w2v.corpus_count, epochs=w2v.iter)

print('emb for cat ---v1 ', w2v.wv['cat'])

import pickle
myw2v = pickle.dumps(w2v)
del w2v
w2v = pickle.loads(myw2v)


sentences = [["a", "b", "say","cat","say","say","cat","cat","say","cat","cat","cat","cat","b","b","a", "cat","cat","b","b","b","cat","b", "say","cat","say","a", ]]
w2v.build_vocab(sentences=sentences, update=True)
# print('emb for queen --- inti', w2v.wv['queen'])



w2v.train(sentences=sentences,total_examples=w2v.corpus_count, epochs=w2v.iter)
print('emb for cat ---v1 ', w2v.wv['cat'])

sentences = [["a", "cat","cat","b","b","b","cat","b", "say","cat","say","a", "b", "say","cat","say","a", "cat","b", "say","cat","cat","cat","hcb","say","cat","cat","cat","cat","b","b"]]
w2v.build_vocab(sentences=sentences, update=True)
# print('emb for queen --- inti', w2v.wv['queen'])



w2v.train(sentences=sentences,total_examples=w2v.corpus_count, epochs=w2v.iter)
print('emb for cat ---v1 ', w2v.wv['cat'])
# 试试相似度变化大不大
# 怎么自己来重置某一个向量；或者不充值继续训练？
# 看看他的update那个到底做了什么


'''
sentences = [["a", "b", "say"],["a", "cat","b","b"],["a", "b", "say","cat","b","b"]]
w2v.build_vocab(sentences=sentences, update=True)
# print('emb for queen --- inti', w2v.wv['queen'])

w2v.train(sentences=sentences,total_examples=w2v.corpus_count, epochs=w2v.iter)
print('emb for cat ---v1 ', w2v.wv['cat'])
print('emb for say ---v1 ', w2v.wv['say'])
print('emb for a ---v1 ', w2v.wv['a'])
print('emb for b ---v1 ', w2v.wv['b'])
'''
