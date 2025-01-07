import pandas as pd
import glob
import os
import chardet
import csv
from openpyxl import load_workbook
from openpyxl.styles import Border, Side

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def detect_delimiter(file_path, encoding):
    with open(file_path, 'r', encoding=encoding) as f:
        sample = f.read(1024)
        sniffer = csv.Sniffer()
        delimiter = sniffer.sniff(sample).delimiter
    return delimiter

def add_borders_to_excel(file_path):
    wb = load_workbook(file_path)
    ws = wb.active
    thin_border = Border(left=Side(style='thin'), 
                         right=Side(style='thin'), 
                         top=Side(style='thin'), 
                         bottom=Side(style='thin'))
    
    for row in ws.iter_rows():
        for cell in row:
            cell.border = thin_border
    
    wb.save(file_path)

def convert_txt_to_xlsx():
    # 获取当前目录下所有的txt文件
    txt_files = glob.glob("*.txt")
    
    for txt_file in txt_files:
        # 检测文件的字符集
        encoding = detect_encoding(txt_file)
        
        # 检测文件的分隔符
        delimiter = detect_delimiter(txt_file, encoding)
        
        # 读取txt文件
        df = pd.read_csv(txt_file, sep=delimiter, encoding=encoding)
        
        # 生成xlsx文件名（将.txt替换为.xlsx）
        xlsx_file = os.path.splitext(txt_file)[0] + '.xlsx'
        
        # 保存为xlsx文件
        df.to_excel(xlsx_file, index=False)
        
        # 为所有单元格添加边框
        add_borders_to_excel(xlsx_file)
        
        print(f"已将 {txt_file} 转换为 {xlsx_file}")

if __name__ == "__main__":
    convert_txt_to_xlsx() 