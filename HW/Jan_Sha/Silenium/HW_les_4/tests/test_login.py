# import os
# import sys
#
# sys.path.append(os.getcwd())

import pytest
# from ..pages.main_page import MainPage
# from ..pages.sing_in_page import SignInPage
from HW_les_4.pages.main_page import MainPage
from HW_les_4.pages.sing_in_page import SignInPage
from HW_les_4.date.url import URL_LUMA
from conftest import *


#@pytest.mark.usefixtures('creds')
class TestSignIn:

    def test_sign_in_positive(self, driver):
        main_page = MainPage(driver, URL_LUMA)
        main_page.open()
        main_page.sign_in_link().click()
            #assert driver.current_url == 'https://magento.softwaretestingboard.com/customer/account/login'
        sign_in_page = SignInPage(driver, driver.current_url)
        sign_in_page.fill_in_the_form()
        assert main_page.welcome_is_present()