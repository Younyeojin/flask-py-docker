import unittest
import os
from titanic.model.titanic_service import TitanicService


class TitanicServiceTest(unittest.TestCase):
    mock = TitanicService()
    def test_new_model(self):
        # print(self.mock.new_model("train"))
        print(self.mock.new_model("test"))
    def count_survived_dead(self, ):
        return []
    def test_create_train(self):
        return None
    def test_drop_feature(self, *feature):
        return None
    def test_embarked_nominal(self):
        return None
    def test_fare_oridnal(self):
        return None
    def test_title_nominal(self):
        return None
    def test_gender_norminal(self):
        return None
    def test_age_ordinal(self):
        return None
    def test_create_k_fold(self):
        return
    def test_accuracy_by_classfier(self):
        return None

if __name__ == '__main__':
    unittest.main()