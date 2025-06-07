import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 시드 고정 (재현성 확보)
np.random.seed(42)

# 설정
mu1 = 50   # Population 1 평균
mu2 = 55   # Population 2 평균
sigma = 10 # 두 분포의 동일한 표준편차
n = 1500   # 각 population의 데이터 수

# 데이터 생성
pop1 = np.random.normal(loc=mu1, scale=sigma, size=n)
pop2 = np.random.normal(loc=mu2, scale=sigma, size=n)

# 그래프 그리기
plt.figure(figsize=(12, 6))
sns.histplot(pop1, kde=True, color="skyblue", label="Population 1 (μ=50)")
sns.histplot(pop2, kde=True, color="salmon", label="Population 2 (μ=55)")
plt.title("Generated Normal Distributions (σ = 10)")
plt.legend()
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# 두 population 반환 (5-6번용)
print("Population 1 & 2 generated.")
