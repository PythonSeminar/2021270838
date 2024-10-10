def input_student_info() :
    # 학생 정보 입력 로직
    list = []
    while True :
        student = input("이름을 입력하세요 : ")
        score = int(input("점수를 입력하세요 : "))
        # 학생 정보 딕셔너리로 저장
        dict = {'이름' : student, '점수' : score}
        # 학생 정보 딕셔너리 리스트에 저장
        list.append(dict)
        # q 누르면 종료
        q = input("입력을 종료하려면 q, 계속하려면 아무 키나 누르세요.\n")
        if q == 'q' :
            break
    return list

def calculate_grade(score) :
    # 점수에 따른 등급 계산 로직
    if score > 89 :
        grade = 'A'
    elif score > 79 :
        grade = 'B'
    elif score > 69 :
        grade = 'C'
    elif score > 59 :
        grade = 'D'
    else :
        grade = 'F'
    return grade

def print_results(students) :
    # 결과 출력 로직
    for student in students :
        name = student['이름']
        score = int(student['점수'])
        grade = calculate_grade(score)
        print(f"이름: {name}, 점수: {score}, 등급: {grade}")

def calculate_stats(students) :
    # 통계 계산 로직
    total_score = 0
    max_score = -1
    min_score = 101
    student_count = len(students)

    for student in students :
        iscore = int(student['점수'])
        total_score += iscore

        if iscore > max_score : 
            max_score = iscore

        if iscore < min_score : 
            min_score = iscore
        
    average_score = total_score / student_count
    
    print(f"\n평균 점수 : {average_score}")
    print(f"\n최고 점수 : {max_score}")
    print(f"\n최저 점수 : {min_score}")


def main() :
    students = []
    # 메인 프로그램 로직
    students = input_student_info()
    print_results(students)
    calculate_stats(students)

if __name__ == "__main__" :
    main()