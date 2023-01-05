import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
path = os.path.abspath('reading books')
df = pd.read_csv(path+'/������_1.csv', index_col=0, parse_dates=['Date'])
df

flg=plt.figure(flgsize=(20,8))
ax = flg.add_subplot(111)

ax.plot(df.index, df['13~19��'], label='13~19��')
ax.plot(df.index, df['15~19��'], label='15~19��')
ax.plot(df.index, df['20~29��'], label='20~29��')
ax.plot(df.index, df['30~39��'], label='30~39��')

ax.plot(df.index, df['40~49��'], label='40~49��')
ax.plot(df.index, df['50~59��'], label='50~59��')
ax.plot(df.index, df['60~69��'], label='60~69��')
ax.plot(df.index, df['70~79��'], label='70~79��')

ax.plot(df.index, df['80�� �̻�'], label='80�� �̻�')

ax.set_title('���ɺ� ������')
ax.set_ylabel('���ɴ�')
ax.set_xlabel('�⵵')

ax.legend()
plt.show()