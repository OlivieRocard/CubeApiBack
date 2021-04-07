from enum import Enum


class CategoryEnum(str, Enum):
    COMMUNICATION = '1'
    CULTURES = '2'
    LOISIRS = '3'
    MONDE_PRO = '4'
    PARENTALITE = '5'
    SANTE_PHYSIQUE = '6'
    VIE_AFFECTIVE = '7'
