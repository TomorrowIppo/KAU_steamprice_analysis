import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
df = pd.read_csv('data/steam.csv')  # 경로는 필요시 수정

# 가격 컬럼 확인 (예: 'price'가 실제 컬럼명인지 확인)
print(df.columns)

# 가격대를 1달러 단위로 bin 나누기 (0~25달러)
bins = range(0, 36, 1)
labels = [f"${i}-${i+1}" for i in bins[:-1]]
df['price_bin'] = pd.cut(df['price'], bins=bins, labels=labels, right=False)

# 각 가격대에 포함된 게임 수 세기
game_count_by_price = df['price_bin'].value_counts().sort_index()

# 그래프 그리기
plt.figure(figsize=(12, 6))
game_count_by_price.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel('Price Range ($)')
plt.ylabel('Number of Games')
plt.title('Number of Games by Price Range')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
