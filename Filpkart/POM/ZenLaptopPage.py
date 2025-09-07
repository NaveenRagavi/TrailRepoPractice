from time import sleep

from Libraries.SeleniumUtilities import SeleniumUtilities
from selenium.common import  exceptions as e
class ZenLaptop:
    currenturl="https://www.flipkart.com/zebronics-pro-series-z-intel-core-i5-12th-gen-1235u-8-gb-512-gb-ssd-windows-11-home-zeb-nbc-4s-thin-light-laptop/p/itmf4967e076a331?pid=COMGSZ8N2NFC8CGS&lid=LSTCOMGSZ8N2NFC8CGSARQDQB&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_4ee80d97-d305-426f-a687-ea122246b1ae_2_LCNPC4VE1P08_MC.COMGSZ8N2NFC8CGS&ppt=hp&ppn=homepage&ssid=8ybmg4pu9c0000001738152616312&otracker=clp_pmu_v2_Core%2Bi5%2BLaptops_4_2.productCard.PMU_V2_ZEBRONICS%2BPro%2BSeries%2BZ%2BIntel%2BCore%2Bi5%2B12th%2BGen%2B1235U%2B-%2B%25288%2BGB%252F512%2BGB%2BSSD%252FWindows%2B11%2BHome%2529%2BZEB-NBC%2B4S%2BThin%2Band%2BLight%2BLaptop_laptops-store_COMGSZ8N2NFC8CGS_neo%2Fmerchandising_3&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Core%2Bi5%2BLaptops_LIST_productCard_cc_4_NA_view-all&cid=COMGSZ8N2NFC8CGS"
    __add_to_cart=("xpath","//*[local-name()='svg']/parent::button[@class='QqFHMw vslbG+ In9uk2 JTo6b7']")
    __place_order=("xpath","//span[text()='Place Order']")
    def add_to_cart(self,obj_instance):
        obj_instance.seleniumutilities.window_handling(self.currenturl)
        obj_instance.seleniumutilities.click_item(self.__add_to_cart)


    def place_order(self,obj_instance):
        for _ in range(5):
            try:
                element = obj_instance.seleniumutilities.driver.find_element(*self.__place_order)
                if element.is_displayed():
                    return True

            except e.NoSuchElementException:
                sleep(2)
                continue
        return  False



