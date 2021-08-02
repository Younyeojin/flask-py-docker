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
        this = self.service.preprocessing()
        return this


    def preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model("train")
        this.test = service.new_model("test")
        return this

