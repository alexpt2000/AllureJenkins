import nose


@nose.allure.step('make_some_data_foo')
def test_foo():
    nose.allure.environment(report='Allure report', browser=u'Firefox')
    assert (True == True)


def test_Othe():
    nose.allure.attach('my attach', 'Hello, World')
    with nose.allure.step('step two'):
        assert (True == True)

    with nose.allure.step('step two'):
        assert (False == False)
