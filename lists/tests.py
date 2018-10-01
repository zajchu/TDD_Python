from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.db import models

from lists.views import home_page
from lists.models import Item


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


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item: models.Model = Item()
        first_item.text = 'Absolutnie piesrwszy element listy'
        first_item.save()

        second_item: models.Model = Item()
        second_item.text = 'Drugi element'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'Absolutnie piesrwszy element listy')
        self.assertEqual(second_saved_item.text, 'Drugi element')
