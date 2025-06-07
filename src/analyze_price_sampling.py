import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# 데이터 불러오기
df = pd.read_csv('data/steam.csv')

# 가격만 추출, 결측치 제거
price_data = df['price'].dropna()
price_data = price_data[price_data > 0]  # 0달러 게임 제외

# 극단값 제거 (IQR 방식)
Q1 = price_data.quantile(0.25)
Q3 = price_data.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
filtered_price = price_data[(price_data >= lower_bound) & (price_data <= upper_bound)]

# 샘플링 분석 함수
def sample_analysis_price(sample_size, population_data):
    np.random.seed(42)
    sample = np.random.choice(population_data, size=sample_size, replace=False)

    sample_mean = float(np.mean(sample))
    sample_var = float(np.var(sample, ddof=1))
    sample_std = float(np.sqrt(sample_var))

    t_critical = stats.t.ppf(0.995, df=sample_size - 1)
    margin_mean = t_critical * sample_std / np.sqrt(sample_size)
    ci_mean = (sample_mean - margin_mean, sample_mean + margin_mean)

    chi2_lower = stats.chi2.ppf(0.005, df=sample_size - 1)
    chi2_upper = stats.chi2.ppf(0.995, df=sample_size - 1)
    ci_variance = ((sample_size - 1) * sample_var / chi2_upper,
                   (sample_size - 1) * sample_var / chi2_lower)

    pred_margin = t_critical * sample_std * np.sqrt(1 + 1 / sample_size)
    pred_interval = (sample_mean - pred_margin, sample_mean + pred_margin)

    future_value = float(np.random.choice(population_data, size=1)[0])
    in_pred_interval = pred_interval[0] <= future_value <= pred_interval[1]

    return {
        'Sample Size': sample_size,
        'Sample Mean': sample_mean,
        'Sample Variance': sample_var,
        '99% CI Mean': ci_mean,
        '99% CI Variance': ci_variance,
        '99% Prediction Interval': pred_interval,
        'Future Value': future_value,
        'In Prediction Interval': in_pred_interval
    }

# 분석 실행
population = filtered_price.values
results_list = [
    sample_analysis_price(10, population),
    sample_analysis_price(30, population),
    sample_analysis_price(100, population)
]

# 결과 출력
for res in results_list:
    print(f"\n[샘플 크기: {res['Sample Size']}]")
    print(f"Sample Mean: {res['Sample Mean']:.3f}")
    print(f"Sample Variance: {res['Sample Variance']:.3f}")
    print(f"99% CI Mean: ({res['99% CI Mean'][0]:.3f}, {res['99% CI Mean'][1]:.3f})")
    print(f"99% CI Variance: ({res['99% CI Variance'][0]:.3f}, {res['99% CI Variance'][1]:.3f})")
    print(f"99% Prediction Interval: ({res['99% Prediction Interval'][0]:.3f}, {res['99% Prediction Interval'][1]:.3f})")
    print(f"Future Value: {res['Future Value']:.3f} → In Prediction Interval: {res['In Prediction Interval']}")
