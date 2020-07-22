import pytest
from selenium.webdriver.support.ui import Select


def test_main(live_server, driver):
    driver.get(live_server.url)
    button_new_game = driver.find_element_by_css_selector('[data-test="new_game"]')

    assert button_new_game is not None


def test_new_game(live_server, driver, default_users):
    driver.get(live_server.url+'/new_game/')

    Select(driver.find_element_by_css_selector('[data-test="player2"]')).select_by_visible_text('user2')
    driver.find_element_by_css_selector('[data-test="start"]').click()

    assert 'game_detail' in driver.current_url
