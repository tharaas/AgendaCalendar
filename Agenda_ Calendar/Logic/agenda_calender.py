from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from Infra.base_page import BasePage


class agendaCalender(BasePage):
    ADD_BUTTON = 'com.claudivan.taskagenda:id/btNovoEvento'
    TOMORROW_ADD_BUTTON = 'com.claudivan.taskagenda:id/containerColunasHorarios'
    CALENDER = '//android.widget.TextView[@text="Calendar"]'
    #DAY_ON_CALENDER = '//android.widget.TextView[@text="28"]'
    ADD_EVENT = '//android.widget.TextView[@text="Week"]'
    NEXT_WEEK = '(//android.widget.ImageView[@content-desc="Image"])[2]'

    def __init__(self, driver):
        super().__init__(driver)
        self.add_button = self.driver.find_element(by=AppiumBy.ID, value=self.ADD_BUTTON)
        self.tomorrow_add_button = self.driver.find_element(by=AppiumBy.ID, value=self.TOMORROW_ADD_BUTTON)
        self.calender = self.driver.find_element(by=AppiumBy.XPATH, value=self.CALENDER)
        #self.day_on_calender = self.driver.find_element(by=AppiumBy.XPATH, value=self.DAY_ON_CALENDER)
        self.add_event = self.driver.find_element(by=AppiumBy.XPATH, value=self.ADD_EVENT)
        self.next_week = self.driver.find_element(by=AppiumBy.XPATH, value=self.NEXT_WEEK)

    def click_on_add_button(self):
        self.add_button.click()
        return self.add_button

    def click_on_tomorrow_button(self):
        self.tomorrow_add_button.click()
        return self.tomorrow_add_button

    def click_on_tomorrow_add_button(self):
        self.test = self.click_on_add_button()
        self.test = self.click_on_tomorrow_button()
        return self.test

    def click_on_calender(self):
        self.calender.click()
        return self.calender

    #def click_on_day(self):
        #self.day_on_calender.click()
        #return self.day_on_calender

    #def click_on_day_on_calender(self):
        #self.new = self.click_on_calender()
        #return self.click_on_day()

    def click_on_add_event(self):
        self.add_event.click()
        return self.add_event

    def click_on_next_week(self):
        self.next_week.click()
        return self.next_week
