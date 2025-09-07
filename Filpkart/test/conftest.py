from _pytest.fixtures import fixture
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

from Libraries.SeleniumUtilities import SeleniumUtilities
from POM.HomePage import HomePage
from POM.LaptopStore import LaptopStore
from POM.ZenLaptopPage import ZenLaptop
@fixture
def test_driver():
    opt=Options()
    opt.add_argument("--headless")
    driver=WebDriver(opt)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://www.flipkart.com/")
    yield driver
    driver.close()

@fixture
def obj_instance(test_driver):
    class Obj_creation:
        seleniumutilities = SeleniumUtilities(test_driver)
        homepage = HomePage(test_driver)
        laptopstore=LaptopStore()
        zenlaptop=ZenLaptop()

    return Obj_creation()


