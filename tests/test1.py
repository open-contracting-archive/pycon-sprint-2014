import unittest
import codecs 
from google_translate_py2_funcs import get_trans_, get_lang_list, get_possible_lang

class TestTranslateFuncs(unittest.TestCase):
	def setUp(self):
		self.api_key = "AIzaSyCZBVx2a3tzKTW9TmTXoB3KJ_Z7T9PEspE"
		self.api_key_unic = "AIzaSyCZBVx2a3tzKTW9TmTXoB3KJ_Z7T9PEspE"
		self.text_French = "La litterature francaise comprend l"
		self.text_German = "Contracting (englisch die Kontrahierung bzw. adjektivisch vertragschlieend)"
		self.text_Georgian = "გამარტივებული ელექტრონული ტენდერი; კონსოლიდირებული ტენდერი; ელექტრონული ტენდერი; შესყიდვის ელექტრონული პროცედურა".encode('utf-8')
		pass


	def test_get_trans_(self):
		pass

	def test_get_lang_list(self):
		self.assertEqual([u'fr', u'de'], get_lang_list([self.text_French, self.text_German]))
		pass

	def test_get_possible_lang():
		pass

if __name__ == '__main__':
	unittest.main()

