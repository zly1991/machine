import sklearn.datasets  as ge
import sklearn.preprocessing as po
#生成样本
def make():
  x,y=  ge.make_classification(n_samples=6, n_features=5, n_informative=2,
    n_redundant=2, n_classes=2, n_clusters_per_class=2, scale=1.0,
    random_state=20)
  # print(x)
  # print(y)
  return x,y

def laodbos():
   bos= ge.load_boston()
   print(bos.data.shape)

#归一化
def transform():
    x,y=make()
    scaler = po.StandardScaler().fit(x)
    scaler.transform(x)
    print (scaler  );
#正则化
def regular():
    data = [[0, 0, 3], [1, 1, 0], [0, 2, 1], [1, 0, 2]]
    encoder = po.OneHotEncoder().fit(data)
    print(encoder.transform(data).toarray())

if __name__ == '__main__':
    # make()
    # laodbos()
    # transform()
    regular()