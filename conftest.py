import pytest
import sys
from selenium import webdriver


@pytest.yield_fixture(scope="session", autouse=True)
def driver(request):
    if sys.platform != "darwin":
        from pyvirtualdisplay import Display
        display = Display(visible=0, size=(1260, 800))
        display.start()
    chop = webdriver.ChromeOptions()
    #chop.add_extension("ublock_origin_1_13_2.crx")
    driver_instance = webdriver.Chrome(chrome_options=chop)
    driver_instance.implicitly_wait(20)
    try:
        yield driver_instance
    finally:
        if sys.platform != "darwin":
            display.stop()
        driver_instance.quit()