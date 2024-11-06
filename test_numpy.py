import sys  
  
# 你要添加的目录路径  
your_directory = '/root/myenvs'  
  
# 检查该目录是否已经在 sys.path 中  
if your_directory not in sys.path:  
    # 将目录添加到 sys.path  
    sys.path.append(your_directory)  
  
import numpy as np  
  
# 生成一个5x5的随机整数矩阵  
matrix = np.random.randint(1, 10, size=(5, 5))  
  
# 计算行列式的值  
det = np.linalg.det(matrix)  
  
print("矩阵:")  
print(matrix)  
print("行列式的值:", det)