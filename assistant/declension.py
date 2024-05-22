import re

_cases = {
    "vardininkas": "nominative",
    "kilmininkas": "genitive",
    "Naudininkas": "dative",
    "Galininkas": "accusative",
    "Įnagininkas": "instrumentative",
    "Vietininkas": "locative",
    "Šauksmininkas": "exclamatory",
}


def decline(word):
    results = []
    for lt_case, case in _cases.items():
        patterns = get_pattern(case)
        for pattern, replacement in patterns.items():
            pattern = pattern + '$'
            if re.search(pattern, word):
                result = re.sub(pattern, replacement, word)
                results.append(result)
                break

    return results


def get_pattern(declension):
    if declension == 'nominative':
        return {
            '': ''
        }
    if declension == 'genitive':
        return {
            'a': 'os',
            'as': 'o',
            'ė': 'ės',
            'tis': 'čio',
            'dis': 'džio',
            'vis': 'vies',
            'is': 'io',
            'us': 'aus',
            'tys': 'čio',
            'dys': 'džio',
            'ys': 'io',
        }
    if declension == 'dative':
        return {
            'a': 'ai',
            'as': 'ui',
            'ė': 'ei',
            'tis': 'čiui',
            'dis': 'džiui',
            'vis': 'viai',
            'is': 'iui',
            'us': 'ui',
            'tys': 'čiui',
            'dys': 'džiui',
            'ys': 'iui'
        }
    if declension == 'accusative':
        return {
            'a': 'ą',
            'as': 'ą',
            'ė': 'ę',
            'is': 'į',
            'us': 'ų',
            'ys': 'į'
        }
    if declension == 'instrumentative':
        return {
            'a': 'a',
            'as': 'u',
            'ė': 'e',
            'tis': 'čiu',
            'dis': 'džiu',
            'vis': 'vimi',
            'ius': 'iumi',
            'jus': 'jumi',
            'is': 'iu',
            'us': 'u',
            'tys': 'čiu',
            'dys': 'džiu',
            'ys': 'iu'
        }
    if declension == 'locative':
        return {
            'a': 'oje',
            'as': 'e',
            'ė': 'ėje',
            'is': 'yje',
            'us': 'uje',
            'ys': 'yje'
        }
    if declension == 'exclamatory':
        return {
            'a': 'a',
            'nas': 'ne',
            'as': 'ai',
            'ė': 'e',
            'vis': 'vie',
            'is': 'i',
            'us': 'au',
            'ys': 'y'
        }