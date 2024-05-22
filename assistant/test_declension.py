from django.test import TestCase
from .declension import decline


class UploadProcessorTest(TestCase):
    def test_decline_nouns(self):
        expected = ['apelsinas', 'apelsino', 'apelsinui', 'apelsiną', 'apelsinu', 'apelsine', 'apelsine']
        self.assertEquals(decline('apelsinas'), expected)

        expected = ['kiaušinis', 'kiaušinio', 'kiaušiniui', 'kiaušinį', 'kiaušiniu', 'kiaušinyje', 'kiaušini']
        self.assertEquals(decline('kiaušinis'), expected)

        expected = ['obuolys', 'obuolio', 'obuoliui', 'obuolį', 'obuoliu', 'obuolyje', 'obuoly']
        self.assertEquals(decline('obuolys'), expected)

        expected = ['citrina', 'citrinos', 'citrinai', 'citriną', 'citrina', 'citrinoje', 'citrina']
        self.assertEquals(decline('citrina'), expected)

        expected = ['daržovė', 'daržovės', 'daržovei', 'daržovę', 'daržove', 'daržovėje', 'daržove']
        self.assertEquals(decline('daržovė'), expected)

        expected = ['žuvis', 'žuvies', 'žuviai', 'žuvį', 'žuvimi', 'žuvyje', 'žuvie']
        self.assertEquals(decline('žuvis'), expected)

        expected = ['skaičius', 'skaičiaus', 'skaičiui', 'skaičių', 'skaičiumi', 'skaičiuje', 'skaičiau']
        self.assertEquals(decline('skaičius'), expected)

    def test_decline_names(self):
        expected = ['Klaudijus', 'Klaudijaus', 'Klaudijui', 'Klaudijų', 'Klaudijumi', 'Klaudijuje', 'Klaudijau']
        self.assertEquals(decline('Klaudijus'), expected)

        expected = ['Helena', 'Helenos', 'Helenai', 'Heleną', 'Helena', 'Helenoje', 'Helena']
        self.assertEquals(decline('Helena'), expected)

        expected = ['Herakas', 'Herako', 'Herakui', 'Heraką', 'Heraku', 'Herake', 'Herakai']
        self.assertEquals(decline('Herakas'), expected)

