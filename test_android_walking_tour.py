from generic import first_stages_selector, wait_and_click, are_elements_displayed, is_element_displayed, get_rgb_by_coordinates
from selenium.common import NoSuchElementException


def test_android_walking_tour():
    # Android environment
    from appium import webdriver
    # Options are only available since client version 2.3.0
    from appium.options.android import UiAutomator2Options
    from appium.webdriver.common.appiumby import AppiumBy
    from appium.webdriver.common.touch_action import TouchAction
    import time
    import logging

    logging.basicConfig(level=logging.INFO)
    logging.basicConfig(filename='android.log', level=logging.INFO)

    options = UiAutomator2Options()
    options.platformVersion = '9'
    options.udid = 'emulator-5554'
    options.app = "/Users/2cconseil/Desktop/tootbus_latest.apk"

    driver = webdriver.Remote('http://192.168.1.59:4723', options=options)

    driver.implicitly_wait(12)

    first_stages_selector(driver)

    time.sleep(20)

    touch = TouchAction(driver)
    touch.press(x=494, y=1300).move_to(x=510, y=137).release().perform()
    time.sleep(1)

    #is_element_displayed(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Walking around in Paris')]"))

    elements = driver.find_elements(AppiumBy.ID, "com.ratpdev.esight.debug:id/imageWalkingTour")

    if len(elements) >= 1:
        elements[1].click()

    walking_tour_card_infos = ['The Parisian art of living ', 'Walking Tours', '4km', '45 min']

    assert are_elements_displayed(driver=driver, texts=walking_tour_card_infos)
    wait_and_click(driver, (AppiumBy.XPATH, f"//*[contains(@text, '{walking_tour_card_infos[0]}')]"))

    time.sleep(2)

    assert are_elements_displayed(driver=driver, texts=walking_tour_card_infos)

    driver.set_location(48.8511, 2.3444)
    time.sleep(2)

    wait_and_click(driver, (AppiumBy.ID, "com.ratpdev.esight.debug:id/icon_go"))

    assert is_element_displayed(driver, (AppiumBy.ID, "com.ratpdev.esight.debug:id/btnQuit"))
    assert is_element_displayed(driver, (AppiumBy.ID, "com.ratpdev.esight.debug:id/button_sound"))
    assert is_element_displayed(driver, (AppiumBy.ID, "com.ratpdev.esight.debug:id/button_pause"))

    walking_tour_card_infos = ['Boulevard Saint-Michel']

    assert are_elements_displayed(driver=driver, texts=walking_tour_card_infos)




