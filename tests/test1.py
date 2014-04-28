# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
import codecs
from translation.google_tranlate_py2_funcs import (
    get_trans_,
    get_lang_list,
    get_possible_langs
)
from .api_key import API_KEY


class TestTranslateFuncs(unittest.TestCase):
    def setUp(self):
        self.api_key = API_KEY
        self.text_French = "La litterature francaise comprend l"
        self.text_German = "Contracting (englisch die Kontrahierung bzw. adjektivisch vertragschlieend)"  # nopep8
        self.text_Georgian = "გამარტივებული ელექტრონული ტენდერი; კონსოლიდირებული ტენდერი; ელექტრონული ტენდერი; შესყიდვის ელექტრონული პროცედურა"  # nopep8

    def test_get_trans_(self):
        pass

    def test_get_lang_list(self):
        self.assertEqual([u'fr', u'de'],
                         get_lang_list([self.text_French, self.text_German],
                                       self.api_key))

    def test_get_possible_lang(self):
        pass

if __name__ == '__main__':
    """
    To run these tests:
        - in the tests directory, create a file called api_key.py and enter
        your google translate api_key on a line `API_KEY = "myapikey"`
        - then from the parent directory (root of pycon-sprint-2014)
        use `python -m tests.test1`
    """
    unittest.main()
