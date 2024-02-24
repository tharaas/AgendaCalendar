import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from selenium.common import StaleElementReferenceException

from Logic.agenda_calender import agendaCalender

capabilities = dict(
    platformName="Android",
    deviceName="emulator-5554",
    platformVersion="11.0",
    automationName="UiAutomator2",
    appPackage="com.claudivan.taskagenda",
    appActivity=".Activities.MainActivity"
)

appium_server_url = 'http://localhost:4723'

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)


class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(
            command_executor=appium_server_url,
            options=capabilities_options
        )
        self.agendaCalender = agendaCalender(self.driver)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_add_button(self):
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                self.add_button = self.agendaCalender.click_on_add_button()
                assert self.add_button.is_displayed(), "Button is not displayed"
                break
            except StaleElementReferenceException:
                retries += 1
                print("StaleElementReferenceException occurred. Retrying...")

    def test_add_event(self):
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                self.event = self.agendaCalender.click_on_add_event()
                assert self.event.is_displayed(), "Button is not displayed"
                break
            except StaleElementReferenceException:
                retries += 1
                print("StaleElementReferenceException occurred. Retrying...")

    def test_go_to_calender(self):
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                self.calender = self.agendaCalender.click_on_calender()
                assert self.calender.is_displayed(), "Button is not displayed"
                break
            except StaleElementReferenceException:
                retries += 1
                print("StaleElementReferenceException occurred. Retrying...")

    def test_next_week(self):
        max_retries = 3
        retries = 0
        while retries < max_retries:
            try:
                self.next_week = self.agendaCalender.click_on_next_week()
                assert self.next_week.is_displayed(), "Button is not displayed"
                break
            except StaleElementReferenceException:
                retries += 1
                print("StaleElementReferenceException occurred. Retrying...")


if __name__ == '__main__':
    unittest.main()
