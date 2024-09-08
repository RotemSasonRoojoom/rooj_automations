from care.basic_utils_care.basic_utils_care import CareUtilsBasic
from care.infrastructure_bo.cjm.cjm_utils import UtlsCjm
from unittest import TestCase

class TestCjm(TestCase):
    utils = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.utils = CareUtilsBasic()
        cls.cjm=UtlsCjm()
        cls.utils.get_url()
        cls.utils.login()

    def test_create_journey(self):
        self.utils.nevigate_businessline()
        self.cjm.edit_cjm()
        self.cjm.create_new_journey('automations test journey','test journey')
        self.cjm.add_objective('test obj','test obj')
        self.cjm.exit_edit_mode()




