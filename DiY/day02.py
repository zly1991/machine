import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
#导入线性回归
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as pt
def readFile():
    dataset=pd.read_csv("studentscores.csv");
    x=dataset.iloc[:,:1].values
    y=dataset.iloc[:,1].values
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=0)
    regression= LinearRegression()
    regression.fit(x_train,y_train)
    y_predit=regression.predict(x_test)
    #训练好了后画图
    pt.scatter(x_train,y_train,color='red')
    pt.plot(x_train,regression.predict(x_train),color='blue')

    pt.scatter(x_test,y_test ,color='orange')
    pt.plot(x_test,y_predit,color='green')
    print(y_test,y_predit)
    pt.show()

if __name__ == '__main__':

    readFile()
