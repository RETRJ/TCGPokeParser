from abc import ABC, abstractmethod
from typing import List, Dict


class TCGPokeInterface(ABC):
    @abstractmethod
    def get_card_ids(self) -> List[int]:
        raise NotImplementedError('Not implemented')

    @abstractmethod
    def get_card_by_id(self, card_id: int) -> Dict[str, str | int]:
        raise NotImplementedError('Not implemented')


