from src.character.character_story import CharacterStory
from src.character_factory import CharacterFactory
from src.utils.human import Sex

if __name__ == "__main__":
    c: CharacterStory = CharacterFactory.make_character("Roland", Sex.MALE)
    print(c)
