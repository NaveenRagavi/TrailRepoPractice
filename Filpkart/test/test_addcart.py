from time import sleep


def test_addcart(obj_instance,test_driver):
    obj_instance.homepage.catagories(obj_instance)
    obj_instance.laptopstore.click_laptop(obj_instance)
    sleep(5)
    obj_instance.zenlaptop.add_to_cart(obj_instance)
    sleep(3)
    assert obj_instance.zenlaptop.place_order(obj_instance)==True
