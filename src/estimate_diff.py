

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

# 시드 고정
np.random.seed(42)

# 모집단 설정
mu1, mu2 = 50, 55
sigma = 10
n_pop = 1500

# 모집단 생성
pop1 = np.random.normal(loc=mu1, scale=sigma, size=n_pop)
pop2 = np.random.normal(loc=mu2, scale=sigma, size=n_pop)

# 모집단 시각화
plt.figure(figsize=(12, 6))
sns.histplot(pop1, kde=True, color="skyblue", label="Population 1 (μ=50)")
sns.histplot(pop2, kde=True, color="salmon", label="Population 2 (μ=55)")
plt.title("Generated Normal Distributions (σ = 10)")
plt.legend()
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)

# 샘플링
sample1 = np.random.choice(pop1, size=81, replace=False)
sample2 = np.random.choice(pop2, size=101, replace=False)

# 샘플 통계량 계산
x1, x2 = np.mean(sample1), np.mean(sample2)
s1, s2 = np.std(sample1, ddof=1), np.std(sample2, ddof=1)
n1, n2 = len(sample1), len(sample2)

print(f"샘플 평균 차이 (x1 - x2): {x1 - x2:.2f}")

# 1. 모집단 분산을 알고 있는 경우 (Z-distribution)
z = stats.norm.ppf(0.975)
se_known = np.sqrt((sigma**2)/n1 + (sigma**2)/n2)
margin_known = z * se_known
ci_known = (x1 - x2 - margin_known, x1 - x2 + margin_known)

# 2. 모집단 분산은 모르지만 같다고 가정 (Pooled t-distribution)
sp2 = (((n1-1)*s1**2 + (n2-1)*s2**2) / (n1 + n2 - 2))
se_equal = np.sqrt(sp2 * (1/n1 + 1/n2))
t_equal = stats.t.ppf(0.975, df=n1 + n2 - 2)
margin_equal = t_equal * se_equal
ci_equal = (x1 - x2 - margin_equal, x1 - x2 + margin_equal)

# 3. 모집단 분산도 모르고, 같다는 가정도 불가능한 경우 (Welch’s t-test)
se_unequal = np.sqrt((s1**2)/n1 + (s2**2)/n2)
df_num = ((s1**2)/n1 + (s2**2)/n2)**2
df_denom = ((s1**2)/n1)**2 / (n1 - 1) + ((s2**2)/n2)**2 / (n2 - 1)
df_unequal = df_num / df_denom
t_unequal = stats.t.ppf(0.975, df=df_unequal)
margin_unequal = t_unequal * se_unequal
ci_unequal = (x1 - x2 - margin_unequal, x1 - x2 + margin_unequal)

# 결과 출력
print("\n95% 신뢰구간 (모평균 차이 추정)")
print(f"1. 모집단 분산을 아는 경우 (Z):         {ci_known}")
print(f"2. 분산은 같다고 가정하는 경우 (t):   {ci_equal}")
print(f"3. 분산이 다를 수 있는 경우 (Welch):  {ci_unequal}")

plt.show()