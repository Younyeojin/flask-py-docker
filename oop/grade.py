'''
국어 kor, 영어 eng, 수학 math를 입력받아서
평균점수를 통해 A~F 학점을 출력하시오
'''

class Grade(object):

    def __init__(self, kor, eng, math):    # 생성자 메소드
        self.kor = kor                     # 인스턴스 변수 (this와 같음)
        self.eng = eng
        self.math = math

    def sum(self):                         # 메소드
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3


    @staticmethod
    def main():                            # static 메인 메소드
        kor = int(input('Korean: '))       # input : print문
        eng = int(input('English: '))
        math = int(input('Math: '))
        grade = Grade(kor, eng, math)      # 메소드 생성; 위에 생성 안한거
        avg = grade.avg()                  # 레퍼런스 변수; 인스턴스 변수와 로컬변수 이어줌
        if avg >= 90:
            result = 'A'
        elif avg >= 80:
            result = 'B'
        elif avg >= 70:
            result = 'C'
        elif avg >= 60:
            result = 'D'
        elif avg >= 50:
            result = 'E'
        else:
            result = 'F'
        print(f'{result}')

Grade.main()