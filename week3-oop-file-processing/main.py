import csv

class Student :
    def __init__(self, name, student_id, grade) :
        # 초기화 로직
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.scores = {}

    def __str__(self):
        return f"이름: {self.name}, 학번: {self.student_id}, 학년: {self.grade}, 점수: {self.scores}"

class StudentManagementSystem :
    def __init__(self) :
        # 초기화 로직
        self.students = []
    
    def add_student(self, student) :
        # 학생 추가 로직
        self.students.append(student)
        print(f"{student.name} 학생이 추가되었습니다.")

    def search_student(self, query) :
        # 학생 검색 로직
        results = [s for s in self.students if s.name == query or s.student_id == query]
        if not results :
            print("해당 학생을 찾을 수 없습니다.")
        return results
    
    def update_student(self, student_id, updates) :
        # 학생 정보 수정 로직
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student :
            for key, value in updates.items() :
                if key == "name" :
                    student.name = value
                elif key == "grade" :
                    student.grade = value
                elif key == "scores" and isinstance(value, dict) :
                    student.scores.update(value)
            print(f"{student.name} 학생의 정보가 업데이트 되었습니다.")
        else :
            print("해당 학번의 학생을 찾을 수 없습니다.")
    
    def delete_student(self, student_id) :
        # 학생 삭제 로직
        initial_count = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]
        if len(self.students) < initial_count :
            print("학생이 삭제되었습니다.")
        else :
            print("해당 학번의 학생을 찾을 수 없습니다.")
    
    def display_all_students(self) :
        # 전체 학생 목록 출력 로직
        if not self.students :
            print("등록된 학생이 없습니다.")
        else :
            for student in self.students :
                print(student)
    
    def analyze_scores(self) :
        # 성적 분석 로직
        all_scores = [score for student in self.students for score in student.scores.values()]
        if all_scores:
            average = sum(all_scores) / len(all_scores)
            highest = max(all_scores)
            lowest = min(all_scores)
            print(f"평균 점수: {average:.2f}, 최고 점수: {highest}, 최저 점수: {lowest}")
        else:
            print("등록된 점수가 없습니다.")

    def save_to_file(self, filename) :
        # CSV 파일 저장 로직
        try:
            # filename으로 지정된 파일을 쓰기 모드로 열기
            with open(filename, mode='w', newline='') as file:
                # file 객체를 사용해 csv 작성 도구인 writer 객체를 생성
                writer = csv.writer(file)
                # 데이터가 어떤 필드를 나타내는지 헤더 작성
                writer.writerow(["name", "student_id", "grade", "scores"])
                # 각 학생 객체의 데이터를 한 줄씩 쓰기
                # 딕셔너리 형태의 student.scores를 CSV 파일에 텍스트로 기록
                for student in self.students:
                    writer.writerow([student.name, student.student_id, student.grade, student.scores])
            print(f"{filename} 파일에 저장되었습니다.")
        except Exception as e:
            print(f"파일 저장 중 오류 발생: {e}")
    
    def load_from_file(self, filename) :
        # CSV 파일 로드 로직
        try:
            # filename 파일 읽기 모드로 열기
            with open(filename, mode='r') as file:
                # 각 행의 데이터가 딕셔너리로 반환
                # DictReader - 각 줄을 딕셔너리 형태로 반환
                reader = csv.DictReader(file)
                # 파일의 각 행 순회
                for row in reader:
                    # scores 데이터는 텍스트로 저장되어 eval()을 사용해 딕셔너리로 복원
                    # 저장된 딕셔너리 형태를 복원
                    scores = eval(row["scores"]) 
                    student = Student(row["name"], row["student_id"], row["grade"])
                    # 복원한 scores를 학생 객체에 할당
                    student.scores = scores
                    # 새 학생 객체를 시스템에 추가
                    self.add_student(student)
            print(f"{filename} 파일에서 데이터를 불러왔습니다.")
        # 파일을 찾을 수 없을 때의 예외 처리
        except FileNotFoundError:
            print(f"{filename} 파일을 찾을 수 없습니다.")
        except Exception as e:
            print(f"파일 불러오기 중 오류 발생: {e}")
    
def main() :
    # 메인 프로그램 로직
    system = StudentManagementSystem()

    while True:
        print("\n학생 관리 시스템")
        print("1. 학생 추가")
        print("2. 학생 검색")
        print("3. 학생 정보 수정")
        print("4. 학생 삭제")
        print("5. 전체 학생 목록 출력")
        print("6. 성적 분석")
        print("7. 파일 저장")
        print("8. 파일 불러오기")
        print("9. 프로그램 종료")
        
        number = input("원하는 작업의 번호를 입력하세요: ")
        
        if number == '1':
            name = input("추가할 학생 이름을 입력하세요 : ")
            student_id = input("추가할 학생 학번을 입력하세요: ")
            grade = input("추가할 학생 학년을 입력하세요 : ")
            student = Student(name, student_id, grade)
            system.add_student(student)
        elif number == '2':
            query = input("검색할 학생의 이름 또는 학번을 입력하세요 : ")
            searchst = system.search_student(query)
            for student in searchst:
                print(student)
        elif number == '3':
            student_id = input("수정할 학생의 학번을 입력하세요 : ")
            updates = {}
            name = input("새 이름을 입력하세요 : ")
            if name:
                updates["name"] = name
            grade = input("새 학년을 입력하세요 : ")
            if grade:
                updates["grade"] = grade
            nscores = input("새 점수를 입력하세요 : ")
            if nscores:
                scores = dict(item.split("=") for item in nscores.split(", "))
                updates["scores"] = {k: int(v) for k, v in scores.items()}
            system.update_student(student_id, updates)
        elif number == '4':
            student_id = input("삭제할 학생의 학번: ")
            system.delete_student(student_id)
        elif number == '5':
            system.display_all_students()
        elif number == '6':
            system.analyze_scores()
        elif number == '7':
            filename = input("저장할 파일 이름: ")
            system.save_to_file(filename)
        elif number == '8':
            filename = input("불러올 파일 이름: ")
            system.load_from_file(filename)
        elif number == '9':
            filename = input("프로그램을 종료합니다. 저장할 파일 이름을 입력하세요: ")
            system.save_to_file(filename)
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 번호를 입력해주세요.")


if __name__ == "__main__" :
    main()
