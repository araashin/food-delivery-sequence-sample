# food-delivery-sequence-sample
일상 속 소프트웨어 사용 사례 - 시퀀스 다이어그램 기반 구현(소웨공)

# 시퀀스 다이어그램

아래는 Mermaid.live에서 작성한 시퀀스 다이어그램입니다.

![시퀀스 다이어그램](./sequence_diagram.png)

## 모듈 평가

### 응집도(Cohesion)
각 모듈은 단일 책임을 가집니다:
- `restaurant.py`: 메뉴 제공 및 주문 수락
- `delivery.py`: 배달 시작 처리
- `payment.py`: 결제 처리
→ 높은 응집도를 유지함

### 결합도(Coupling)
모든 모듈은 `app.py`에서 조정되며, 서로 직접 참조하지 않음.
→ 낮은 결합도를 유지하여 유지보수에 유리함

## ▶ 실행 방법

Python이 설치된 환경에서 아래 명령어로 실행합니다:

```bash
python main.py

