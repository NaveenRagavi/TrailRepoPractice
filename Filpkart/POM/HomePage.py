
from Libraries.SeleniumUtilities import SeleniumUtilities
class HomePage:
    __electronics=("xpath","//img[@alt='Electronics']")
    __laptop_desktop=("xpath","//a[text()='Laptop and Desktop']")
    __laptop= ("xpath", "(//a[text()='Laptops'])[3]")


    def __init__(self, driver):
            self.driver = driver

    def catagories(self,obj_instance):
        obj_instance.seleniumutilities.move_element(self.__electronics)
        obj_instance.seleniumutilities.move_element(self.__laptop_desktop)
        obj_instance.seleniumutilities.move_element_click(self.__laptop)
