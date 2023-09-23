#封包:包含模組的資料夾，用來整理/分類模組程式  
#資料夾對應到封包，檔案對應到模組

#主程式
import geometry.point
result=geometry.point.distance(3,4)
print('距離:',result)
import geometry.line as line
result=line.slope(1,1,3,3)
print('斜率:',result)