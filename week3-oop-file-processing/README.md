# 3주차 파이썬 기초 프로젝트 : 학생 정보 관리 시스템
이 프로젝트는 파이썬 데이 구조와 파일 처리, 객체 지향 프로그래 사용 프로그램으로, 학생 관련 정보와 학생 명단, 성적을 관리하는 간단한 프로그램입니다.

## 프로젝트 설명
이 프로그램은 다음과 같은 기능을 수행합니다 :
1. 학생 정보, 성적 관리
2. 학생 명단 관리
   2.1 학생 추가, 검색, 정보 수정 및 삭제
   2.2 학생 목록 출력
   2.3 성적 분석
   2.4 파일 저장 및 불러오기


## 각 함수의 기능
- add_student(self, student) : 목록에 학생 정보 추가
- search_student(self, query) : 목록에서 학생 검색
- update_student(self, student_id, updates) : 학생 정보 업데이트
- delete_student(self, student_id) : 목록에서 학생 삭제
- display_all_students(self) : 전체 학생 목록 출력
- analyze_scores(self) : 평균 점수, 최고 점수, 최저 점수 계산
- save_to_file(self, filename) : 학생 정보 CSV 파일로 저장
- load_from_file(self, filename) : CSV 파일에서 학생 정보 불러오기
- main() : main 함

## 사용된 파이썬 기능
- 복합 자료형 (딕셔너리)
- 제어문 (if, elif, else문)
- 함수 정의 및 호출
- 예외 처리 (try ~ catch문)


## 실행 방법
1. 이 폴더로 이동합니다.
2. 터미널에서 `python main.py` 명령어로 프로그램을 실행합니다.

## 실행 결과
아래는 프로그램 실행 결과입니다:
