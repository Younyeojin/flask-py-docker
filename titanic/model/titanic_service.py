from titanic.model.dataset import Dataset
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier

class TitanicService(object):
    dataset = Dataset()

    def new_model(self, payload) -> object:
        # this = self.dataset
        # this.context = './data/'
        # this.fname = payload
        return pd.read_csv(f"/data/{payload}.csv")

    @staticmethod
    def count_survived_dead(this)->object:
        return this.train.drop('Survived', axis=1)      # axis 세로
    @staticmethod
    def create_label(this)->object:
        return this.train['Survived']
    @staticmethod
    def drop_feature(this, *feature)->object:
        for i in feature:
            this.train = this.train.drop([i], axis=1)
            this.test = this.test.drop([i], axis=1)
        return this

    def embarked_nominal(self):
        return None

    def fare_oridnal(self):
        return None

    def title_nominal(self):
        return None

    def gender_norminal(self):
        return None

    def age_ordinal(self):
        return None

    def create_k_fold(self):
        return None

    def accuracy_by_classfier(self) :
        return None