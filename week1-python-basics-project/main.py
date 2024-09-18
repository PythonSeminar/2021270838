print("학과 정보")
# 학과 정보 입력 받기
name = input("학과명을 입력하세요 : ")
count = input("학생 수를 입력하세요 : ")
icount = int(count)
pname = input("담당 교수 이름을 입력하세요 : ")
year = input("설립 연도를 입력하세요 : ")
iyear = int(year)

# 학과 정보 딕셔너리로 저장
dict = {'학과명' : name, '학생 수' : icount, '담당 교수 이름' : pname, '설립 연도' : iyear}
print(dict)

# 학생 정보를 저장할 빈 리스트 생성
sinfor = []

# 5명의 학생 정보 입력 받기
print("\n학생 정보")
for i in range(5) :
    print(f"\n{i+1}번째 학생")
    sname = input("이름을 입력하세요 : ")
    snum = input("학번을 입력하세요 : ")
    score = float(input("평균 학점을 입력하세요 : "))
    #fscore = float(score)
    sub = input("수강 과목을 입력하세요 : ")
    tsub = tuple(subject.strip() for subject in sub.split(','))
    sdict = {'이름' : sname, '학번' : snum, '평균 학점' : score, '수강 과목' : tsub}
    sinfor.append(sdict)

# 학과 정보 처리
print(f"\n{dict['학과명']}는 {dict['설립 연도']}년에 설립되었습니다.")
print(f"\n학과명은 {dict['학과명']}입니다")
print(f"\n{dict['학과명']}의 길이는 {len(dict['학과명'])}글자입니다.")

# 학생 정보 처리
print(f"\n첫번째 학생의 정보는 {sinfor[0]}입니다.")
print(f"\n마지막 학생의 정보는 {sinfor[-1]}입니다.")
for i in range(3) :
    print(f"\n{i+2}번째 학생의 정보는 {sinfor[i+1]}입니다.")

print("\n새로운 학생 추가")
sname = input("이름을 입력하세요 : ")
snum = input("학번을 입력하세요 : ")
score = float(input("평균 학점을 입력하세요 : "))
sub = input("수강 과목을 입력하세요 : ")
nsdict = {'이름' : sname, '학번' : snum, '평균 학점' : score, '수강 과목' : tsub}
sinfor.append(nsdict)

del sinfor[0]

for each in sinfor :
    print(f"\n{each}")

# 학과 통계 계산
scores = sum(sdict['평균 학점'] for sdict in sinfor)
scoreavg = float(scores / len(sinfor))
print(f"\n평균 학점은 {scoreavg}입니다.")
counts = sum(1 for sdict in sinfor if sdict['평균 학점'] >= 3.5)
print(f"평균 학점이 3.5 이상인 학생 수는 {counts}명입니다.")
bscore = max(sdict['평균 학점'] for sdict in sinfor)
print(f"최고 점수는 {bscore}점입니다.")
wscore = min(sdict['평균 학점'] for sdict in sinfor)
print(f"최저 점수는 {wscore}점입니다.")

# 추가 기능 구현
aut = input("\n인증 여부를 입력하세요(예 or 아니요) : ")
dict['인증 여부'] = aut
print(dict)

qname = input("\n검색할 학생의 이름을 입력하세요 : ")
found = False
for student in sinfor :
    if student['이름'] == qname :
        print(f"\n학생 정보 : {student}")
        found = True
        break

if not found : 
    print("해당 학생을 찾을 수 없습니다.")

# 모든 정보 출력
print("\n학과 정보")
print(dict)
print("\n학생 정보")
print(sinfor)
print("\n평균")
print(scoreavg)
print("\n최고 점수")
print(bscore)
print("\n최저 점수")
print(wscore)