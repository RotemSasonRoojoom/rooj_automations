import time
from playwright.sync_api import sync_playwright
from datetime import datetime
from basic_utils.conf import settings
from PIL import Image
import imagehash
import os
import logging
import sys
from playwright.sync_api import sync_playwright

CURRENT_DATE = datetime.now().strftime('%Y-%m-%d')
CURRENT_TIME = datetime.now().strftime('%H:%M:%S')
def get_driver(wait_seconds=3000):
    proxy_config = option_dependency_env()
    p = sync_playwright().start()
    browser = p.chromium.launch(
        headless=False,
        proxy=proxy_config['proxy']
    )

    page = browser.new_page()
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.set_default_timeout(wait_seconds)

    return page


def set_up_logger():
    logger = logging.getLogger('tester')
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    file_handler = logging.FileHandler(f'{settings.logs_path}/logs_{CURRENT_DATE}.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger


def option_dependency_env():

    proxy_server = f"http://{settings.login_info.server}:{settings.login_info.port}"
    option = {
        'proxy': {
            'server': proxy_server,
            'username': settings.login_info.username_proxy,
            'password': settings.login_info.password_proxy,
        }
    }
    return option
def get_date_directory():
    current_date = datetime.now().strftime('%Y-%m-%d')
    date_dir = os.path.join(settings.screenshots_path, CURRENT_DATE)
    if not os.path.exists(date_dir):
        os.makedirs(date_dir)
    return date_dir


class UtilsBasic:

    class LocatorType:
        ID = lambda id_value: f"#{id_value}"
        CLASS_NAME = lambda class_value: f".{class_value}"
        XPATH = lambda xpath_value: f"xpath={xpath_value}"
        LINK_TEXT = lambda text_value: f"text={text_value}"
        NAME = lambda name_value: f"[name='{name_value}']"
        PLACEHOLDER = lambda placeholder_value: f"placeholder={placeholder_value}"


    logger = set_up_logger()
    page =get_driver(wait_seconds=5000)
    iframe=None
    iframe_flag=False

    def __init__(user):
        user.page = UtilsBasic.page
        user.logger = UtilsBasic.logger

    def get_url(user, url=settings.login_info.url):
        user.logger.info("get url")
        user.page.goto(url)
        user.page.wait_for_selector('body')

    def quit_driver(user):
        user.logger.info("quit driver")
        user.page.context.browser.close()

    def close_window(user):
        user.logger.info("close window")
        user.page.close()

    def go_to_default_iframe(user):
        user.page
        user.iframe_flag=False
    def switch_to_iframe(user, locator_type, locator_value):
        user.iframe = user.page.frame_locator(locator_type(locator_value))
        user.iframe_flag = True


    def click_and_wait(user, locator_type,locator_value,wait_seconds=25000):
        locator = user.page.locator(locator_type(locator_value))
        locator.wait_for(timeout=wait_seconds * 1000)
        locator.click()

    def wait_for_element(user, locator_type, locator_value, timeout=30000):
        locator = user.page.locator(locator_type(locator_value))
        locator.wait_for(timeout=timeout)

    def set_value(user, locator_type, locator_value, value):
        selector = locator_type(locator_value)
        user.page.wait_for_selector(selector)
        user.page.locator(selector).fill(value)

    def click_clear_box(user, locator_type, locator_value):
        selector = locator_type(locator_value)
        user.page.wait_for_selector(selector)
        user.page.locator(selector).click()
        user.page.locator(selector).fill('')

    def hover_and_click_element(user, locator_type, locator_value):
        selector = locator_type(locator_value)
        user.page.wait_for_selector(selector)
        user.page.locator(selector).hover()
        user.page.locator(selector).click()

    def hover_element(user, locator_type, locator_value):
        selector = locator_type(locator_value)
        user.page.wait_for_selector(selector)
        user.page.locator(selector).hover()

    def hover(user, locator_type, locator_value):
        selector = locator_type(locator_value)
        user.page.wait_for_selector(selector)
        user.page.locator(selector).hover()

    def select_value_in_dropdown_list(user, locator_type, locator_value, select_value):
        selector = locator_type(locator_value)
        user.page.wait_for_selector(selector)
        dropdown = user.page.locator(selector)
        dropdown.select_option(label=select_value)

    def fill_box(user, locator_type, locator_value, value):
        user.page.wait_for_selector(locator_type(locator_value))
        user.page.locator(locator_type(locator_value)).is_visible()
        user.set_value(locator_type, locator_value, value)

    def click_and_wait_element_with_text(user, text):
      user.page.get_by_text(text).click()

    def get_parent(user, xpath):
        user.page.wait_for_selector('body')
        element = user.page.locator(xpath)
        return element.locator('..')

    def get_text_of_element(user, locator_type, locator_value):
        selector = locator_type(locator_value)
        user.page.wait_for_selector(selector)
        return user.page.locator(selector).inner_text()

    def get_list_of_elements(user, locator_type, locator_value):
        selector = locator_type(locator_value)
        elements = user.page.locator(selector).element_handles()
        return elements

    def scroll_into_view(user, locator_type, locator_value):
        selector = locator_type(locator_value)
        element = user.page.locator(selector)
        element.scroll_into_view_if_needed()
        user.page.locator(selector).wait_for()

    def scroll_text_into_view(user, text):
        selector = f"//*[contains(text(),'{text}')]"
        user.page.locator(selector).scroll_into_view_if_needed()

    def click_enter(user):
        user.page.keyboard.press('Enter');

    def count_elements(user, locator_type, locator_value):
        selector = locator_type(locator_value)
        elements = user.page.locator(selector).element_handles()
        return len(elements), elements

    def click_coordinate(user, wait_seconds=1):
        user.logger.info("click coordinate")
        time.sleep(wait_seconds)
        user.page.mouse.click(10, 10)

    def open_new_tab(user, url, locator_type, locator_value):
        user.logger.info('open new tab')
        context = user.page.context
        new_page = context.new_page()
        new_page.goto(url)
        selector = locator_type(locator_value)
        new_page.locator(selector).wait_for()

    def go_to_default_tab(user):
        user.logger.info('close new tab and return to default tab')
        user.page.close()
        user.page.context.pages[0].bring_to_front()

    def go_to_new_tab(user):
        user.logger.info('go to new tab')
        user.page.context.pages[-1].bring_to_front()

    def scroll_page_vertically(user):
        user.logger.info('scroll page vertically')
        user.page.evaluate("window.scrollTo(0, document.body.scrollHeight);")

    def take_screenshot(user,screenshot_filename):
        date_dir = get_date_directory()
        screenshot_path = os.path.join(date_dir, screenshot_filename)
        user.page.screenshot(path=screenshot_path,full_page=True)
        return screenshot_path

    def compare_images(user,image1_path,image2_path):
        image1 = Image.open(image1_path)
        image2 = Image.open(image2_path)
        hash1 = imagehash.average_hash(image1)
        hash2 = imagehash.average_hash(image2)
        return hash1 == hash2


























































