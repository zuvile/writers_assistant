from .generic_processor import process_paragraphs

def process_txt(file, novel_id):
    data = file.read().decode("utf-8")
    process_paragraphs(data.splitlines(), novel_id=novel_id)
    file.close()


