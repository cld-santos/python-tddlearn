from unittest import TestCase
from package.sub_package_a import module_a
from package.sub_package_b import module_b


class PackageTest(TestCase):

    def test_must_run_func_imported(self):
        module_a.print_module_a_b()

    def test_must_not_throw_cyclic_import_error(self):
        """ To avoid cyclic import err you must import a module from a method.
        """
        module_b.print_module_b_a()
