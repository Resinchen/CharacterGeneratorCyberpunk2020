from enum import Enum

from src.utils import roll_10, roll_to_type

Sex = Enum("Sex", "MALE FEMALE")
RollToSex = roll_to_type({Sex.MALE: [2, 4, 6, 8, 10], Sex.FEMALE: [1, 3, 5, 7, 9]})


def get_random_sex() -> Sex:
    return RollToSex[roll_10()]
