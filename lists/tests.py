from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


# Create your tests here.

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_views(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_home_page_can_save_a_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        post_value = 'Nowy element listy'
        request.POST['item_text'] = post_value
        expected_html = render_to_string('home.html', {'new_item_text': post_value})

        response = home_page(request)

        self.assertIn(post_value, response.content.decode())
        self.assertEqual(response.content.decode(), expected_html)
