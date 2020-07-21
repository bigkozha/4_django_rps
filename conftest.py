
import os

import pytest
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.yield_fixture(scope="session")
def driver():
    if os.environ.get('GITHUB_ACTIONS'):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        with webdriver.Chrome(chrome_options=chrome_options) as driver:
            yield driver
    else:
        with webdriver.Remote(command_executor='http://127.0.0.1:9515') as driver:
            yield driver


@pytest.fixture
def user_client(client, live_server, driver):
    user = User.objects.create_user(
        username='user',
        password='pass',
    )

    driver.get(live_server.url)
    username = driver.find_element_by_css_selector('[data-test="username"]')
    username.send_keys("user")
    password = driver.find_element_by_css_selector('[data-test="password"]')
    password.send_keys("pass")
    submit = driver.find_element_by_css_selector('[data-test="submit"]')
    submit.click()

    return user_client

@pytest.fixture
def default_users():
    user = User.objects.create(
        username='user1',
        password='pass1'
    )
