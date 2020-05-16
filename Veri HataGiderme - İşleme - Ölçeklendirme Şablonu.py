import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer  
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler 
from sklearn.model_selection import train_test_split

veri = pd.read_csv("eksikveriler.csv")
imputer = SimpleImputer(missing_values=np.NaN,strategy="mean")

Yas = veri.iloc[:,1:4].values 
imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
ulke = veri.iloc[:,0:1].values  #0:1 yerine sadece 0 yazınca error veriyor

#Encoder --> Nominal,Ordinal --> Numeric 
le =LabelEncoder()
ulke[:,0] = le.fit_transform(ulke[:,0]) 


ohe = OneHotEncoder(categories ="auto")
ulke=ohe.fit_transform(ulke).toarray()

#Numpy Dizileri DataFrame Dönüşümü
sonuc = pd.DataFrame(data = ulke,index=range(22),columns=['fr','tr','usa'])  
sonuc2=pd.DataFrame(data = Yas,index=range(22),columns=['Boy','Kilo','Yas'])
cinsiyet = veri.iloc[:,-1].values
sonuc3 = pd.DataFrame(data = cinsiyet,index=range(22),columns = ['Cinsiyet'])

#DataFrame Birleştirme İşlemi
s=pd.concat([sonuc,sonuc2],axis=1)
s2= pd.concat([s,sonuc3],axis=1)

#Verilerin Eğitim ve Test olarak bölünmesi
x_train,x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33,random_state = 0)

#Verilerin Ölçeklendirilmesi
sc = StandardScaler()
X_train = sc.fit_transform(x_train)  
X_test = sc.fit_transform(x_test)