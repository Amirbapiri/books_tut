from django.test import SimpleTestCase
from django.urls import reverse, resolve

from pages.views import HomePageView


class HomePageTests(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse("home")
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_home_page_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "Homepage")

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get("/")
        self.assertNotContains(response, "Hi There! I should not be in the page.")

    def test_home_page_url_resolves_home_page_view(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__
        )
