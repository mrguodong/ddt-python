from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retriveve_it_later(self):

        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get('http://127.0.0.1:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute(
                'placeholder'
            ),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobyy
        # is tying fly-fishing lures)
        inputbox.send_keys("1: Buy peacock feathers")
        time.sleep(2)

        # when she hits enter , the page updates, and now the page lists
        # "1: But peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            f"New to-do item did not appear in table. Contents were:\n{table.text}"
        )
        # There is stil a text box inviting her to add another items.
        # She enters "Use peacock feathers to make a fly"
        # (Edith is very methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys("2: Use peacock feathers to make a fly")
        time.sleep(2)
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        # The page updates again , and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            f"1: Buy peacock feathers  did not appear in table. Contents were:\n{table.text}"
        )
        self.assertTrue(
            any(row.text == '2: Use peacock feathers to make a fly' for row in rows),
            f"2: Use peacock feathers to make a fly did not appear in table. Contents were:\n{table.text}"
        )


        # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')