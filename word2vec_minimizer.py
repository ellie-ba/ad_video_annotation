import gensim
from gensim.scripts.glove2word2vec import glove2word2vec

glove2word2vec("./data/word2vec/glove.6B.300d.txt", "./data/word2vec/word2vec.6B.300d.txt")
model = gensim.models.KeyedVectors.load_word2vec_format("./data/word2vec/word2vec.6B.300d.txt")

model.save_word2vec_format("./data/word2vec/word2vec.6B.300d.bin", binary=True)

print(model.similarity("hello", "hi"))
