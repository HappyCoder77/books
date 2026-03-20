from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import HomePageView


class HomePageTests(SimpleTestCase):

    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_homepage_contains_correct_HTML(self):
        self.assertContains(self.response, "Homepage")

    def test_homepage_doesnt_contains_incorrect_HTML(self):
        self.assertNotContains(self.response, "Hi there!")

    def test_homepage_url_resoves_to_homepageview(self):
        view = resolve("/")

        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
