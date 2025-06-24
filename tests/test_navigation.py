import pytest

EXPECTED_HEADERS = {
    "Admin": "User Management",
    "PIM": "PIM",
    "Leave": "Leave",
}


@pytest.mark.parametrize("panel,expected", EXPECTED_HEADERS.items())
def test_navigation_panels(dashboard, panel, expected):
    dashboard.click_panel(panel)
    assert dashboard.get_header() == expected
