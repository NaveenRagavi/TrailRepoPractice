from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located

def wait(func):
    def wrapper(*args,**kwargs):
        obj=args[0]
        locator=args[1]
        webwait=WebDriverWait(obj.driver,10)
        webwait.until(visibility_of_element_located(locator))
        return func(*args,**kwargs)
    return wrapper

class SeleniumUtilities:
    def __init__(self,driver):
        self.driver=driver
    @wait
    def click_item(self,locator):
        self.driver.find_element(*locator).click()
    @wait
    def send_items(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def move_element_click(self,locator):
        element=self.driver.find_element(*locator)
        action=ActionChains(self.driver)
        action.move_to_element(element).click().perform()

    @wait
    def move_element(self,locator):
        element = self.driver.find_element(*locator)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()

    @wait
    def window_handling(self,url):
        windows=self.driver.window_handles
        for window in windows:
            self.driver.switch_to.window(window)
            url_current=self.driver.current_url
            if url_current.__eq__(url):
                return
            else:
                continue

