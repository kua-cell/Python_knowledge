import time


def test_time(func):
    """In order to test the time of running function"""

    def func_time(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        running_time = start_time - end_time
        print(running_time)
        return result
    return func_time()


@test_time
def example_function():
    time.sleep(3)
