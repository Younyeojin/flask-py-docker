'''
학생이름을 입력받고
국어 kor, 영어 eng, 수학 math를 입력받아서
학생이름, 총점, 평균, 학점을 출력하시오
'''

class Grade(object):

    def __init__(self, name):
        self.name = name
        self.scores = []                                     # []: list

    def addScores(self, score):
        self.scores.append(score)                            # append: 맨 마지막에 값을 붙인다 , 배열추가(list)

    def avg(self):
        return sum(self.scores) / len(self.scores)           # len: length(문자길이)

    @staticmethod
    def main():
        grade = Grade(input('Input Student name: '))
        '''
        kor = int(input('Korean: '))
        eng = int(input('English: '))
        math = int(input('Math: '))
        '''
        for i in ['Korean: ', 'English: ', 'Math: ']:         # for i in []:
            grade.addScores(int(input(f'{i}')))
            # print(int(input(f'{i}: ')))                     # pass          => 기본 형식
            # pass
        avg = grade.avg()
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
        # print(f'{name} + {addScores}')
        print(f'{result}')


Grade.main()