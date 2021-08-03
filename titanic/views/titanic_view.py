from titanic.model.dataset import Dataset
from titanic.model.titanic_service import TitanicService


class TitanicView(object):
    dataset = Dataset()
    service = TitanicService()

    def modeling(self):
        # service = self.service
        '''
        print(f'The Type of This is  {type(this.test)}')
        print(f'The head of Test is \n {this.test.head(2)}')
        print(f'The head of Test is \n {this.train.head(2)}')
        '''
        this = self.preprocessing()
        return this


    def preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        self.print_this(this)
        return this

    @staticmethod
    def print_this(this):
        print('*'*100)
        print(f'The Type of Train is {type(this.train)}, The Type of Test is {type(this.test)} ')
        print(f'Columns of Train is {this.train.columns}, Columns of Test is {this.test.columns} ')
        print(f'Top Row of Train is {this.train.head(1)}, Top Row of Test is {this.test.head(1)} ')
        print(f'Null Count of Train is {this.train.isnull().sum()}, '
              f'Null Count of Test is {this.test.isnull().sum()}')