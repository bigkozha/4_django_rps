import pytest

def test_main(live_server, driver):
    driver.get(live_server.url)
    button_new_game = driver.find_element_by_css_selector('[data-test="new_game"')

    assert button_new_game is not None