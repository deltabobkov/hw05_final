from http import HTTPStatus

from django.test import Client, TestCase


class StaticPagesURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.pages = [
            "/about/author/",
            "/about/tech/",
        ]

        cls.templates_url_names = {
            "/about/author/": "about/author.html",
            "/about/tech/": "about/tech.html",
        }

    def setUp(self):
        self.guest_client = Client()

    def test_static_url_exists(self):
        """Проверка доступности статичных страниц."""
        for address in self.pages:
            with self.subTest(address):
                response = self.guest_client.get(address)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_url_uses_correct_template(self):
        """Проверка шаблонов статичных страниц"""
        for address, template in self.templates_url_names.items():
            with self.subTest(template=template):
                response = self.guest_client.get(address)
                self.assertTemplateUsed(response, template)
