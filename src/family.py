from src.utils import Sex, get_random_sex, roll_10, roll_great

AgeRelativeCharacter = {
    1: "старше тебя",
    2: "старше тебя",
    3: "старше тебя",
    4: "старше тебя",
    5: "старше тебя",
    6: "младше тебя",
    7: "младше тебя",
    8: "младше тебя",
    9: "младше тебя",
    10: "твой близнец",
}
SiblingReaction = {
    1: "которому ты не нравишься",
    2: "которому ты не нравишься",
    3: "которому ты нравишься",
    4: "которому ты нравишься",
    5: "который относится к тебе спокойно",
    6: "который относится к тебе спокойно",
    7: "для которого ты персональный герой",
    8: "для которого ты персональный герой",
    9: "который ненавидит тебя",
    10: "который ненавидит тебя",
}


class Sibling:
    def __init__(self):
        self.sex: str = "Брат" if get_random_sex() == Sex.MALE else "Сестра"
        self.age: str = AgeRelativeCharacter[roll_10()]
        self.relation_for_you: str = SiblingReaction[roll_10()]

    def __str__(self) -> str:
        return f'{self.sex}, котор{"ый" if self.sex == "Брат" else "ая"} {self.age} и {self.relation_for_you}'


RankFamily = {
    1: "Корпоративное управление",
    2: "Менеджеры корпорации",
    3: "Техники корпорации",
    4: "Банда кочевников",
    5: "Пираты",
    6: "Гангстерская семья",
    7: "Лорды преступности",
    8: "Нищие жители боевой зоны",
    9: "Городские Бездомные",
    10: "Археологи",
}
ParentsStatus = {
    1: "Погибли на войне",
    2: "Погибли в катастрофе",
    3: "Убиты",
    4: "Амнезия, не помнят тебя",
    5: "Никогда их не знал",
    6: "Скрываются защищая тебя",
    7: "Брошен с родственниками на произвол судьбы",
    8: "Вырос на улице без родителей",
    9: "Отдан на усыновление",
    10: "Продали тебя за деньги",
}
FamilyTragedy = {
    1: "Семья потеряла все в результате предательства",
    2: "Семья потеряла все в результате плохого управления",
    3: "Семья сослана, или как-то еще выселена с места обитания",
    4: "Семья в тюрьме, ты один избежал правосудия",
    5: "Семья пропала без вести, ты единственный известный член семьи",
    6: "Семья уничтожена, ты единственный выживший",
    7: "Семья втянута в заговор или революционную деятельность",
    8: "Семья разбросана по миру, волей судьбы",
    9: "Семья находится в состоянии постоянного конфликта который тянется из поколения в поколение",
    10: "Вы “унаследовали” семейный долг, вам надо оплатить его.",
}
Childhood = {
    1: "на улице, без присмотра",
    2: "в безопасном корпоративном пригородном поселении",
    3: "в банде кочевников, ездил из города в город",
    4: "в загнивающих слоях, высшее общество",
    5: "в защищенной корпоративной зоне, в центре города",
    6: "в сердце боевой зоны",
    7: "в небольшой деревушки или поселке, далеко от города",
    8: "в большом археологическом городе",
    9: "в акваториальной пиратской банде",
    10: "на ферме или исследовательской платформе корпорации",
}
CountSiblings = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 0, 9: 0, 10: 0}


class Family:
    def __init__(self):
        self.rank: str = RankFamily[roll_10()]
        self.parent_status: str = ParentsStatus[roll_10()] if roll_great(6) else None
        self.family_tragedy: str = FamilyTragedy[roll_10()] if roll_great(6) else None
        self.childhood: str = Childhood[roll_10()]
        self.siblings: list[Sibling] = []
        for _ in range(CountSiblings[roll_10()]):
            self.siblings.append(Sibling())

    def __str__(self) -> str:
        siblings_str: str = "\n\t".join(map(str, self.siblings))
        return (
            f"Твоя семья - {self.rank}.\n"
            f"С твоими родителями произошло - {self.parent_status}\n"
            f"С твоей семьей произошло - {self.family_tragedy}\n"
            f"Твое детство прошло {self.childhood}\n"
            f"Твои родственники({len(self.siblings)}):\n"
            f"\t{siblings_str}"
        )