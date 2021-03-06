import pandas as pd
import  os
# 目標資料夾
dir_path = 'D:/task/01.liver-disorders/03.Kmeans_cluster_result/2/eva_part2'
# 輸出資料夾
output_dor_path ='D:/task/01.liver-disorders/03.Kmeans_cluster_result/2/eva_part2_new_label_upade'

file_number = 0


for fd in os.listdir(dir_path):
    full_path = os.path.join(dir_path, fd)
    if os.path.isdir(full_path):
        continue
    else:
        data = pd.read_csv(full_path,sep=',',header=None)
        columes_name = data.columns

        data[columes_name[-1]] = data[columes_name[-1]].replace(1,'A')
        data[columes_name[-1]] = data[columes_name[-1]].replace(2,'B')
        data = data.fillna(0)

        data.to_csv(os.path.join(output_dor_path, fd), index=0, header=0)

        print('檔案:', full_path)
        file_number +=1
