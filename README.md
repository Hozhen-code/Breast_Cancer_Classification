# 유방암 진단

## 개요
- **목표:** 세포 핵 특성(30개)을 이용해 악성(M) / 양성(B) 종양을 분류
- **알고리즘:** k-Nearest Neighbors (k-NN)
- **핵심 포인트:**
  - 전처리 데이터 타입 변경
  - train_test_split, MinMaxScaler
  - k 값 튜닝으로 Bias-Variance 균형 맞추기

## 데이터
PATH = `D:/projects/KNN_breast_cancer/data/breast-cancer.csv`

#### Description:
Breast cancer is the most common cancer amongst women in the world. It accounts for 25% of all cancer cases, and affected over 2.1 Million people in 2015 alone. It starts when cells in the breast begin to grow out of control. These cells usually form tumors that can be seen via X-ray or felt as lumps in the breast area.

The key challenges against it’s detection is how to classify tumors into malignant (cancerous) or benign(non cancerous). We ask you to complete the analysis of classifying these tumors using machine learning (with SVMs) and the Breast Cancer Wisconsin (Diagnostic) Dataset.


## 실행 방법
1. `knn_breast_cancer.ipynb` 실행
2. 필요 시 상단 설정에서 CSV 파일명을 수정 (기본: `./data/breast_cancer.csv`)

## 폴더 구조
```
knn_breast_cancer_project/
├─ data/
├─ knn_breast_cancer.ipynb
├─ README.md
├─ requirements.txt
└─ .gitignore
```

## 결과물
- Target값에 대한 변수들의 상관관계 그래프
- Confusion Matrix, Accuracy, Precision/Recall(F1), ROC-AUC
- k 값(1~31) 변화에 따른 Accuracy, Sensitivity(=Recall for Positive) 비교 그래프
- 전체 변수를 사용한 모델과 상위 선택 변수만을 사용한 모델의 성능비교 Bar chart
