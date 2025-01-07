import pandas as pd
import glob
import os

def convert_txt_to_xlsx():
    # 获取当前目录下所有的txt文件
    txt_files = glob.glob("*.txt")
    
    for txt_file in txt_files:
        # 读取txt文件，假设txt文件是用tab分隔的
        df = pd.read_csv(txt_file, sep='\t')
        
        # 生成xlsx文件名（将.txt替换为.xlsx）
        xlsx_file = os.path.splitext(txt_file)[0] + '.xlsx'
        
        # 保存为xlsx文件
        df.to_excel(xlsx_file, index=False)
        print(f"已将 {txt_file} 转换为 {xlsx_file}")

if __name__ == "__main__":
    convert_txt_to_xlsx() 