import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Malgun Gothic'
# CSV 파일 불러오기 (각자 경로 지정)
csv_files = ["./gen/assignment_csv1.csv", "./gen/assignment_csv2.csv", "./gen/assignment_csv3.csv"]

for i, file in enumerate(csv_files, 1):
    df = pd.read_csv(file)
    
    # 숫자형 컬럼 NaN 제거
    df = df.dropna(subset=['Glucose','Cholesterol','Disease_Prob','Exercise_per_week'])
    
    # 산점도
    plt.figure(figsize=(8,6))
    scatter = plt.scatter(
        df['Glucose'], 
        df['Cholesterol'], 
        c=df['Disease_Prob'], 
        s=df['Exercise_per_week']*20,  # 운동 횟수에 비례
        cmap='viridis', 
        alpha=0.7,
        edgecolors='w'
    )
    plt.colorbar(scatter, label='Disease_Prob')
    plt.xlabel('Glucose')
    plt.ylabel('Cholesterol')
    plt.title(f'CSV {i} 산점도 (학생 수준 기준)')
    plt.grid(True)
    plt.show()