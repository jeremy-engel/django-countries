from django_countries import settings
from django_countries.utils.tests import TempAppTestCase


class TestCountryField(TempAppTestCase):
    test_apps = (
        'django_countries.tests.countries_test',
    )

    def create_person(self, country='NZ'):
        from django_countries.tests.countries_test.models import Person
        return Person.objects.create(name='Chris Beaven', country=country)

    def test_logic(self):
        person = self.create_person()

        self.assertEqual(person.country, 'NZ')
        self.assertNotEqual(person.country, 'ZZ')

        self.assert_(person.country < 'OA')
        self.assert_(person.country > 'NY')

        self.assert_(person.country)
        person.country = ''
        self.assertFalse(person.country)

    def test_unicode(self):
        person = self.create_person()
        self.assertEqual(unicode(person.country), 'NZ')

    def test_name(self):
        person = self.create_person()
        self.assertEqual(person.country.name, u'New Zealand')

    def test_flag(self):
        person = self.create_person()
        expected_url = settings.FLAG_URL % {'code': 'nz', 'code_upper': 'NZ'}
        self.assertEqual(person.country.flag, expected_url)

    def test_blank(self):
        from django_countries.tests.countries_test.models import Person
        person = self.create_person(country=None)
        self.assertEqual(person.country, '')

        person = Person.objects.get(pk=person.pk)
        self.assertEqual(person.country, '')
