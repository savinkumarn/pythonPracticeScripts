
def dec_func_for_test(input_func):
    def wrap_func():
        print("Before Wrap")
        input_func()
        print("After Wrap")
    return wrap_func


@dec_func_for_test
def test_func_for_dec():
    print("Inside test func")


def main_dec():
    # Case 1: Basic Testing
    test_func_for_dec()
