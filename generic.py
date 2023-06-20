from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException


def wait_and_click(driver, locator):
    driver.implicitly_wait(12)
    element = driver.find_element(*locator)
    element.click()


def is_element_displayed(driver, locator):
    driver.implicitly_wait(12)
    element = driver.find_element(*locator)
    return element.is_displayed()


def are_elements_displayed(driver, texts):
    import logging
    logging.basicConfig(level=logging.INFO)
    logging.basicConfig(filename='android.log', level=logging.INFO)

    for text in texts:
        elements = driver.find_elements(*text_locator(text))
        logging.info(text, elements)
        print(text, elements)
        if len(elements) == 0 or not elements[0].is_displayed():
            return False
    return True


def are_card_elements_displayed(driver, texts):
    import logging
    from appium.webdriver.common.appiumby import AppiumBy
    logging.basicConfig(level=logging.INFO)
    logging.basicConfig(filename='android.log', level=logging.INFO)

    recycler_view = driver.find_element(by=AppiumBy.ID, value="com.ratpdev.esight.preprod:id/listCards")

    for text in texts:
        # Recherchez le texte à l'intérieur de la vue RecyclerView
        elements = recycler_view.find_elements(by=AppiumBy.XPATH, value=f".//android.widget.TextView[contains(@text, '{text}')]")
        logging.info(text, elements)
        print(text, elements)
        if len(elements) == 0 or not elements[0].is_displayed():
            return False
    return True


def text_locator(text):
    from appium.webdriver.common.appiumby import AppiumBy
    return AppiumBy.XPATH, f"//*[contains(@text, '{text}') or @content-desc='{text}']"


def id_locator(id):
    from appium.webdriver.common.appiumby import AppiumBy
    return AppiumBy.ID, f"{id}"


def class_locator(class_name):
    from appium.webdriver.common.appiumby import AppiumBy
    return AppiumBy.CLASS_NAME, f"{class_name}"


def first_stages_selector(driver):
    # Action 1
    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Paris')]"))

    # Action 2
    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Confirm')]"))

    # Action 3
    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'No')]"))

    # Action 4
    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Skip')]"))

    # Action 4
    try:
        driver.find_element(AppiumBy.XPATH, "//*[contains(@text, 'Maybe later')]").click()
    except NoSuchElementException:
        assert True

    # Action 5
    wait_and_click(driver, (AppiumBy.XPATH, "//*[contains(@text, 'Next')]"))

    # Action 6
    wait_and_click(driver, (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button"))

    # Action 7
    wait_and_click(driver, (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button"))


def get_rgb_by_coordinates(driver, by, value, add_x=0, add_y=0):
    from PIL import Image, ImageDraw
    import io

    # Identifier l'élément à vérifier (utilisez les sélecteurs appropriés pour localiser l'élément)
    element = driver.find_element(by=by, value=value)

    # Prendre une capture d'écran de la page
    screenshot = driver.get_screenshot_as_png()
    screenshot_image = Image.open(io.BytesIO(screenshot))

    # Obtenir les coordonnées de l'élément
    element_location = element.location
    element_width = element.size['width']
    element_height = element.size['height']

    # Définir les coordonnées du pixel à vérifier
    check_color_x = element_location['x'] + add_x
    check_color_y = element_location['y'] + add_y

    # Obtenir la couleur du pixel
    pixel_color = screenshot_image.getpixel((check_color_x, check_color_y))
    red, green, blue = pixel_color[:3]

    # Afficher les valeurs RVB
    print("Red Color value =", red)
    print("Green Color value =", green)
    print("Blue Color value =", blue)

    # Dessiner un point à l'emplacement du pixel
    draw = ImageDraw.Draw(screenshot_image)
    point_radius = 5
    draw.ellipse((check_color_x - point_radius, check_color_y - point_radius,
                  check_color_x + point_radius, check_color_y + point_radius),
                 fill='red', outline='red')

    # Enregistrer l'image avec le point
    screenshot_image.save('screenshot_indicator.png')

    return red, green, blue