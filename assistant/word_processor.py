import textract
from .generic_processor import process_paragraphs

def process_word(file, novel_id):
    try:
        text = textract.process(file, encoding='utf-8', output_encoding='utf-8')
        text = text.decode('utf-8')
        process_paragraphs(text.splitlines(), novel_id=novel_id)
        file.close()
    except Exception as e:
        return -1
