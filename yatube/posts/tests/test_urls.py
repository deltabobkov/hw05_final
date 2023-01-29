from http import HTTPStatus

from django.core.cache import cache
from django.test import Client, TestCase

from ..models import Group, Post, User


class PostURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username="user1")
        cls.user_1 = User.objects.create_user(username="HasNoName")
        cls.group = Group.objects.create(
            title="Тестовая группа",
            slug="test-slug",
            description="Тестовое описание",
        )
        cls.post = Post.objects.create(
            author=cls.user,
            text="Тестовый пост",
        )
        cls.templates = [
            "/",
            f"/group/{cls.group.slug}/",
            f"/posts/{cls.post.id}/",
            f"/profile/{cls.user}/",
        ]
        cls.templates_url_names = {
            "/": "posts/index.html",
            f"/group/{cls.group.slug}/": "posts/group_list.html",
            f"/posts/{cls.post.id}/": "posts/post_detail.html",
            f"/profile/{cls.user.username}/": "posts/profile.html",
            "/create/": "posts/create_post.html",
            f"/posts/{cls.post.id}/edit/": "posts/create_post.html",
        }

    def setUp(self):
        cache.clear()
        self.guest_client = Client()
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user_1)
        self.author_client = Client()
        self.author_client.force_login(PostURLTests.user)

    def test_urls_exists(self):
        """Проверка доступности страниц любому пользователю."""
        for address in self.templates:
            with self.subTest(address):
                response = self.guest_client.get(address)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_not_found(self):
        """Проверка несуществующей страницы"""
        response = self.guest_client.get("/not_avaliable_url/")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test_url_create_for_authorized(self):
        """Проверка доступа к странице создания поста"""
        response = self.authorized_client.get("/create/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_edit_post_for_author(self):
        """Страница редактирования поста доступна только автору"""
        response = self.author_client.get(f"/posts/{self.post.id}/edit/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_url_create_redirect(self):
        """Страница create перенаправит анонима
        на страницу логина
        """
        response = self.guest_client.get("/create/", follow=True)
        self.assertRedirects(response, "/auth/login/?next=/create/")

    def test_urls_uses_correct_template(self):
        """URL-адрес использует соответствующий шаблон."""
        for address, template in self.templates_url_names.items():
            with self.subTest(template=template):
                response = self.author_client.get(address)
                self.assertTemplateUsed(response, template)

    def test_404_correct_template(self):
        """Страница 404 использует соответствующий шаблон."""
        response = self.guest_client.get("/nowhere/")
        self.assertTemplateUsed(response, "core/404.html")


class StaticURLTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_homepage(self):
        response = self.guest_client.get("/")
        self.assertEqual(response.status_code, HTTPStatus.OK)
