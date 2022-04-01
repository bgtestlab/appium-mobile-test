from typing import Any

from appium import webdriver

from page_objects.element import Element


class Page:
    """Base class to initialize pages"""

    def __init__(self, driver: webdriver) -> None:
        self._driver = driver

    def element(self, locator: Any) -> Element:
        return Element(self.driver, locator)
