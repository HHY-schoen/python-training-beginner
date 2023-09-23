#載入numpy套件
import numpy as np
#根據列表建立ndarray物件
ndarr=np.array([3,4,-5])
#簡單的觀察
print(ndarr)  #把物件中的資料印出來
print(ndarr.size)  #取得資料的數量



#Python的一個第三方套件
#   用"陣列"代替"列表"處理資料
#   適合處理"多維度"的資料

#資料處理、機器學習的基礎套件
#   陣列運算速度遠高於列表 (核心是用c, c++
#   Pandas, TensorFlow的基礎