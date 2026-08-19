import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# 한글 폰트 설정
import platform

from matplotlib import rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Linux':
    rc('font', family = 'NanumGothic')  # 또는 '나눔고딕'
    print('Linux system... font set to NanumGothic')
elif platform.system() == 'Windows':
    rc('font', family = 'Malgun Gothic')   # 또는 '맑은 고딕'
    print('Windows system... font set to Malgun Gothic')
else:
    print('Unknown system... sorry~~~~')

df = pd.read_csv('./datas/seoul.csv', encoding='cp949')

df.info
df.describe()

df["날짜"].describe()

df['최고기온(℃)'] == df['최고기온(℃)'].max()

df.loc[df['최고기온(℃)'] == df['최고기온(℃)'].max(), ]

df.sort_values('최고기온(℃)', ascending=False).head(1)

my_bins = np.arange(df['최고기온(℃)'].min(), df['최고기온(℃)'].max(), 4)

plt.hist(data=df, x='최고기온(℃)', rwidth=0.8, bins=my_bins)
plt.show()

df_2014 = df.loc[df['날짜'] >= '2014-01-01', ]

my_bins = np.arange(df_2014['최고기온(℃)'].min(), df_2014['최고기온(℃)'].max(), 4)

plt.hist(data = df_2014, x = '최고기온(℃)', rwidth=0.8, bins=my_bins)
plt.show()

plt.figure(figsize=(10,4))

plt.subplot(1,2,1)
my_bins = np.arange(df['최고기온(℃)'].min(), df['최고기온(℃)'].max(), 4)
plt.hist(data=df, x='최고기온(℃)', rwidth=0.8, bins=my_bins)

plt.subplot(1,2,2)
my_bins = np.arange(df_2014['최고기온(℃)'].min(), df_2014['최고기온(℃)'].max(), 4)
plt.hist(data = df_2014, x = '최고기온(℃)', rwidth=0.8, bins=my_bins)

plt.show()

(df['날짜'] >= '2017-08-01') & (df['날짜'] <= '2017-08-15')
df_2017_08 = df.loc[(df['날짜'] >= '2017-08-01') & (df['날짜'] <= '2017-08-15'), ]
df_2017_08

plt.scatter(data=df_2017_08, x='날짜', y='최고기온(℃)')
plt.xticks(rotation = 60)
plt.show()

# ----------------------------------------------------------

df = pd.read_csv('./datas/subwayfee.csv', encoding='cp949')
df
df.info()
df.describe()
df.shape
df['사용월'].unique()
df['호선명'].unique()
df['역ID'].unique()
df['지하철역'].unique()
df['유임승차'].unique()
df['유임하차'].unique()
df['무임승차'].unique()
df['무임하차'].unique()

df['지하철역'].value_counts()
df_seoul = df.loc[df['지하철역'] == '서울역', ]
df_seoul

df.loc[df['유임승차'] == df['유임승차'].max(), ]
df.sort_values('유임승차', ascending=False).head(1)

df.loc[df['유임하차'] == df['유임하차'].max(), ]
df.sort_values('유임하차', ascending=False).head(1)

df.loc[df['무임승차'] == df['무임승차'].max(), ]
df.sort_values('무임승차', ascending=False).head(1)

df.loc[df['무임하차'] == df['무임하차'].max(), ]
df.sort_values('무임하차', ascending=False).head(1)

# 실습 1
df['비율'] = df['유임승차']/df['무임승차']
df.loc[df['비율'] == df['비율'].max(), ]

df_1 = df.loc[df['무임승차'] != 0, ]
df_1['비율'] = df_1['유임승차']/df_1['무임승차']
df_1.loc[df_1['비율'] == df_1['비율'].max(), ]
df_1.head(3)
df_1.sort_values("비율", ascending=False).head(1)

df_1["전체승차인원"] = df_1["유임승차"] + df_1["무임승차"]
df_over_10000 = df_1.loc[df_1['전체승차인원'] >= 10000]

df_over_10000.loc[df_over_10000['비율'] == df_over_10000['비율'].max(),]

# -----------------------------------------------------
