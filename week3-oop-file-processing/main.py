import csv

class Student :
    def __init__(self, name, student_id, grade) :
        # 초기화 로직
        self.name = name
        self.student_id = student_id
        self.grade = grade
        self.scores = {}

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
        if not self.student :
            print("등록된 학생이 없습니다.")
        else :
            for student in self.students :
                print(student)
    
    def analyze_scores(self) :
        # 성적 분석 로직
        all_scores = [score for student in self.student for score in student.scores.values()]
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
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["name", "student_id", "grade", "scores"])
                for student in self.students:
                    writer.writerow([student.name, student.student_id, student.grade, student.scores])
            print(f"{filename} 파일에 저장되었습니다.")
        except Exception as e:
            print(f"파일 저장 중 오류 발생: {e}")
    
    def load_from_file(self, filename) :
        # CSV 파일 로드 로직
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    scores = eval(row["scores"])  # 저장된 딕셔너리 형태를 복원
                    student = Student(row["name"], row["student_id"], row["grade"])
                    student.scores = scores
                    self.add_student(student)
            print(f"{filename} 파일에서 데이터를 불러왔습니다.")
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