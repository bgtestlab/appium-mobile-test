import pytest
import copy

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from config import AppiumConfigs, AppConfigs
from helpers import take_screenshot_and_logcat
from page_objects.locators import Locator


class TestAndroidSelectors:
    @pytest.fixture(scope="function")
    def driver(self, request, device_logger):
        calling_request = request._pyfuncitem.name

        caps = copy.copy(AppConfigs.DESIRED_CAPABILITIES["device1"])
        caps["name"] = calling_request
        driver = webdriver.Remote(
            command_executor=AppiumConfigs.BASE_SERVER_URI, desired_capabilities=caps
        )
        yield driver
        take_screenshot_and_logcat(driver, device_logger, calling_request)
        driver.quit()

    def test_find_elements_by_accessibility_id(self, driver):
        search_parameters_element = driver.find_elements(
            AppiumBy.ACCESSIBILITY_ID, Locator.CONTENT
        )
        assert 1 == len(search_parameters_element)

    def test_find_elements_by_id(self, driver):
        action_bar_container_elements = driver.find_elements(
            AppiumBy.ID, Locator.ACTION_BAR_CONTAINER
        )
        assert 1 == len(action_bar_container_elements)

    def test_find_elements_by_class_name(self, driver):
        frame_layout_elements = driver.find_elements(
            AppiumBy.CLASS_NAME, Locator.FRAME_LAYOUT_CLASS
        )
        assert 3 == len(frame_layout_elements)

    def test_find_elements_by_xpath(self, driver):
        frame_layout_elements = driver.find_elements(
            AppiumBy.XPATH, Locator.FRAME_LAYOUT_XPATH
        )
        assert 3 == len(frame_layout_elements)
