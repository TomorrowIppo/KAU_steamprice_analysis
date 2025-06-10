import numpy as np
from scipy.stats import f
import matplotlib.pyplot as plt
import seaborn as sns

# 시드 고정
np.random.seed(42)

# 모집단 설정
mu1, mu2 = 50, 55
sigma1, sigma2 = 10, 10
n_total = 1500

# 모집단 생성
pop1 = np.random.normal(loc=mu1, scale=sigma1, size=n_total)
pop2 = np.random.normal(loc=mu2, scale=sigma2, size=n_total)

# 각 모집단에서 표본 추출
n1, n2 = 81, 101
sample1 = np.random.choice(pop1, size=n1, replace=False)
sample2 = np.random.choice(pop2, size=n2, replace=False)

# 표본 분산 계산 (ddof=1: unbiased)
s1_sq = np.var(sample1, ddof=1)
s2_sq = np.var(sample2, ddof=1)

# 신뢰수준
alpha = 0.05

# F 분포 기반 신뢰구간 계산
f_lower = f.ppf(alpha / 2, dfn=n1 - 1, dfd=n2 - 1)
f_upper = f.ppf(1 - alpha / 2, dfn=n1 - 1, dfd=n2 - 1)

# 신뢰구간 계산 (σ1² / σ2²)
ci_lower = (s1_sq / s2_sq) / f_upper
ci_upper = (s1_sq / s2_sq) / f_lower

# 결과 출력
print(f"표본 분산 비율 (s1² / s2²): {s1_sq:.3f} / {s2_sq:.3f} = {s1_sq / s2_sq:.3f}")
print(f"95% 신뢰구간 (σ1² / σ2²): ({ci_lower:.4f}, {ci_upper:.4f})")

# 분포 시각화
plt.figure(figsize=(12, 6))
sns.histplot(sample1, kde=True, color='skyblue', label="Sample 1")
sns.histplot(sample2, kde=True, color='salmon', label="Sample 2")
plt.title("Sample Distributions from Population 1 and 2")
plt.legend()
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
