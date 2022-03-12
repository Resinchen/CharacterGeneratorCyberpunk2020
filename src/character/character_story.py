from typing import Optional

from src.event import Event
from src.family import Family
from src.utils import roll_10
from src.utils.human import Sex
Wear = {
    1: "Байкерская кожа",
    2: "Джинсовый стиль",
    3: "Деловой костюм",
    4: "Спортивный костюм",
    5: "Мини-юбка",
    6: "Высокая мода",
    7: "Комбинизон",
    8: "Обычная одежда",
    9: "Обнаженный",
    10: "Вульгарная",
}
Hair = {
    1: "Ирокез",
    2: "Длинные крысиные",
    3: "Короткие шипами",
    4: "Торчащие/вьющиеся",
    5: "Лысый",
    6: "Полосками",
    7: "Раскрашенные",
    8: "Акуратные, короткие",
    9: "Короткие",
    10: "Длинные, прямые",
}
Salt = {
    1: "Татуировки",
    2: "Зеркальные очки",
    3: "Ритуальные шрамы",
    4: "Шипастые перчатки",
    5: "Кольцо в носу",
    6: "Серьги в ушах",
    7: "Длинные ногти",
    8: "Ботинки с шипами на подошве",
    9: "Причудливые контактные линзы",
    10: "Перчатки без пальце",
}


class Fashion:
    def __init__(self):
        self.wear: str = Wear[roll_10()]
        self.hair: str = Hair[roll_10()]
        self.salt: str = Salt[roll_10()]

    def __str__(self) -> str:
        return f"Ты одет в {self.wear}, на голове у тебя {self.hair} и у тебя {self.salt}."


Ethnic = {
    1: "англо-американец",
    2: "африканец",
    3: "японец",
    4: "из центральной европы",
    5: "с островов тихого океана",
    6: "из северной азии",
    7: "черный америкаец",
    8: "латиноамериканец",
    9: "из центральной америки",
    10: "европеец",
}
Language = {
    1: "английском",
    2: "конго",
    3: "японском",
    4: "русском",
    5: "гавайском",
    6: "китайском",
    7: "черном фольке",
    8: "испанском",
    9: "португальском",
    10: "немецком",
}


class National:
    def __init__(self):
        self.country: str = Ethnic[roll_10()]
        self.language: str = Language[roll_10()]

    def __str__(self) -> str:
        return f"Ты {self.country} и говоришь на {self.language}."


PersonalityStrait = {
    1: "Недоверчивый и замкнутый",
    2: "Вспыльчивый, антиобщественный бунтарь",
    3: "Заносчивый, надменный гордец",
    4: "Своенравный, активный, легок на подъем",
    5: "Требовательный, вычурный, нервный",
    6: "Серьезный, постоянный",
    7: "Простой, бесхитростный, безобидный",
    8: "Трусливый лгун",
    9: "Обособленный интеллигент",
    10: "Дружелюбный и отзывчивый",
}
Idol = {
    1: "Мать/Отец",
    2: "Брат/Сестра",
    3: "Любовник/Любовница",
    4: "Друг/Подруга",
    5: "Себя любимого",
    6: "Домашнее Животное",
    7: "Учитель/Наставник",
    8: "Знаменитость",
    9: "Личный кумир",
    10: "Никого",
}
Preference = {
    1: "Деньги",
    2: "Честь",
    3: "Свой Мир",
    4: "Честность",
    5: "Знания",
    6: "Вендетту",
    7: "Любовь",
    8: "Власть",
    9: "Хорошее времепровождение",
    10: "Дружбу",
}
Treasure = {
    1: "Оружие",
    2: "Инструмент",
    3: "Часть одежды",
    4: "Фотография",
    5: "Книга или дневник",
    6: "Аудио или видео запись",
    7: "Музыкальный инструмент",
    8: "Ювелирное / драгоценное изделие",
    9: "Игрушка",
    10: "Письмо / записка",
}
Social = {
    1: "Нейтрально",
    2: "Нейтрально",
    3: "Любишь почти всех",
    4: "Ненавидишь почти всех",
    5: "Люди это инструмент. Используешь их для своих нужд, а потом выбрасываешь",
    6: "Каждый человек - драгоценная индивидуальность",
    7: "Люди это препятствие, которое ты уничтожаешь если они мешают",
    8: "Люди ненадежны. На них нельзя полагаться.",
    9: "Размазать их всех, освободив место для тараканов",
    10: "Люди прекрасны",
}


class Personality:
    def __init__(self):
        self.personality_strait: str = PersonalityStrait[roll_10()]
        self.idol: str = Idol[roll_10()]
        self.preference: str = Preference[roll_10()]
        self.treasure: str = Treasure[roll_10()]
        self.social: str = Social[roll_10()]

    def __str__(self) -> str:
        return (
            f"Ты довольно {self.personality_strait}. Ты больше всего ценишь {self.idol}. "
            f"Для тебя довольно важно {self.preference}. Ты относишься к людям как {self.social} "
            f"Самый значимый для тебя предмет {self.treasure}."
        )


class CharacterStory:
    def __init__(self, name: str, sex: Sex):
        self.name: str = name
        self.sex: Sex = sex
        self.age: int = 17
        self.fashion: Optional[Fashion] = None
        self.national: Optional[National] = None
        self.personality: Optional[Personality] = None
        self.family: Optional[Family] = None
        self.events: dict[int, Event] = {}

    def __str__(self) -> str:
        result = (
            f"Ты {self.sex} и тебя зовут {self.name}\nТебе {self.age} лет. \n"
            f"{self.fashion}\n\n"
            f"{self.national}\n\n"
            f"{self.personality}\n\n"
            f"{self.family}\n\n"
            f"За последние {self.age - 17} лет с тобой произошло следующее:"
        )
        for year, event in self.events.items():
            result += f"\n\t {year + 17} лет: {event}"

        return result

    def set_family(self, family: Family) -> None:
        self.family = family

    def set_fashion(self, fashion: Fashion) -> None:
        self.fashion = fashion

    def set_national(self, national: National) -> None:
        self.national = national

    def set_personality(self, personality: Personality) -> None:
        self.personality = personality

    def set_age(self, years: int) -> None:
        self.age += years

    def add_events(self, age: int, event: Event) -> None:
        self.events[age] = event
