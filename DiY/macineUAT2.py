import numpy as np
import pandas as pa
from  sklearn.preprocessing import StandardScaler#

from sklearn.feature_extraction.text import  CountVectorizer,TfidfVectorizer
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
import jieba;
import csv;
import time;
def getFenci(x):
    document=[]
    for line in x :
        sent_words = [list(jieba.cut(sent0)) for sent0 in line]
        doc = [" ".join(sent0) for sent0 in sent_words]
        document.append(doc[0]);
        print(line);
    return document
#分类文本
def machine():
    #导入数据
    # 数据不是真实数据，自己定义的，真实数据需要采集
    # 鼠标往右拖动距离 x,分为前中后三段记录，鼠标上下移动距离 y，分为前中后三段，time是总耗时，machine为标签字段，0为人，1为机器
    #x-front x-middle	x-back	y-front	y-middle	y-back	time	machine
    dataset=pa.read_csv('machine-uat2.csv')
    x=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values
    x=getFenci(x);
    #拆分训练集测试集,10%测试，90%训练
    trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.1,random_state=0)
    print('测试集',testx,testy)
    #归一化
    # tokenizer参数是用来对文本进行分词的函数（就是上面我们结巴分词）
    count_vect = CountVectorizer(  )
    scaler=TfidfVectorizer()
    trainx=scaler.fit_transform(trainx)
    joblib.dump(scaler, 'machine-uat-scaler.m')
    testx=scaler.transform(testx)
    #支持向量机训练
    # classfier=SVC(kernel='rbf',random_state=0)
    # classfier.fit(trainx, trainy)
    #朴素贝叶斯
    classfier= MultinomialNB().fit(trainx,trainy)
    #保存训练好模型
    joblib.dump(classfier,'machine-uat.m')
    # classifier2=joblib.load('machine-uat.m')
    #预测
    predity=classfier.predict(testx)
    print('测试结果',predity)
    #生产报告
    report=classification_report(testy,predity)
    print (report)
def predictUseMode():
    classifier2 = joblib.load('D:\MyData\zhouly2\PycharmProjects\machine\DiY\machine-uat.m')
    scaler2 = joblib.load('D:\MyData\zhouly2\PycharmProjects\machine\DiY\machine-uat-scaler.m')
    times=time.strftime("%Y%m%d")
    filename='D:/MyData/zhouly2/Downloads/'+times+'log.csv'
    filename1='D:/MyData/zhouly2/Downloads/'+times+'log分类.csv'
    dataset=pa.read_csv(filename)
    start=dataset.iloc[:,0:7].values
    x=dataset.iloc[:,2:3].values
    print(x)
    x=getFenci(x);
    print(x)
    #拆分训练集测试集,10%测试，90%训练
    #归一化
    scaler = scaler2;
    trainx=scaler.transform(x)
    predity = classifier2.predict(trainx)
    print(predity)
    result = np.c_[start, predity]
    #写入文件
    f = open(filename, 'r')
    out = open(filename1, 'a',newline='')
    csv_write = csv.writer(out, dialect='excel')
    for x in result:
        csv_write.writerow(x)
    f.close()
    out.close()
if __name__=='__main__':
    # machine()
    predictUseMode()