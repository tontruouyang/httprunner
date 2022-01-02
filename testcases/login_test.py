# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\login.yaml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLogin(HttpRunner):

    config = Config("login").base_url("http://192.168.0.141")

    teststeps = [
        Step(
            RunRequest("登录")
            .post("/index.php/login/submit")
            .with_json(
                {"username": 15011110000, "password": "abcd1234", "device_type": "5"}
            )
            .validate()
            .assert_equal("body.code", 1000)
            .assert_equal("status_code", 200)
        ),
    ]


if __name__ == "__main__":
    TestCaseLogin().test_start()
