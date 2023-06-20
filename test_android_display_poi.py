from .generic import first_stages_selector, wait_and_click, are_elements_displayed, is_element_displayed
from selenium.common import NoSuchElementException


def test_android_display_poi():
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

    x, y = 519, 917
    x1, y2 = 519, 905
    action = TouchAction(driver)
    action.tap(x=x, y=y, count=2).release().perform()
    time.sleep(4)

    try:
        assert is_element_displayed(driver, (AppiumBy.ID, "com.ratpdev.esight.debug:id/listCards"))
    except NoSuchElementException:
        action = TouchAction(driver)
        action.tap(x=x1, y=y2, count=2).release().perform()
        time.sleep(4)
        assert is_element_displayed(driver, (AppiumBy.ID, "com.ratpdev.esight.debug:id/listCards"))

    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'See more')]"))

    wait_and_click(driver, (AppiumBy.ID, 'com.ratpdev.esight.debug:id/image_poi'))

    time.sleep(3)

    assert are_elements_displayed(driver, ['Palais Garnier', "Close"])

    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Close')]"))

    time.sleep(3)

    action = TouchAction(driver)
    action.tap(x=525, y=184, count=1).release().perform()

    time.sleep(3)

    action = TouchAction(driver)
    action.tap(x=822, y=709, count=1).release().perform()

    time.sleep(2)

    action = TouchAction(driver)
    map = driver.find_element(AppiumBy.ID, "com.ratpdev.esight.debug:id/map")

    time.sleep(4)

    x_ = 789
    y_ = 798

    action = TouchAction(driver)

    for _ in range(2):
        action.tap(x=x_, y=y_, count=4).release().perform()
        time.sleep(2)




