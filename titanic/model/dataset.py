from dataclasses import dataclass


@dataclass                                                 # @dataclass : Decoration 패턴
class Dataset(object):
    context: str
    fname: str
    train: object
    test: object
    id: str                 #id가 key
    label: str

    @property                                               # @property : getter / @ddd.setter : setter
    def context(self) -> str: return self._context          # self._context : 초기화
    @context.setter                                         # ._ : 보호된 공간
    def context(self, context): self._context = context
    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fname): self._fname = fname
    @property
    def train(self) -> object: return self._train
    @train.setter
    def train(self, train): self._train = train
    @property
    def test(self) -> object: return self._test
    @test.setter
    def test(self, test): self._test = test
    @property
    def id(self) -> str: return self._id
    @id.setter
    def id(self, id): self._id = id
    @property
    def label(self) -> str: return self._label
    @label.setter
    def label(self, label): self._label = label

