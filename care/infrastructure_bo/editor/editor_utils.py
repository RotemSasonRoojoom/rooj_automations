from care.basic_utils_care.basic_utils_care import CareUtilsBasic
from basic_utils.conf import settings

class UtlsEditor(CareUtilsBasic):
    def enter_to_main_journey(user):
        user.logger.info('enter_to_main_journey')
        user.nevigate_businessline()
        journey_name =user.main_journey_by_env[settings.test_env]
        user.take_screenshot('bla.png')
        user.click_and_wait_element_with_text(journey_name)
        user.wait_for_element(user.LocatorType.CLASS_NAME,'text')
        return user.take_screenshot('enter_to_main_journey.png')

    def create_new_build(user,build_name):
        user.logger.info('create_new_build')
        user.click_and_wait(user.LocatorType.ID,'build-dropdown-menu')
        user.click_and_wait(user.LocatorType.ID,'create-new-build-btn')
        user.fill_box(user.LocatorType.ID,'name',build_name)
        user.click_and_wait(user.LocatorType.CLASS_NAME,'component.button.apply-button')
