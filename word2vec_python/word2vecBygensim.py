#coding=utf-8

from gensim.models import word2vec
import gensim,logging,os
from twisted.python.test.test_sendmsg import WorseList
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

#english
# sentences = word2vec.Text8Corpus(r'E:\MyEclipseWorks\MyPython\data\word2vec\text8')
# model = word2vec.Word2Vec(sentences, size=200,workers=1)
# model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
# model.save('/tmp/text8.model')
# model.save_word2vec_format('/tmp/text8.model.bin', binary=True)
# model = word2vec.Word2Vec.load_word2vec_format('/tmp/vectors.bin', binary=True)
# model.most_similar(['girl', 'father'], ['boy'], topn=3)
# 
# more_examples = ["he his she", "big bigger bad", "going went being"]
# for example in more_examples:
#     a, b, x = example.split()
#     predicted = model.most_similar([x, b], [a])[0][0]
#     print "'%s' is to '%s' as '%s' is to '%s'" % (a, b, x, predicted)


#chinese 1
# sentences = word2vec.Text8Corpus(r'E:\MyEclipseWorks\MyPython\data\word2vec\train.txt')
# model = word2vec.Word2Vec(sentences, size=200,workers=1)
# print model.most_similar(positive=['花果山', '荒山'], negative=['高中'], topn=1)
# model.save('/tmp/text8.model')
# model.save_word2vec_format('/tmp/text8.model.bin', binary=False)
# model = word2vec.Word2Vec.load_word2vec_format('/tmp/vectors.bin', binary=False)
# print model.most_similar('政府','部门')

#chinese 2

def trainMyW2V_2(trainfile,modelfile,vocabfile):
    '''
    trainfile,data set for train word2vec
    modelfile,save w2v model
    vocabfile,save w2v vocab
    '''
    model = gensim.models.Word2Vec(size=200,min_count=5)
    #gensim.models.Word2Vec(sentences, size, alpha, window, min_count, max_vocab_size, sample, seed, workers, min_alpha, sg, hs, negative, cbow_mean, hashfxn, iter, null_word, trim_rule, sorted_vocab, batch_words)
    sentences = gensim.models.word2vec.LineSentence(trainfile)
    #train dataSet must add more
    model.build_vocab(sentences)
    model.train(sentences)
    #judge files exits?
    if(os.path.exists(modelfile)):
        print 'model file is exit,remove old file'
        os.remove(modelfile)
    if(os.path.exists(vocabfile)):
        print 'vocab file is exit,remove old file'
        os.remove(vocabfile)
    model.save_word2vec_format(modelfile, binary=False)
    #put vocab into txt,for filter
    words=model.vocab.keys()
    #write to txt
    f=open(vocabfile,'w')
    for word in words:
        f.write(word.encode('UTF-8')+',')
    f.close()
    

#load model
# model = word2vec.Word2Vec.load_word2vec_format('/home/min/workspace/MyPython/word2vec_python/models/mytrain.model.bin', binary=False)
# 
# print len(model.vocab)
# 
# print model.similarity(u'楼盘', u'房产')
#  
# print model.similarity(u'地段', u'房产')

# print model.similarity(u'华园交通图', u'之后小区')

trainMyW2V_2(r'/home/min/workspace/MyJava/my_w2v_train615.txt','/home/min/workspace/MyPython/word2vec_python/models/mytrain.model.bin','vocab.txt')


