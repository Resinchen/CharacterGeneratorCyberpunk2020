from src.character.character_story import CharacterStory, Fashion, National, Personality
from src.event import Event, EventType, RollToEvent
from src.events import Fact, Friends, Romantic
from src.family import Family
from src.utils import roll_6, roll_10
from src.utils.human import Sex

class CharacterFactory:
    @staticmethod
    def make_character(name: str, sex: Sex) -> CharacterStory:
        character: CharacterStory = CharacterStory(name, sex)
        character.set_fashion(Fashion())
        character.set_national(National())
        character.set_family(Family())
        character.set_personality(Personality())

        age: int = roll_6() + roll_6()
        character.set_age(age)

        for year in range(age):
            event_type = RollToEvent[roll_10()]
            event = Event()
            if event_type == EventType.FACT:
                event = Fact()
            elif event_type == EventType.FRIENDS:
                event = Friends()
            elif event_type == EventType.ROMANTIC:
                event = Romantic()
            character.add_events(year, event)

        return character
