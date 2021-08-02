

class OneToTenSum(object):

    def one_to_ten_sum_1(self):
        # example 1
        sum = 0                   # 기본 구조: for i in []
        for i in range(1, 11):    # range: 뒤의 값은 포함하지 않음 -> 뽑아내고자 하는 값에 +1 해야 나옴
            sum += i
        print(sum)


    def one_to_ten_sum_2(self):
       print(sum(i for i in range(1, 11)))
   # print(sum(i for i in []))                    # 이 식도 가능 ; list  있을때


    def one_to_ten_sum_3(self):
        print(sum(range(1, 11)))


