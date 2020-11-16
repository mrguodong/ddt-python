from selenium import webdriver
import unittest


class NewVistorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retriveve_it_later(self):

        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        # header_text = self.browser.find_element_by_tag_name('h1').text
        # self.assertIn('To-Do', header_text)
        #
        # # She is invited to enter a to-do item straight away
        # inputbox = self.browser.find_element_by_id('id_new_item')
        # self.assertEqual(
        #     inputbox.get_attribute(
        #         'placeholder'
        #     ),
        #     'Enter a to-do item'
        # )

        # self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')