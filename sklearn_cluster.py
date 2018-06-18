#!"/xampp/WinPython/python-3.6.5.amd64/python.exe"
import numpy as np
import matplotlib.pyplot as plt
import mysql.connector as mariadb
import cgi

from sklearn.cluster import KMeans

fs = cgi.FieldStorage()

mariadb_connection = mariadb.connect(host='localhost', user='testuser', password='test', database='analyzedb')
cursor = mariadb_connection.cursor()

cursor.execute("SELECT cust_ctact, trx FROM bp")
x = cursor.fetchall()

mariadb_connection.close()

XA = np.array(x)

if "nb_clusters" not in fs:
  nb_clusters = 2
else:
  nb_clusters = int(fs["nb_clusters"].value)

kmeans = KMeans(n_clusters=nb_clusters, random_state=0).fit_predict(XA)

plt.scatter(XA[:,0], XA[:,1], c = kmeans)

plt.show()


print("Content-type: text/plain; charset=iso-8859-1\n")

print('[')
i=0
while i<len(kmeans) :
  if i>0:
    print(',')
  print('{"x": '+str(x[i][0])+',"y":'+str(x[i][1])+',"r": 3,"c": '+str(kmeans[i])+'}')
  i+=1

print(']')
