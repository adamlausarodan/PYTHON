# -*- coding: utf-8 -*-
"""python for data science.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nGzom8VqWeUqarwotKHaKeXLKErxKbHR

# Import numpy dan pandas untuk pelajaran
"""

import pandas as pd
 import numpy as np

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/data/Iris.csv')

"""# Pengenalan pandas"""

df.columns

#tampilkan 5 data awal
df.head()

"""## Dataframe Slicing"""

#slicing mengambil hanya kolom spesifik
df_slicing = df[['Id', 'SepalLengthCm', 'Species']]
df_slicing.head()

#penggunan loc,nilai sebelah kanan inclusive
df_slice = df.loc[:, "SepalLengthCm":"PetalLengthCm"]
df_slice.head()

df_slice = df.loc[2:6, "SepalLengthCm":"PetalLengthCm"]
df_slice

#df.loc[slice_index, slice_columns]
df_slice = df.loc[2:6, ["SepalLengthCm","PetalLengthCm"]]
df_slice

#df.loc[slice_index, slice_columns]
df_slice = df.loc[2:6, "SepalLengthCm":"PetalLengthCm"]
df_slice

#penggunaan iloc, nilai sebuah sebelah kanan exclusive
df_slice = df.iloc[2:6, 2:4]
df_slice

df_slice = df.iloc[[2,6], [2,4]]
df_slice

"""## Agregasi"""

df.groupby('Species').mean()
#Mengelompokkan data berdasarkan kolom

#ambil hanya kolom tertentu rata-rata
df.groupby('Species').mean()[["SepalLengthCm", "PetalLengthCm"]]

"""### perbedaan np.min& np.max dengan min & max
kenapa np performa leboh baik np backend di C
dan lebih efisien
"""

#agregasi custom
df.groupby('Species').agg({"SepalLengthCm": np.min, "SepalWidthCm": np.max})

#ambil hanya kolom tertentu jumlah
df.groupby('Species').sum()[["SepalLengthCm", "PetalLengthCm"]]

#ambil hanya kolom tertentu sum&loc
df.groupby('Species').sum().loc[:"SepalLengthCm", "PetalLengthCm"]

#agregasi custom median&sum
df.groupby('Species').agg({
    "SepalLengthCm": np.median,
    "SepalWidthCm": np.sum})

df_sentosa = pd.DataFrame({
    "Species": ["Iris-setosa"],
    "attrib": [1]
})
df_sentosa

"""perbedaan join di sql dan join
'''SELECT
*
FROM df
LEFT JOIN df_sentosa
ON df.Species = df_sentosa.Species'''
"""

df_join = pd.merge(df, df_sentosa, on="Species", how="left")
df_join.head()
#kolom attrib yang dan kolom species bisa di join dan dapat nilai 1 pada setosa saja
#jika selain setoas maka akan NaN

df_join.groupby(["Species",]).sum()

df_join.groupby(["Species",]).sum()[["attrib"]]

df_join = pd.merge(df, df_sentosa, on="Species", how="left")
df_join.sample(10)

df_join = pd.merge(df, df_sentosa, on="Species", how="inner")
df_join.sample(10)

df_join = pd.merge(df, df_sentosa, on="Species", how="outer")
df_join.sample(10)

df_join = pd.merge(df, df_sentosa, on="Species", how="right")
df_join.sample(10)

import cv2
from google.colab.patches import cv2_imshow
img = cv2.imread("join.png")
cv2_imshow(img)

"""## Bonus : Contoh regresi linear"""

import statsmodels.api as sm

# convert target menjadi numerik
df_converter = pd.DataFrame({
    "Species": ["Iris-setosa", "Iris-versicolor", "Iris-virginica"],
    "Converted Species": [-1,0,1]
})
df_converter

dataset = pd.merge(df, df_converter, on="Species", how="inner")
dataset.head()
#menjoikan df_converter dengan dataset

#add constant to feature
feature = sm.add_constant(dataset.iloc[:, :4])
Species = dataset[["Converted Species"]]

# Membuat model regresi logistik
model = sm.OLS(Species, feature).fit()
# Melihat ringkasan model
print(model.summary())

import matplotlib.pyplot as plt

plt.xlabel("prediction")
plt.ylabel("actual")
plt.scatter(model.predict(feature), Species)

"""# Visualisati data dengan python

Visualisasi data mengubah informasi (data) menjadi konteks visual yang mudah dicerna oleh otak manusia

## 1.MATPOTLIB
"""

from google.colab import drive
drive.mount('/content/drive')

