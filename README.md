 ### 1. 가상환경 생성 및 활성화
ufw allow 5000 #5000번 포트 활성화
apt update 
apt install python3 python3-pip -y #Python 설치
python3 -m venv venv #Python 가상 머신 설치
source venv/bin/activate #가상 머신 접근 
pip install -r requirements.txt

### 2. 서버 실행 
python app.py

### 3. 서버 접근 
기본 실행 주소: http://0.0.0.0:5000
EC2에서 접근 시: http://<EC2_IP>:5000

### API 설명
1. GET /todos
설명: 전체 할일 목록 조회
 2. POST /todos
설명: 새 할일 추가
3. PUT /todos/{id}
설명: 해당 ID의 할일 완료/미완료 상태 토글
4. DELETE /todos/{id}
설명: 해당 ID의 할일 삭제
