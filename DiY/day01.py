import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.cross_validation import  train_test_split
from sklearn.preprocessing import StandardScaler
def readFile():
    dataset=pd.read_csv('D:/MyData/zhouly2/Desktop/test.csv');
    X = dataset.iloc[:, :-1].values
    Y = dataset.iloc[:, 3].values

    print ( Y )

def makeMiss():
    dataset=pd.read_csv('D:/MyData/zhouly2/Desktop/test.csv');
    X = dataset.iloc[:, :-1].values
    Y = dataset.iloc[:, 3].values
    #补充缺失的数据
    impute=Imputer(missing_values="NaN", strategy= "mean" ,axis=0)
    impute=impute.fit(X[:,1:3])
    X[:, 1:3] = impute.transform(X[:, 1:3])
    print(X)
    #将这个英文列变为了数字
    labelencoder_x=LabelEncoder()
    X[:,0] = labelencoder_x.fit_transform(X[:,0])
    labekencoder_y=LabelEncoder()
    Y  = labekencoder_y.fit_transform(Y )
    #创建虚拟变量?
    onehotencoder=OneHotEncoder(categorical_features=[0])
    X =onehotencoder.fit_transform(X).toarray()
    print(X)
    #拆分训练集
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
    print(X_train, X_test,Y_train,Y_test)
    print('----------------')
    #特征标准化，归一化
    sc_x=StandardScaler()
    X_train=sc_x.fit_transform(X_train)
    X_test=sc_x.fit_transform(X_test)
    print(X_train,X_test)



if __name__ == '__main__':
    makeMiss()
