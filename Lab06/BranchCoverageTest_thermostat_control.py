import pytest
from thermostat_control import target_temperature, hvac_action, energy_alert

# Branch coverage tests: every if / for decision in thermostat_control.py is
# driven both True and False, plus the boundary values of each condition.


# ---------- target_temperature ----------

def test_away_mode():
    assert target_temperature("away", True, 12) == 16

def test_away_mode_ignores_occupancy_and_hour():
    assert target_temperature("away", False, 3) == 16

def test_sleep_mode_early_morning():
    # hour < 6 -> True
    assert target_temperature("sleep", True, 2) == 18

def test_sleep_mode_late_night():
    # hour < 6 -> False, hour >= 22 -> True
    assert target_temperature("sleep", True, 23) == 18

def test_sleep_mode_daytime():
    # both sides of the "or" False
    assert target_temperature("sleep", True, 14) == 20

@pytest.mark.parametrize("hour, expected", [
    (5, 18),   # last hour before 6
    (6, 20),   # 6 is not < 6
    (21, 20),  # last hour before 22
    (22, 18),  # 22 is >= 22
])
def test_sleep_mode_boundaries(hour, expected):
    assert target_temperature("sleep", True, hour) == expected

def test_sleep_mode_ignores_occupancy():
    assert target_temperature("sleep", False, 14) == 20

def test_home_unoccupied():
    assert target_temperature("home", False, 12) == 18

def test_home_unoccupied_overrides_schedule():
    assert target_temperature("home", False, 7) == 18

def test_home_morning():
    assert target_temperature("home", True, 7) == 22

def test_home_evening():
    assert target_temperature("home", True, 19) == 21

def test_home_midday():
    assert target_temperature("home", True, 12) == 20

def test_home_night():
    assert target_temperature("home", True, 2) == 20

@pytest.mark.parametrize("hour, expected", [
    (5, 20),   # before morning window
    (6, 22),   # morning window starts
    (8, 22),   # last morning hour
    (9, 20),   # morning window ends
    (16, 20),  # before evening window
    (17, 21),  # evening window starts
    (21, 21),  # last evening hour
    (22, 20),  # evening window ends
])
def test_home_schedule_boundaries(hour, expected):
    assert target_temperature("home", True, hour) == expected


# ---------- hvac_action ----------

def test_idle_when_close_to_target():
    assert hvac_action(21.5, 22, 15) == "idle"

def test_idle_when_slightly_above_target():
    assert hvac_action(22.5, 22, 15) == "idle"

def test_idle_when_exactly_on_target():
    assert hvac_action(22, 22, 15) == "idle"

def test_heat_boost_when_cold_outside():
    assert hvac_action(15, 22, 0) == "heat_boost"

def test_heat_when_mild_outside():
    assert hvac_action(18, 22, 12) == "heat"

def test_heat_at_outside_boundary():
    # outside == 5 is not < 5
    assert hvac_action(18, 22, 5) == "heat"

def test_heat_boost_just_below_outside_boundary():
    assert hvac_action(18, 22, 4.9) == "heat_boost"

def test_heat_when_diff_exactly_one():
    # abs(diff) == 1 is not < 1, so the system acts
    assert hvac_action(21, 22, 12) == "heat"

def test_cool_boost_when_hot_outside():
    assert hvac_action(28, 22, 35) == "cool_boost"

def test_cool_when_warm_outside():
    assert hvac_action(26, 22, 25) == "cool"

def test_cool_at_outside_boundary():
    # outside == 30 is not > 30
    assert hvac_action(26, 22, 30) == "cool"

def test_cool_boost_just_above_outside_boundary():
    assert hvac_action(26, 22, 30.1) == "cool_boost"

def test_cool_when_diff_exactly_minus_one():
    assert hvac_action(23, 22, 25) == "cool"


# ---------- energy_alert ----------

def test_no_readings():
    # for loop body never runs
    assert energy_alert([], 10) == "ok"

def test_all_readings_under_limit():
    assert energy_alert([3, 5, 8], 10) == "ok"

def test_reading_equal_to_limit_is_not_over():
    assert energy_alert([10, 10, 10], 10) == "ok"

def test_critical_when_most_over_limit():
    assert energy_alert([12, 15, 4], 10) == "critical"

def test_critical_when_all_over_limit():
    assert energy_alert([11, 12, 13], 10) == "critical"

def test_critical_single_reading_over():
    assert energy_alert([20], 10) == "critical"

def test_warning_when_few_over_limit():
    assert energy_alert([12, 4, 6], 10) == "warning"

def test_warning_when_exactly_half_over():
    # over * 2 == len(readings) is not > len, so only a warning
    assert energy_alert([12, 15, 4, 6], 10) == "warning"
