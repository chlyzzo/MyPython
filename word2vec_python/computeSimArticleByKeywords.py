#coding=utf-8
#根据计算出的word vector，计算文章的相似度
#
from gensim.models import word2vec
import numpy,operator,happybase,os
from numpy import *

#1,文章中的每个词进行相似度计算，然后取累加，求均值
#2,根据词的向量进行累加，然后均值求得文章的向量，最后根据文章的向量进行相似度计算

#2,把文章进行向量化，根据词的向量进行累加
s='卧室,居住,购房者,'


model = word2vec.Word2Vec.load_word2vec_format('/home/min/workspace/MyPython/word2vec_python/models/mytrain.model.bin', binary=False)
#get word vector

#a some key words to a vector
def KeyworsToVec(s):
    words=s.replace('\r\n','').split(',')
    docvec=numpy.zeros(model.vector_size,)
    n=len(words)
    for i in range(n):#n-1,end with , 
        docvec+=model[unicode(words[i], "utf8")]
    docvec=docvec/n
    docvec=docvec.reshape(1, len(docvec))[0]#(1,size)
    return docvec

def numpyVectToStringByWhitepace(docvec):
    #numpy (1,size)--->String Whitepace join
    res=''
    size=len(docvec)
    for i in range(size):
        if i==size-1:
            res+=str(docvec[i])
        else:
            res+=str(docvec[i])+' '
    return res

#read from file,key words to vector,and write in txt
def readDocToVec(fromfile,tofile):
    fromf=open(fromfile)
    line=fromf.readline()
    if(os.path.exists(tofile)):
        print 'model file is exit,remove old file'
        os.remove(tofile)
    while 1:
        if not line:
            break
        else:
            keyAndwords=line.split('=')
            tempvec=KeyworsToVec(keyAndwords[1])
            tof=open(tofile,'a')
            tempvec=numpyVectToStringByWhitepace(tempvec)
            tof.write(keyAndwords[0]+"="+tempvec+"\r\n")
            tof.close()
            line=fromf.readline()
    fromf.close()

#read from file,key words to vector,and write in hbase
def readDocToVecInHbase(fromfile,hostname,tablename):
    #connect the hbase,and read the table
    connection=happybase.Connection(hostname,port=9090)
    table=connection.table(tablename)
    
    fromf=open(fromfile)
    line=fromf.readline()
    
    while 1:
        if not line:
            break
        else:
            keyAndwords=line.split('=')
            rowkey=keyAndwords[0]
            tempvec=KeyworsToVec(keyAndwords[1])#numpy.ndarray
            #write to hbase
            table.put(rowkey,{"cf1:vec":str(tempvec)})
            #next line
            line=fromf.readline()
    fromf.close()

#based docvec,compute sim
def computSimByDocvec(fromfile):
    fromf=open(fromfile)
    line=fromf.readline()
    docKeyVec={}
    while 1:
        if not line:
            break
        else:
            keyAndwords=line.split('=')
            tempvec=KeyworsToVec(keyAndwords[1])
            #
            docKeyVec[keyAndwords[0]]=tempvec #add
            #
            line=fromf.readline()
    fromf.close()
    #compute sim
    keys=docKeyVec.keys()
    stand='298165'
    res={}
    for key in keys:
        if (stand!=key):
            vector1=docKeyVec.get(stand)
            vector2=docKeyVec.get(key)
            sim=dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2))            
            res[stand+":"+key]=sim
    res=sorted(res.iteritems(),key=operator.itemgetter(1))
    print res


#     
# fromfile='/home/min/workspace/MyJava/out_artid_title_filter.txt'
# tofile ='/home/min/workspace/MyJava/out_artid_title_filter_vec.txt'
# readDocToVec(fromfile,tofile)
# 
# fromfile ='/home/min/workspace/MyJava/out_artid_title_filter.txt'
# computSimByDocvec(fromfile)


# readDocToVecInHbase(fromfile,'tjtx-103-32','hwh_zx_article')

tempvec=KeyworsToVec('新房,涨幅,居,中部,省会,土地,市场,上演,年终,争夺战')#numpy.ndarray
print numpyVectToStringByWhitepace(tempvec)
# print tempvec.shape
# 新房,涨幅,居,中部,省会,土地,市场,上演,年终,争夺战
# vec=tempvec.reshape(1, len(tempvec))
# 
# print vec.shape
# 



