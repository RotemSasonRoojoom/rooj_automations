from datetime import time

from care.basic_utils_care.basic_utils_care import CareUtilsBasic
from basic_utils.conf import settings
class UtlsSimulator(CareUtilsBasic):

    def enter_to_journey_simulator(user):
        ##todo - think about different generic way
        user.page.goto(settings.simulator_path)

    def set_env(user):
        user.logger.info('set environment')
        user.click_and_wait(user.LocatorType.ID,'envs-dropdown')
        user.click_and_wait(user.LocatorType.ID,settings.env)

    def set_channel(user):
        user.logger.info('set channel')
        user.click_and_wait(user.LocatorType.ID,'channels-dropdown')
        user.click_and_wait(user.LocatorType.ID,settings.channel)

    def set_customer_id(user):
        user.logger.info('set customer id')
        user.fill_box(user.LocatorType.ID,'customerId',settings.cid)
        return user.take_screenshot('settings.png')

    def play_in_light_box_button(user):
        user.logger.info("click play in light box button")
        user.click_and_wait(user.LocatorType.ID, 'play-journey-in-light-box-btn')
        user.switch_to_iframe(user.LocatorType.NAME, 'rj_popup_viewer')
        user.run_journey_in_simulator()
        return user.take_screenshot('play_in_light_box.png')
    def run_journey_in_simulator(user):
        user.logger.info("runing journey in simulator")
        set_user = user.iframe.locator(user.LocatorType.CLASS_NAME('button.primary-button'))
        set_user.click()
        set_user = user.iframe.locator(user.LocatorType.CLASS_NAME('button.secondary-button'))
        set_user.click()

    def play_button(user):
        user.logger.info("click play button")
        user.click_and_wait(user.LocatorType.ID, 'play-journey-btn')
        user.switch_to_iframe(user.LocatorType.ID, 'simulator-frame')
        user.run_journey_in_simulator()
        user.take_screenshot("simulator.png")

    def close_simulator(user):
        user.click_and_wait(user.LocatorType.ID, 'rj_close_frame')
        return user.take_screenshot('close_simulator.png')






