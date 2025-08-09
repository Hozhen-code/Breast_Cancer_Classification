# 유방암 진단

## 개요
- **목표:** 세포 핵 특성(30개)을 이용해 악성(M) / 양성(B) 종양을 분류
- **알고리즘:** k-Nearest Neighbors (k-NN)
- **핵심 포인트:**
  - 전처리 데이터 타입 변경
  - train_test_split, MinMaxScaler
  - k 값 튜닝으로 Bias-Variance 균형 맞추기

## 사용 데이터
- **Dataset**: [Breast Cancer Dataset](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset/data)

## 분석과정
1. 데이터 로드 및 탐색(EDA)
2. diagnosis와 이외의 변수간의 상관관계 시각화
3. train_test_split, MinMaxScaler 데이터 분할 및 전처리
4. 최적의 k값 튜닝(최적해 찾기)
5. 모델 학습
6. 모델 성능평가
7. 번외로 기존 모델과 변수선택 모델의 성능 비교 

## 실행 방법
1. `breast_cancer.ipynb` 실행

## 프로젝트 파일 구조
```
breast_cancer_project/
├─ utils/
├─ data/ # 원본 데이터
├─ .gitignore # Git 제외 파일 설정
├─ .gitattirbutes # Git 파일 처리 규칙 적용
├─ README.md # 프로젝트 설명
├─ breast_cancer.ipynb
└─ requirements.txt # 필요한 라이브러리 목록
```

## 결과물
- Target값에 대한 변수들의 상관관계 그래프
- k 값(1~31) 변화에 따른 Accuracy, Sensitivity(=Recall for Positive) 비교 그래프
- 최적의 k로 만든 모델을 Confusion Matrix, Accuracy, Precision/Recall(F1), ROC-AUC로 성능평가
- 전체 변수를 사용한 모델과 상위 선택 변수만을 사용한 모델의 성능비교 Bar chart
