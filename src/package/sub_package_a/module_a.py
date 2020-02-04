from ..sub_package_b.module_b import print_module_b


def print_module_a():
    return "module_a"


def print_module_a_b():
    return print_module_a() + print_module_b()
