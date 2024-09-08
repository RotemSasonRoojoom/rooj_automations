from care.basic_utils_care.basic_utils_care import CareUtilsBasic
from care.infrastructure_bo.simulator.simulator_utils import UtlsSimulator
from unittest import TestCase

class TestSimulator(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.utils = CareUtilsBasic()
        cls.simulator = UtlsSimulator()
        cls.utils.get_url()
        cls.utils.login()

    def test_enter_to_simulator(user):
        ##todo -find a smart way to pass the imgpath
        user.simulator.enter_to_journey_simulator()
        user.assertTrue(user.utils.compare_images(user.utils.click_on_view_button(),'/Users/rotemsason/PycharmProjects/rooj_automations/care/screenshot_path/2024-09-08/open_simulator.png'))

    def test_set_settings_for_simulator(user):
        user.simulator.set_env()
        user.simulator.set_env()
        user.simulator.set_channel()
        user.simulator.set_customer_id()
        user.assertTrue(user.utils.compare_images(user.simulator.set_customer_id(),'/Users/rotemsason/PycharmProjects/rooj_automations/care/screenshot_path/2024-09-08/open_simulator.png'))

    def test_play_simulator(user):
        user.assertTrue(user.utils.compare_images(user.simulator.play_button(),'/Users/rotemsason/PycharmProjects/rooj_automations/care/screenshot_path/2024-09-08/simulator.png'))

    def test_plat_in_light_box(user):
        user.assertTrue(user.utils.compare_images(user.simulator.play_in_light_box_button(),'/Users/rotemsason/PycharmProjects/rooj_automations/care/screenshot_path/2024-09-08/play_in_light_box.png'))

    def test_close_simulator(user):
        user.assertTrue(user.utils.compare_images(user.simulator.close_simulator(),'/Users/rotemsason/PycharmProjects/rooj_automations/care/screenshot_path/2024-09-08/close_simulator.png'))


