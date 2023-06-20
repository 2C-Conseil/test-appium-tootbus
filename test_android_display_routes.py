from .generic import first_stages_selector, wait_and_click, are_elements_displayed, is_element_displayed, get_rgb_by_coordinates
from selenium.common import NoSuchElementException


def test_android_display_routes():
    # Android environment
    from appium import webdriver
    # Options are only available since client version 2.3.0
    from appium.options.android import UiAutomator2Options
    from appium.webdriver.common.appiumby import AppiumBy
    from appium.webdriver.common.touch_action import TouchAction
    from appium.webdriver.common.multi_action import MultiAction
    import pathlib
    import time
    import socket
    from mitmproxy import http
    import logging
    from datetime import datetime
    import pytz

    logging.basicConfig(level=logging.INFO)
    logging.basicConfig(filename='android.log', level=logging.INFO)

    options = UiAutomator2Options()
    options.platformVersion = '9'
    options.udid = 'emulator-5554'
    options.app = "C:/Users/Elite/Desktop/tootbus_latest.apk"

    driver = webdriver.Remote('http://localhost:4723/wd/hub', options=options)

    driver.implicitly_wait(12)

    first_stages_selector(driver)

    time.sleep(20)
    element = driver.find_element(AppiumBy.ID, "com.ratpdev.esight.debug:id/map_clicker")
    action = TouchAction(driver)
    action.tap(element).release().perform()

    wait_and_click(driver, (AppiumBy.ID, 'com.ratpdev.esight.debug:id/image_maptype'))

    driver.implicitly_wait(12)
    elements = driver.find_elements(by=AppiumBy.ID, value="com.ratpdev.esight.debug:id/tv_bus_stop")

    if len(elements) > 10:
        elements[0].is_displayed()

    routes = ['1', '2', '3', '4', '5']
    bus_stop = ['Printemps / Galerie Lafayette', 'Musée du Louvre', 'Notre-Dame - Quartier Latin']

    assert are_elements_displayed(driver=driver, texts=routes)
    assert are_elements_displayed(driver, bus_stop)

    # Récupérer l'heure actuelle avec le fuseau horaire de Paris
    paris_timezone = pytz.timezone('Europe/Paris')
    current_hour = datetime.now(paris_timezone).time()

    # Vérifier si l'heure actuelle est entre 23h et 7h du matin
    if current_hour >= datetime.strptime('23:00', '%H:%M').time() or current_hour <= datetime.strptime('07:00', '%H:%M').time():
        assert is_element_displayed(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Inactive')]"))
        assert is_element_displayed(driver, (AppiumBy.ID, "com.ratpdev.esight.debug:id/tv_bus_state"))

    wait_and_click(driver, (AppiumBy.ID, 'com.ratpdev.esight.debug:id/image_maptype'))
    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Blue Route')]"))

    action = TouchAction(driver)
    action.tap(x=773, y=970, count=1).release().perform()

    time.sleep(2)

    try:
        card = driver.find_element(by=AppiumBy.ID, value="com.ratpdev.esight.debug:id/listCards")
        if card.is_displayed():
            assert False
    except NoSuchElementException:
        assert True

    assert get_rgb_by_coordinates(driver, AppiumBy.XPATH, "//*[contains(@text, 'Blue Route')]", 50) == (102, 102, 102)

    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Blue Route')]"))
    time.sleep(2)

    assert get_rgb_by_coordinates(driver, AppiumBy.XPATH, "//*[contains(@text, 'Blue Route')]", 50) == (0, 141, 45)








