import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def grade_df(df_new):
    # 1. 결측치 확인
    print("=== 결측치 ===")
    print(df_new.isnull().sum())
    
    # 2. 값 범위 확인
    print("\n=== 이상치 점검 ===")
    numeric_cols = ['Age','BMI','BloodPressure','Glucose','Cholesterol','Exercise_per_week','Disease_Prob']
    for col in numeric_cols:
        if col in df_new.columns:
            print(f"{col}: min={df_new[col].min()}, max={df_new[col].max()}")

    # 4. 시각화
    plt.figure(figsize=(12,5))
    
    # Glucose vs Disease_Prob 산점도
    plt.subplot(1,2,1)
    sns.scatterplot(data=df_new, x='Glucose', y='Disease_Prob', hue='Smoking', style='Gender')
    plt.title("Glucose vs Disease_Prob")
    
    # Correlation heatmap
    plt.subplot(1,2,2)
    corr = df_new[numeric_cols].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm',vmin=-1,vmax=1)
    plt.title("Numeric Correlation")
    
    plt.tight_layout()
    plt.show()

# grade_df(pd.read_csv("csv_3.csv"))
grade_df(pd.read_csv("csv_3_cleaned.csv"))
