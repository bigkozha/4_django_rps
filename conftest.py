import os

import pytest
from django.contrib.auth.models import User
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from game.models import Game, Move, MoveKind


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
def logged_user1(live_server, driver, default_users):
    driver.get(live_server.url)
    username = driver.find_element_by_css_selector('[data-test="username"]')
    username.send_keys("user1")
    password = driver.find_element_by_css_selector('[data-test="password"]')
    password.send_keys("pass1")
    submit = driver.find_element_by_css_selector('[data-test="submit"]')
    submit.click()


@pytest.fixture
def logged_user2(live_server, driver, default_users):
    driver.get(live_server.url)
    username = driver.find_element_by_css_selector('[data-test="username"]')
    username.send_keys("user2")
    password = driver.find_element_by_css_selector('[data-test="password"]')
    password.send_keys("pass2")
    submit = driver.find_element_by_css_selector('[data-test="submit"]')
    submit.click()


@pytest.fixture
def default_users():
    User.objects.create_user(
        username='user1',
        password='pass1'
    )
    User.objects.create_user(
        username='user2',
        password='pass2'
    )


@pytest.fixture
def default_game(default_users, default_move_kinds):
    instance = Game.objects.create(is_active=True, player1=User.objects.get(pk=1), player2=User.objects.get(pk=2))
    assert instance.id == 1
    return instance


@pytest.fixture
def default_move_kinds():
    MoveKind.objects.create(name='Papper')
    MoveKind.objects.create(name='Scissors')
    MoveKind.objects.create(name='Stone')


@pytest.fixture
def default_five_moves(default_game):
    Move.objects.create(game=default_game, gamer=User.objects.get(pk=1), move_kind=MoveKind.objects.get(pk=1))
    Move.objects.create(game=default_game, gamer=User.objects.get(pk=2), move_kind=MoveKind.objects.get(pk=3))
    Move.objects.create(game=default_game, gamer=User.objects.get(pk=1), move_kind=MoveKind.objects.get(pk=1))
    Move.objects.create(game=default_game, gamer=User.objects.get(pk=2), move_kind=MoveKind.objects.get(pk=3))
    Move.objects.create(game=default_game, gamer=User.objects.get(pk=1), move_kind=MoveKind.objects.get(pk=1))
