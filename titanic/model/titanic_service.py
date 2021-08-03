from titanic.model.dataset import Dataset
import pandas as pd
from sklearn.model_selection import KFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import np

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
    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})
        this.test = this.test.fillna({'Embarked':'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S':1, 'C':2, 'Q':3})
        this.test['Embarked'] = this.test['Embarked'].map({'S': 1, 'C': 2, 'Q': 3})
        return this
    @staticmethod
    def fare_ordinal(this) -> object:
        this.train['FareBand'] = pd.qcut(this.train['Fare'], 4)
        this.test['Fare'] = this.test['Fare'].fillna(1)
        this.test['FareBand'] = pd.qcut(this.test['Fare'],4)
        this.train['FareBand'] = pd.qcut(this.train['Fare'],4)
        return this
        # bins = [-1, 8, 15, 31, np.inf]
        # this.train = this.train.drop(['Fare'])
        # this.test = this.train.test(['Fare'])
        # qcut() 을 사용하면 자동으로 구간을 4등분한다
        # 타이타닉에서는 bins = [-1, 8, 15, 31,np.inf]로 구분된다.

    @staticmethod
    def title_nominal(this) -> object:
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)
        for dataset in combine:
            dataset["Title"] = dataset['Title'].replace(['Mme'], 'Rare')
            dataset["Title"] = dataset['Title'].replace([''], 'Rare')
            dataset["Title"] = dataset['Title'].replace('Mile', 'Mr')
            dataset["Title"] = dataset['Title'].replace('Ms', 'Miss')
        return None
    def age_ordinal(self) -> object:
        return None

    def gender_nominal(self) -> object:
        return None

    def create_k_fold(self) -> object:
        return None

'''
"PassengerId","Survived","Pclass","Name","Sex","Age","SibSp","Parch","Ticket","Fare","Cabin","Embarked"
'''
    def accuracy_by_classfier(self) :
        return None