"""Library data visualisasi paling standart di python.Kita mulai dengan visualisasis data satu dimensi berupa python list.

Matpotlib digunakan untuk visualisasi basic,seperti linechart,bar graph,dll seperti lego,pada matpotlib nilai nilai komponen grafik seperti xlabel,ylabel,tittle perlu di definisikan satusatu melalui code
"""

import matplotlib.pyplot as plt

data = [1,1,2,3,5,8,13,21,34,55]
plt.plot(data)
plt.show()

plt.plot(data)
plt.xlabel("index")
plt.ylabel("nilai")
plt.title("plot data garis")

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/data/Iris.csv')
df.head

"""gunakan scatter plot untuk menampilkan hubungan antara dua variable"""

plt.scatter(df["SepalLengthCm"], df["SepalWidthCm"])

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
for species in df["Species"].unique():
    # Filter data berdasarkan spesies
    sub_df = df[df["Species"] == species]
    # Plot sub data pada grafik dengan label sesuai spesies
    ax.scatter(sub_df["SepalLengthCm"], sub_df["SepalWidthCm"], label=species, s=40)

# Menambahkan legenda dan label sumbu
ax.legend(title="Species")
ax.set_xlabel("SepalLengthCm")
ax.set_ylabel("SepalWidthCm")
plt.show()

df.plot(x="SepalLengthCm", y="SepalWidthCm", kind="scatter")
#df.plot(x="SepalLengthCm", y="SepalWidthCm", kind="scatter")

"""# Visualisasi dasar dengan pandas"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
colors = ["red", "green", "blue"]
species_list = df["Species"].unique()

for species, color in zip(species_list, colors):
   # Filter data berdasarkan spesies
    # argumen c = color
    # s = ukuran titik
    # ax = axis , bisa dibayangkan ini merupakan canvas tempat kita menggambarkan grafik
    #kita pastikan kalau setiap plot menggunakan canvas yang sama
    sub_df = df[df["Species"] == species]
    # Plot sub data pada grafik dengan label sesuai spesies
    sub_df.plot(x="SepalLengthCm", y="SepalWidthCm", kind="scatter", label=species, ax=ax, color=color, s=50)

"""## Histogram"""

# histogram hanya berlaku pada salah satu kolom saja
df.plot(y="SepalLengthCm", kind="hist", bins=30)

"""## Seaborn

library viasualisasi data yang user friendly dibuat default dan fokus pada data yang diplot
"""

import seaborn as sns
import pandas as pd
sns.set()#otomatis membuat syling plot

"""## Bar Graph"""

df = pd.DataFrame({
    'nama': ["Budi", "Vidi", "Cici"],
    'tinggi': [170,165,150]
})
df

#presentasi kan pada bar graph
# Membuat bar plot
sns.barplot(data=df, x="nama", y="tinggi", color="black").set(title="TINGGI")

"""## Scatter Plot"""

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('/content/drive/MyDrive/data/Iris.csv')
df.head

sns.scatterplot(data=df, x="SepalLengthCm", y="SepalWidthCm",hue="Species").set(title="scatter plot pada data iris")

#hue untuk plot kategorui berdasarkan warna
#bins menentukan jumlah bins pada histogram
sns.histplot(data=df, x="SepalLengthCm", hue="Species", bins=20).set(title="histogram pada data iris")

#hue untuk plot kategorui berdasarkan warna
#bins menentukan jumlah bins pada histogram
sns.histplot(data=df.sample(30), x="SepalLengthCm", hue="Species", bins=10).set(title="histogram pada data iris")

df_filtered = df[df["Species"].isin(['Iris-setosa', 'Iris-versicolor'])]
sns.histplot(data=df_filtered, x='SepalLengthCm', hue='Species', bins=10) # Changed data_filtered to df_filtered

df = pd.DataFrame({
    'penjualan': [10,10,20,31,53,85],
    'tahun': range(2017,2023)
})
df.head()

sns.lineplot(data=df, x="tahun", y="penjualan")

"""## Blox Plot"""

df = pd.read_csv('/content/drive/MyDrive/data/Iris.csv')
df.head()

sns.boxplot(data=df, x="Species", y="SepalLengthCm")

import numpy as np

a = np.random.random(1000)

for i,x in enumerate(a):
  print("index:", i)

  print("data:", x)

nilai_random = np.random.random(1000)

index_data_rentang46 = []
for i, data in enumerate(nilai_random):
  if 0.4<data< 0.46:
    index_data_rentang46.append(i)

nilai_random[697]