from care.basic_utils_care.basic_utils_care import CareUtilsBasic
from basic_utils.conf import settings

class UtlsCjm(CareUtilsBasic):


    def edit_cjm(user):
        user.logger.info("edit cjm")
        user.click_and_wait(user.LocatorType.ID,'settings-dropdown')
        user.click_and_wait(user.LocatorType.ID, 'edit-journey-model')
        user.click_and_wait(user.LocatorType.CLASS_NAME, 'button.apply-button')
        user.wait_for_element(user.LocatorType.XPATH, '//*[@id="vps"]/div[1]/div/div[1]/div[1]/div/div')
        return user.take_screenshot('edit2_cjm.png')
    def create_new_journey(user, journey_name, description):
        user.logger.info("create new journey")
        user.click_and_wait(user.LocatorType.XPATH, '//*[@id="vps"]/div[1]/div/div[1]/div[1]/div/div')
        user.wait_for_element(user.LocatorType.ID, 'name')
        user.add_name_and_description(journey_name, description)
        user.click_and_wait(user.LocatorType.ID, 'apply-button')
        user.take_screenshot('new_journey.png')

    def add_objective(user, objective_name, description):
        user.logger.info("add new objective")
        user.click_and_wait(user.LocatorType.XPATH,'//*[@id="vps"]/div[1]/span/div/div[2]/div[2]/div/section/div[2]/span')
        user.click_and_wait(user.LocatorType.ID, 'create')
        user.take_screenshot('new_objective.png')
        user.add_name_and_description(objective_name, description)
        user.click_and_wait(user.LocatorType.ID, 'apply-button')
        user.click_and_wait(user.LocatorType.ID, 'create','apply-button')
        user.take_screenshot('new_objective.png')

    def exit_edit_mode(user):
        user.logger.info("exit edit mode")
        user.click_and_wait(user.LocatorType.CLASS_NAME, 'button.grey.apply-button')
        user.take_screenshot('finish.png')












