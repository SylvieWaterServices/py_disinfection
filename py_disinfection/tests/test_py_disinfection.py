import pytest
from py_disinfection.estimation import conservative_ct, interpolate_ct, regression_ct


@pytest.mark.parametrize(
    "temp, ph, chlorine_conc, expected",
    [
        (6.0, 6.7, 0.9, 149),
    ],
)
def test_conservative_ct(temp, ph, chlorine_conc, expected):
    assert conservative_ct(temp, ph, chlorine_conc) == expected


@pytest.mark.parametrize(
    "temp, ph, chlorine_conc, expected",
    [
        (6.0, 6.7, 0.9, 126.5),
    ],
)
def test_interpolate_ct(temp, ph, chlorine_conc, expected):
    assert pytest.approx(interpolate_ct(temp, ph, chlorine_conc), rel=1e-2) == expected


@pytest.mark.parametrize(
    "temp, ph, chlorine_conc, expected",
    [
        (6.0, 6.7, 0.9, 134),
    ],
)
def test_regression_ct(temp, ph, chlorine_conc, expected):
    assert pytest.approx(regression_ct(temp, ph, chlorine_conc), rel=1e-2) == expected
