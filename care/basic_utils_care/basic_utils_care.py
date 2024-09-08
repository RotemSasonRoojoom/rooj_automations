from basic_utils.basic_utils import UtilsBasic
from basic_utils.conf import settings
import time

class CareUtilsBasic(UtilsBasic):
    main_journey_by_env = {'vf-qa':'Automations','bytel-qa':'Surf Journey QA','bytel-prod':'Surf Journey'}

    def login(user):
        user.logger.info("login to care")
        user.get_url()
        user.switch_to_iframe(user.LocatorType.XPATH,'/html/body/iframe')
        set_user = user.iframe.locator(user.LocatorType.ID('id_username'))
        set_user.fill(settings.login_info.username)
        set_pass = user.iframe.locator(user.LocatorType.ID('id_password'))
        set_pass.fill(settings.login_info.password)
        user.iframe.locator(user.LocatorType.CLASS_NAME('button')).click()
        tic = time.perf_counter()
        user.go_to_default_iframe()
        user.wait_for_element(user.LocatorType.XPATH,'//*[@id="app"]/div[1]/header/div[3]/div[1]/button/img')
        user.take_screenshot('login.png')
        toc = time.perf_counter()
        login_time = toc - tic
        return login_time

    def nevigate_businessline(user):
        user.logger.info("nevigate businessline")
        user.click_and_wait(user.LocatorType.ID, 'business-line-dropdown')
        if user.get_text_of_element(user.LocatorType.ID, 'business-line-dropdown') == settings.business_line:
            return
        user.click_and_wait_element_with_text(settings.business_line)
        user.take_screenshot('businessline.png')

    def click_on_view_button(user):
        user.logger.info("click view button")
        user.click_and_wait(user.LocatorType.ID, 'journey-view-btn')
        user.wait_for_element(user.LocatorType.ID, 'play-journey-btn')
        return user.take_screenshot('open_simulator.png')

    def add_name_and_description(user, name, description):
        user.fill_box(user.LocatorType.ID, 'name', name)
        user.fill_box(user.LocatorType.ID, 'description', description)


