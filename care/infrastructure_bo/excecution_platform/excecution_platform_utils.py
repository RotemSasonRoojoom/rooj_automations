from care.basic_utils_care.basic_utils_care import CareUtilsBasic
from basic_utils.conf import settings


class UtilsExcecutionPlatform(CareUtilsBasic):
    def enter_open_interface(user):
        user.logger.info('Entering to open interface')
        user.click_and_wait(user.LocatorType.ID,'settings-dropdown')
        user.click_and_wait(user.LocatorType.ID,'open-interface')
        user.wait_for_element(user.LocatorType.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/header/div/input')
        return user.take_screenshot('ep1.png')

    def search_action(user):
        user.logger.info('search action in search box')
        user.fill_box(user.LocatorType.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/header/div/input','GetAvailabilityMock')
        user.click_enter()
        return user.take_screenshot('search.png')

    def run_action_from_excecution_platform(user):
        user.logger.info('runing action from excecution platform')
        user.click_and_wait(user.LocatorType.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div[1]/section/table/tbody/tr/td[8]/div/div[2]/div')
        user.select_value_in_dropdown_list(user.LocatorType.ID,'env','Test')
        user.fill_box(user.LocatorType.ID ,'name', settings.cid)
        user.click_and_wait(user.LocatorType.CLASS_NAME,'execute')
        user.wait_for_element(user.LocatorType.XPATH,'//*[@id="modals-container"]/div/div/div[2]/div/form/div[3]')
        user.take_screenshot('newaction.png')

    def search_by_session_id(user):
        user.logger.info('runing action from excecution platform')
        user.fill_box(user.LocatorType.XPATH,'//*[@id="app"]/div[1]/div[2]/header/div/input[2]','b39adf81-2bfb-4322-8807-e343c7e57bb1')
        user.click_enter()
        user.take_screenshot('search.png')

    def enter_to_exection_logs(user):
        user.logger.info('entering to exection logs')
        user.click_and_wait(user.LocatorType.CLASS_NAME,'dropdown-menu')
        user.click_and_wait(user.LocatorType.XPATH,'//*[@id="app"]/div[1]/div[1]/div/div[3]/div/div/div[2]/div[3]')
        user.take_screenshot('execlogs.png')

    def search_by_context_key(user):
        user.logger.info('searching by context key')
        user.fill_box(user.LocatorType.PLACEHOLDER,'Search context key','715fd883-bb16-4332-bba0-35491913c650')
        user.click_enter()










