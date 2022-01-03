import time

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)

def get_user():
    return [
        {"name":"15011110000"},
        {"name":"15011110001"},
        {"name":"15011110002"}

    ]

def register_user():
    user = "test" + str(int(time.time()))
    return user

def setup_hook():
    print("---------setup-----------")

def teardown_hook():
    print("---------teardown-----------")



if __name__ == "__main__":
    print(register_user())


