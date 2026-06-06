import pytest
from data.data_login import LOGIN_CREDENTIALS
@pytest.mark.login
@pytest.mark.xfail(
    reason= "KL-001:Login validation blocked by Shopify CAPTCHA",
    strict=False
)
@pytest.mark.parametrize("data", LOGIN_CREDENTIALS, ids=[d["name"] for d in LOGIN_CREDENTIALS])
def test_login(data, login_page):
    login_page.open()
    login_page.login(data["username"], data["password"])

    if data["expected"] == "success":
        assert login_page.is_logged_in()

    else:
        if login_page.is_captcha_present():
            pytest.skip("Captcha bloquea validación de error message")

        error = login_page.get_error_message()
        assert data["error_message"] in error
