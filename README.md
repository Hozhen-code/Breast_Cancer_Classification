# 유방암 진단

## 개요
- **목표:** 세포 핵 특성(30개)을 이용해 악성(M) / 양성(B) 종양을 분류
- **알고리즘:** k-Nearest Neighbors (k-NN)
- **핵심 포인트:**
  - 전처리 데이터 타입 변경
  - train_test_split, MinMaxScaler
  - k 값 튜닝으로 Bias-Variance 균형 맞추기

## 데이터
utils/paths 패키지로 절대경로 설정

## 실행 방법
1. `breast_cancer.ipynb` 실행
2. 필요 시 상단 설정에서 CSV 파일명을 수정 (기본: `./data/breast_cancer.csv`)

## 폴더 구조
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
- Confusion Matrix, Accuracy, Precision/Recall(F1), ROC-AUC
- k 값(1~31) 변화에 따른 Accuracy, Sensitivity(=Recall for Positive) 비교 그래프
- 전체 변수를 사용한 모델과 상위 선택 변수만을 사용한 모델의 성능비교 Bar chart
