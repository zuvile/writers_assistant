from .declension import decline
from .documents import ParagraphDocument
from .models import Novel
from elasticsearch_dsl import Q


def get_character_search_results(name, novel):
    name_declinations = decline(name)
    #todo filter by novel
    novel = Novel.objects.get(novel_name=novel, author_id=1)
    results = []
    should = []
    s = ParagraphDocument.search().extra(size=3000)
    s = s.sort({
        "id": {
            "order": "asc"
        },
    })
    for declination in name_declinations:
        should.append(Q('match', text=declination))

    s.query = Q('bool', should=should)

    hits = s.execute()
    for hit in hits:
        results.append(hit.text)

    return len(results), results
