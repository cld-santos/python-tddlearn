from unittest import TestCase
from package.sub_package_a import module_a


class PackageTest(TestCase):

    def test_must_run_func_imported(self):
        module_a.print_module_a_b()

