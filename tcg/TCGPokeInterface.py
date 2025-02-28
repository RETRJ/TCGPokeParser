from abc import ABC, abstractmethod



class TCGPokeInterface(ABC):
    @abstractmethod
    def get_card_ids(self):
        raise NotImplementedError('Not implemented')

    @abstractmethod
    def get_card_by_id(self):
        raise NotImplementedError('Not implemented')


