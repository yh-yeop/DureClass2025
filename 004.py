import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
csv_files = ["csv1.csv", "csv2.csv", "csv3.csv",'csv4.csv']

# 각 CSV별 산점도 그리기
for i, file in enumerate(csv_files, 1):
    df = pd.read_csv(file)
    
    # 결측치 제거
    df = df.dropna(subset=["Disease_Prob"])
    
    # x축 선택 (예: Glucose)
    if "Glucose" in df.columns:
        x = df["Glucose"]
    else:
        # Glucose가 없으면 다른 수치 컬럼 사용
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        numeric_cols.remove("Disease_Prob")
        x = df[numeric_cols[0]]
    
    y = df["Disease_Prob"]
    
    plt.figure(figsize=(6,4))
    plt.scatter(x, y)
    plt.title(f"CSV {i} 산점도 (x: {x.name}, y: Disease_Prob)")
    plt.xlabel(x.name)
    plt.ylabel("Disease_Prob")
    plt.grid(True)
    plt.show()
