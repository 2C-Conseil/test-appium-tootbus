from selenium.common import NoSuchElementException
from .generic import first_stages_selector, wait_and_click, are_elements_displayed, is_element_displayed


def test_android_display_bus():
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

    # Confirm city + location
    first_stages_selector(driver)

    # Action 8
    #assert is_element_displayed(driver, (AppiumBy.ID, "com.ratpdev.esight.preprod:id/header"))

    # Action 9
    #assert is_element_displayed(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Find your bus')]"))
    '''
    elements = driver.find_elements(AppiumBy.XPATH, "//*[@resource-id]")
    for index in range(len(elements)):
        elements = driver.find_elements(AppiumBy.XPATH, "//*[@resource-id]")
        resource_id = elements[index].get_attribute("resource-id")
        print(resource_id)
    '''

    # Action 10
    time.sleep(20)
    element = driver.find_element(AppiumBy.ID, "com.ratpdev.esight.debug:id/map_clicker")
    action = TouchAction(driver)
    action.tap(element).release().perform()

    wait_and_click(driver, (AppiumBy.ID, 'com.ratpdev.esight.debug:id/image_maptype'))

    assert is_element_displayed(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Blue Route')]"))
    assert is_element_displayed(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Paris By Night')]"))

    driver.implicitly_wait(12)
    elements = driver.find_elements(by=AppiumBy.ID, value="com.ratpdev.esight.debug:id/tv_bus_stop")

    if len(elements) > 10:
        elements[0].is_displayed()

    routes = ['1', '2', '3', '4', '5']
    bus_stop = ['Printemps / Galerie Lafayette', 'Printemps / Galerie Lafayette', 'Printemps / Galerie Lafayette']

    assert are_elements_displayed(driver=driver, texts=routes)
    assert are_elements_displayed(driver, bus_stop)

    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Paris By Night')]"))

    bus_stop = ['Musée du Louvre']

    assert are_elements_displayed(driver, bus_stop)

    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Blue Route')]"))

    wait_and_click(driver, (AppiumBy.ID, 'com.ratpdev.esight.debug:id/image_maptype'))

    x, y = 779, 917
    x1, y2 = 712, 930
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

    assert are_elements_displayed(driver, ['2', "Paris 75002", "mn"])

    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'See more')]"))

    assert is_element_displayed(driver, (AppiumBy.ID, "com.ratpdev.esight.debug:id/design_bottom_sheet"))

    bus_stop = ['mn', 'Line', 'Blue Route',
                'What to see around me ?', 'Palais Garnier']

    assert are_elements_displayed(driver=driver, texts=bus_stop)
    assert is_element_displayed(driver, (AppiumBy.ID, "com.ratpdev.esight.debug:id/tv_poi_name"))













