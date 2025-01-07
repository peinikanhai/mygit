import random
import csv

def generate_large_test_file(filename, num_rows=500000):
    # 定义列名
    headers = ['id', 'name', 'age', 'city']
    
    # 定义一些示例数据
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    
    # 打开文件并写入数据
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        for i in range(1, num_rows + 1):
            # 随机生成数据
            name = random.choice(names)
            age = random.randint(20, 60)
            city = random.choice(cities)
            writer.writerow([i, name, age, city])
    
    print(f"已生成 {filename}，包含 {num_rows} 行数据")

if __name__ == "__main__":
    generate_large_test_file('large_test_file.txt') 