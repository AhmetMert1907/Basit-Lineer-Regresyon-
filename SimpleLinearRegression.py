#Importing Library(Kutuphanelerin eklenmesi)
import numpy as np
import matplotlib.pyplot as plt

#Creation of data lists(veri listelerinin olusturulmasi)
x = np.array([1,2,3,4,5])
y = np.array([1.5,0.8,1.7,3.8,7.6])

#Make a single array(Tek bir dizi yapar)
B = np.vstack([x,np.ones(len(x))]).T
             
#finds m and c in function(mx+c=y fonksiyonundaki m ve c yi bulur) 
m , c = np.linalg.lstsq(B,y)[0]

#finally , to see what I'm doing in the chart(son olarak , grafikte ne yaptigimi görebilmek icin)
plt.plot(x,y,'o', label='Orijinal veri', markersize=8)
plt.plot(x,m*x+c,'r',label='Uydurulmuş Veri')
plt.legend()
plt.show()
