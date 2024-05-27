from .declension import decline
from .documents import ParagraphDocument
from .models import Novel
from elasticsearch_dsl import Q


def search(search_term, novels):
    #todo filter by novel
    should = []
    s = ParagraphDocument.search().extra(size=3000)
    s = s.sort({
        "id": {
            "order": "asc"
        },
    })

    should.append(Q('match', text=search_term))

    s.query = Q('bool', should=should)
    results = []
    hits = s.execute()
    for hit in hits:
        results.append(hit.text)

    return len(results), results
