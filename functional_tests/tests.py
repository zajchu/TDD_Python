from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
import unittest
import time


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_row_for_in_list_table(self, row_text: str):
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.live_server_url)

        self.assertIn('Listy', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('lista', header_text)

        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'),
                         'Wpisz rzeczy do zrobienia')

        input_box.send_keys('Kupic pawie piora')
        input_box.send_keys(Keys.ENTER)
        edith_st_url = self.browser.current_url
        self.assertRegex(edith_st_url, '/lists/.+')
        self.check_row_for_in_list_table('1: Kupic pawie piora')

        input_box = self.browser.find_element_by_id('id_new_item')
        input_box.send_keys('Uzyc pawich pior do zrobienia przynety')
        input_box.send_keys(Keys.ENTER)

        self.check_row_for_in_list_table('1: Kupic pawie piora')
        self.check_row_for_in_list_table('2: Uzyc pawich pior do zrobienia przynety')

        self.fail("Zakończenie testu")




if __name__ == '__main__':
    unittest.main(warnings='ignore')
