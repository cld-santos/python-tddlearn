
def print_module_b():
    return "module_b"

def print_module_b_a():
    from ..sub_package_a.module_a import print_module_a
    return print_module_a() + print_module_b()
