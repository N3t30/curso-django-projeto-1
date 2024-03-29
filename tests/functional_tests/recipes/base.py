import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from recipes.templates.recipes.tests.test_recipe_base import RecipeMixin
from utils.browser import make_chrome_browser


class RecipesbaseFunctionalTest(StaticLiveServerTestCase, RecipeMixin):
    def setUp(self) -> None:  # responsavel por criar o browser
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:  # Responsavel por matar o browser
        self.browser.quit()
        return super().tearDown()

    def sleep(self, seconds=6):
        time.sleep(seconds)
