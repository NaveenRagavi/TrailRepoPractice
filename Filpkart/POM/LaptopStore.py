
from Libraries.SeleniumUtilities import SeleniumUtilities

class LaptopStore:
    __zenlaptop=("xpath","(//a[text()='ZEBRONICS Pro Series Z Intel Core i5 12th Gen 1235U - (8 GB/512 G...'])[1]")
    def click_laptop(self,obj_instance):
        obj_instance.seleniumutilities.click_item(self.__zenlaptop)


