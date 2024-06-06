from .ai_gen import get_portrait
from .models import Character, Novel, Portrait
import logging


def create_portrait(character: Character):
    novel = character.novels.all().first()

    if novel is None:
        logging.error("Character does not have a novel")
        return None

    url = get_portrait(character.age, character.description, character.gender, novel.genre)

    portrait = Portrait.objects.create(character=character, url=url)
    portrait.active = True
    portrait.save()

    return portrait