from typing import Dict, List

from .TCGPokeInterface import TCGPokeInterface


class TCGPokeParser(TCGPokeInterface):
    def __init__(self):
        self.__database_example = {
            4 : {
                'name':'pookachu',
                'rarity':'SAR',
                'quantity':69
            },
            46: {
                'name': 'eevee',
                'rarity': 'U',
                'quantity': 1286
            },
            27: {
                'name': 'mega aboba',
                'rarity': 'SSSR promo',
                'quantity': 1,
                'extra tag': 'golden'
            }
        }

    def get_card_ids(self) -> List[int]:
        return list(self.__database_example.keys())

    def get_card_by_id(self, card_id: int) -> Dict[str, str | int]:
        return self.__database_example[card_id]





