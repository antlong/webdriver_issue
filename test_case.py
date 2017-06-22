from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def verify_length(driver, el):
    wait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "lede__image"))
    )
    return True if len(el.text) > 100 else False


def verify_no_error_div(driver, url):
    try:
        driver.find_element_by_xpath(
            "//*[contains(text(), 'not-found__title')]"
        )
    except NoSuchElementException:
        return True
    else:
        raise Exception("not-found__title found at %s" % url)


def check_root(driver, url, bypass=False):
    if not bypass:
        driver.get(url)
    el = driver.find_element_by_id("root")

    # root is over 100 chars
    assert verify_length(driver, el)

    # error message div isn't present on the page
    assert verify_no_error_div(driver, url)


def test_broadly_en(driver):
    check_root(driver, "https://broadly.vice.com/en_us")