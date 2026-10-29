import pytest
from thermostat_control import target_temperature, hvac_action, energy_alert

# Code (line) coverage tests: exercise the main scenario of each function so
# that at least 90% of the statements in thermostat_control.py are executed.


# ---------- target_temperature ----------

def test_away_mode():
    assert target_temperature("away", True, 12) == 16

def test_sleep_mode_daytime():
    assert target_temperature("sleep", True, 14) == 20

def test_home_unoccupied():
    assert target_temperature("home", False, 12) == 18

def test_home_morning():
    assert target_temperature("home", True, 7) == 22

def test_home_evening():
    assert target_temperature("home", True, 19) == 21

def test_home_midday():
    assert target_temperature("home", True, 12) == 20


# ---------- hvac_action ----------

def test_idle_when_close_to_target():
    assert hvac_action(21.5, 22, 15) == "idle"

def test_heat_boost_when_cold_outside():
    assert hvac_action(15, 22, 0) == "heat_boost"

def test_heat_when_mild_outside():
    assert hvac_action(18, 22, 12) == "heat"

def test_cool_when_warm_outside():
    assert hvac_action(26, 22, 25) == "cool"


# ---------- energy_alert ----------

def test_no_readings():
    assert energy_alert([], 10) == "ok"

def test_all_readings_under_limit():
    assert energy_alert([3, 5, 8], 10) == "ok"

def test_critical_when_most_over_limit():
    assert energy_alert([12, 15, 4], 10) == "critical"

def test_warning_when_few_over_limit():
    assert energy_alert([12, 4, 6], 10) == "warning"
