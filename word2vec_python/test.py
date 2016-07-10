#coding=utf-8

print 'dsf'
import multiprocessing
import logging,os,gensim
from gensim.models.word2vec import LineSentence
# class MySentences(object):
#      def __init__(self, dirname):
#          self.dirname = dirname
#  
#      def __iter__(self):
#         for fname in os.listdir(self.dirname):
#             for line in open(os.path.join(self.dirname, fname)):
#                 yield line.split()

def MySentences(filepath):
    f=open(filepath)
    lines=f.readlines()
    f.close()
    return lines     

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# sentences=MySentences(r'/home/min/Myfiles/resaerchs/nlp/HanLP/data/dictionary/custom/上海地名.txt')
# #sentences=LineSentence(r'/home/min/Myfiles/resaerchs/nlp/HanLP/data/dictionary/custom/上海地名.txt')
# model = gensim.models.Word2Vec(size=400, window=5, min_count=5,workers=multiprocessing.cpu_count())
# model.build_vocab(sentences)
# model.train(sentences)
# model.save("base_model")
 
model = gensim.models.Word2Vec.load('/home/min/workspace/MyJava/w2v/trunk/vectors.bin')
# print model.similarity('丁夏', '丁夏村')
print model.vector_size#400维
#KeyError: '\xe4\xb8\x81\xe5\xa4\x8f'

print '\xe4\xb8\x81\xe5\xa4\x8f'
