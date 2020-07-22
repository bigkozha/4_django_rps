from selenium.webdriver.support.ui import Select


def test_main(live_server, driver, logged_user1):
    driver.get(live_server.url)
    button_new_game = driver.find_element_by_css_selector('[data-test="new_game"]')

    assert button_new_game is not None


def test_new_game(live_server, driver, logged_user1):
    driver.get(live_server.url+'/new_game/')

    Select(driver.find_element_by_css_selector('[data-test="player2"]')).select_by_visible_text('user2')
    driver.find_element_by_css_selector('[data-test="start"]').click()

    assert 'game_detail/1' in driver.current_url


def test_move(live_server, driver, logged_user1, default_game):
    driver.get(live_server.url+'/game_detail/1')

    Select(driver.find_element_by_css_selector('[data-test="move_kind"]')).select_by_visible_text('Papper')
    driver.find_element_by_css_selector('[data-test="submit"]').click()

    submited_item = driver.find_elements_by_css_selector('[data-test="move_item"]')[0].text

    assert 'Papper' in submited_item
    assert 'user1' in submited_item


def test_move_second_time_same_user_fail(live_server, driver, logged_user1, default_game):
    driver.get(live_server.url+'/game_detail/1')
    Select(driver.find_element_by_css_selector('[data-test="move_kind"]')).select_by_visible_text('Papper')
    driver.find_element_by_css_selector('[data-test="submit"]').click()

    submited_item = driver.find_elements_by_css_selector('[data-test="move_item"]')[0].text

    assert 'Papper' in submited_item
    assert 'user1' in submited_item

    Select(driver.find_element_by_css_selector('[data-test="move_kind"]')).select_by_visible_text('Papper')
    driver.find_element_by_css_selector('[data-test="submit"]').click()

    assert 'error' in driver.current_url


def test_game_end(live_server, driver, logged_user2, default_five_moves):
    driver.get(live_server.url+'/game_detail/1')
    Select(driver.find_element_by_css_selector('[data-test="move_kind"]')).select_by_visible_text('Stone')
    driver.find_element_by_css_selector('[data-test="submit"]').click()

    submited_item = driver.find_elements_by_css_selector('[data-test="move_item"]')[-1].text
    win_text = driver.find_element_by_css_selector('[data-test="is_over"]').text

    assert 'Stone' in submited_item
    assert 'user2' in submited_item
    assert 'The game is over. Winner user2' in win_text
