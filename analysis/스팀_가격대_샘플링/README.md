# 🎮 Steam 게임 가격 분석

이 프로젝트는 Steam 게임 데이터셋을 기반으로 게임 가격의 **샘플 통계**, **신뢰 구간**, **예측 구간** 등을 분석합니다. 이를 통해 Steam 가격 분포의 특성과 정규성 가정의 적절성에 대해 이해하고자 합니다.


## 📊 분석 목표

- 게임 가격의 **표본 평균 및 분산**, **99% 신뢰 구간(CI)**, **99% 예측 구간(PI)**을 계산합니다.
- **표본 크기에 따른 오차 범위와 신뢰성의 변화**를 관찰합니다.
- Steam 게임 가격이 정규분포를 따른다고 가정했을 때, 그 적절성을 탐색합니다.

## 🗂️ 데이터

- 파일명: `steam.csv`
- 사용 컬럼: `price` (게임 가격)
- 전처리 과정:
  - 가격이 0인 게임 제거 (무료 게임 제외)
  - IQR 방식으로 극단값 제거

## ⚙️ 사용된 도구

- Python 3.x
- pandas
- numpy
- scipy
- matplotlib

## 🧪 분석 과정

1. **표본 추출**  
   샘플 크기 10, 30, 100에 대해 가격 데이터를 랜덤 추출하여 분석을 진행합니다.

2. **통계량 계산**  
   - 표본 평균 (Sample Mean)
   - 표본 분산 (Sample Variance)
   - 99% 신뢰 구간 (CI) — t 분포, chi-square 분포 사용
   - 99% 예측 구간 (PI) — 미래 관측값 포함 가능 범위

3. **미래값 추정**  
   새로운 가격 값을 무작위로 뽑아 예측 구간에 포함되는지 여부 확인

---

## 📈 결과 요약

### [샘플 크기: 10]
- Sample Mean: 4.850  
- Sample Variance: 17.174  
- 99% CI (Mean): (0.591, 9.109)  
- 99% CI (Variance): (6.552, 89.089)  
- 99% Prediction Interval: (-9.275, 18.975)  
✅ Future Value (4.990) in Interval: **True**

---

### [샘플 크기: 30]
- Sample Mean: 5.573  
- Sample Variance: 16.964  
- 99% CI (Mean): (3.501, 7.646)  
- 99% CI (Variance): (9.400, 37.494)  
- 99% Prediction Interval: (-5.967, 17.114)  
✅ Future Value (4.990) in Interval: **True**

---

### [샘플 크기: 100]
- Sample Mean: 5.199  
- Sample Variance: 16.382  
- 99% CI (Mean): (4.136, 6.262)  
- 99% CI (Variance): (11.669, 24.385)  
- 99% Prediction Interval: (-5.484, 15.882)  
✅ Future Value (4.990) in Interval: **True**

---

## 🧠 분석 해석

- **표본 크기가 커질수록** 신뢰 구간과 예측 구간의 폭이 **좁아집니다**.
- 이는 **추정의 정밀도가 증가**함을 의미합니다.
- 모든 경우에서 미래 가격 값은 예측 구간에 포함되어 있으며, 이는 **중심극한정리(CLT)** 덕분에 정규 근사 기반 예측이 잘 작동함을 시사합니다.
- 다만 가격 데이터는 음수가 없기 때문에 완전한 정규분포가 아닌 **비대칭 분포**(truncated normal 또는 log-normal)에 가까운 특성이 있습니다.

---

## 📝 결론 요약

- Steam 게임은 **0~5달러 구간**에 가장 많이 분포하며, 고가 게임은 매우 드뭅니다.
- 데이터는 정규분포가 아니지만, **표본 통계 분석에는 정규 가정이 유용하게 적용**됩니다.
- **신뢰 구간과 예측 구간은 표본 크기 증가에 따라 안정적으로 수렴**합니다.

## 🔍 참고 문서

- [pandas.cut() 공식 문서](https://pandas.pydata.org/docs/reference/api/pandas.cut.html)
- [Scipy Stats](https://docs.scipy.org/doc/scipy/)
- [Steam Dataset (Kaggle)](https://www.kaggle.com/datasets/nikdavis/steam-store-games)

---