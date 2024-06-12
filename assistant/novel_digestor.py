from .models import Chapter, Character, Paragraph, Portrait
from .ai_summarizer import AiSummarizer


class NovelDigestor:
    #todo rename
    def summarise(self, novel_id):
        ai_summarizer = AiSummarizer()

        chapter_ids = self.get_chapter_ids(novel_id)

        for chapter_id in chapter_ids:
            chapter = Chapter.objects.get(id=chapter_id)
            if chapter.word_count == 0:
                continue
            text = self.get_chapter_text(chapter_id)
            summary = ai_summarizer.get_chapter_summary(text)
            characters = ai_summarizer.get_characters(text)
            chapter.summary = summary
            for character in characters:
                chapter.characters.add(self.upsert_character(character, novel_id, text))
            chapter.save()

    def upsert_character(self, character_name, novel_id, text):
        character = Character.objects.filter(name=character_name).first()
        ai_summarizer = AiSummarizer()
        # todo extract other qualities such as age, gender
        if character is None:
            description = ai_summarizer.describe_character(character_name, text)
            character = Character.objects.create(name=character_name, age=20, description=description, gender="unknown")
            character.save()
            portrait = Portrait.objects.create(character=character, url="default_profile.jpg", active=True)
            portrait.save()
        character.novels.add(novel_id)
        character.save()

        return character

    def get_chapter_ids(self, novel_id):
        chapter_ids = Chapter.objects.filter(novel_id=novel_id).values_list('id', flat=True)

        return chapter_ids

    def get_chapter_text(self, chapter_id):
        paragraphs = Paragraph.objects.filter(chapter_id=chapter_id).all()
        text = ""

        for paragraph in paragraphs:
            text += paragraph.text + "\n"

        return text