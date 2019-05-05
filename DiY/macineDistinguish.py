import numpy as np
import pandas as pa
from  sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
#根据移动轨迹判断是否人机
def machine():
    #导入数据
    # 数据不是真实数据，自己定义的，真实数据需要采集
    # 鼠标往右拖动距离 x,分为前中后三段记录，鼠标上下移动距离 y，分为前中后三段，time是总耗时，machine为标签字段，0为人，1为机器
    #x-front x-middle	x-back	y-front	y-middle	y-back	time	machine
    dataset=pa.read_csv('machine-ren.csv')
    x=dataset.iloc[:,:-1].values
    y=dataset.iloc[:,-1].values
    #拆分训练集测试集,10%测试，90%训练
    trainx,testx,trainy,testy=train_test_split(x,y,test_size=0.1,random_state=0)
    print('测试集',testx,testy)
    #归一化
    scaler=StandardScaler()
    trainx=scaler.fit_transform(trainx)
    testx=scaler.transform(testx)
    #支持向量机训练
    classfier=SVC(kernel='rbf',random_state=0)
    classfier.fit(trainx,trainy)
    #保存训练好模型
    #joblib.dump(classfier,'machine.m')
    #classifier2=joblib.load('machine.m')
    #预测
    predity=classfier.predict(testx)
    print('测试结果',predity)
    #生产报告
    report=classification_report(testy,predity)
    print (report)

if __name__=='__main__':
    machine()