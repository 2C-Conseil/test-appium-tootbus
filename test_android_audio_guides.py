from selenium.common import NoSuchElementException
from .generic import first_stages_selector, wait_and_click, are_elements_displayed, is_element_displayed


def test_android_audio_guides():
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

    driver.set_location(48.8584, 2.3128)

    driver.implicitly_wait(12)

    first_stages_selector(driver)

    time.sleep(20)

    wait_and_click(driver, (AppiumBy.ID, 'com.ratpdev.esight.debug:id/imageAudioGuide'))

    wait_and_click(driver, (AppiumBy.ID, 'com.ratpdev.esight.debug:id/swOnBoard'))

    touch = TouchAction(driver)
    touch.press(x=492, y=1632).move_to(x=516, y=604).release().perform()

    assert is_element_displayed(driver, (AppiumBy.XPATH, "//*[contains(@text, '47. Hôpital des Invalides')]"))

    driver.set_location(48.8598, 2.2922)

    time.sleep(50)

    assert is_element_displayed(driver, (AppiumBy.XPATH, "//*[contains(@text, '38. The Eiffel Tower')]"))

    elements = driver.find_elements(AppiumBy.ID, "com.ratpdev.esight.debug:id/tvLabel")

    if len(elements) != 1:
        assert False

    elements = driver.find_elements(by=AppiumBy.ID, value="com.ratpdev.esight.debug:id/tvDescription")
    for el in elements:
        if "See more" in el.text:
            initial_text = el.text
            el.click()
            driver.implicitly_wait(5)

            updated_text = el.text
            if len(updated_text) <= len(initial_text):
                assert False
            break



