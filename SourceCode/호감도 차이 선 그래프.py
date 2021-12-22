#호감도 차이 선 그래프

import matplotlib
import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform
df = pd.DataFrame()
print(platform.system()) # 플랫폼 확인
# Window
    
if platform.system() == 'Windows':
     matplotlib.rc('font', family='Malgun Gothic')

elif platform.system() == 'Darwin': # Mac
     matplotlib.rc('font', family='AppleGothic')

else: #linux
    matplotlib.rc('font', family='NanumGothic')

# 그래프에 마이너스 표시가 되도록 변경
matplotlib.rcParams['axes.unicode_minus'] = False

#지역
df['area'] = ['진에어','플라이강원','티웨이항공','에어부산','제주항공','아시아나항공','대한항공','에어서울','이스타항공']

df['count'] =[15.54,11.98,9.46,8.59,4.95,3.14,2.49,1.55,-16.79]

df['date'] = ['2020']*9 ## 날짜

## 3개 데이터 분리
a_df = df.query('date =="2020"')
a_count = a_df['count']
area = a_df['area']

fig = plt.figure(figsize=(8,8)) ## 캔버스 생성
fig.set_facecolor('white') ## 캔버스 색상 설정
ax = fig.add_subplot() ## 그림 뼈대(프레임) 생성
     
ax.plot(area,a_count,marker='o',label='순호감도(%)') ## 선그래프 생성



plt.show()
    
if __name__=='__main__':
    main()
