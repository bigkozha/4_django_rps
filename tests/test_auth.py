def test_auth_fail(live_server, driver):
    driver.get(live_server.url + '/accounts/login/')

    username = driver.find_element_by_css_selector('[data-test="username"]')
    username.send_keys("user")
    password = driver.find_element_by_css_selector('[data-test="password"]')
    password.send_keys("pass")
    submit = driver.find_element_by_css_selector('[data-test="submit"]')
    submit.click()

    assert 'accounts/login/' in driver.current_url