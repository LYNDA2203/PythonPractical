import pytest
import re
from car import Hatchback, Suv

@pytest.mark.parametrize("car_class,brand,model,year,expected_sunroof", [
    (Hatchback, "Maruti","Alto","2022", "Sunroof: Not available "),
    (Suv, "boxy city","mahindra","2024", "Sunroof: Available")
])
def test_car_methods(car_class, brand, model, year, expected_sunroof, capsys):
    car = car_class(brand, model, year)

    car.printDetails()
    captured = capsys.readouterr()
    normalized_output = re.sub(r'\s+', ' ', captured.out)
    assert f"Brand: {brand}" in normalized_output
    assert f"Model: {model}" in normalized_output 
    assert f"Year: {year}" in normalized_output

    car.accelerate()
    captured = capsys.readouterr()
    assert "Speed up....." in captured.out

    car.sunroof()
    captured = capsys.readouterr()
    assert expected_sunroof in captured.out  

    car.break_applied()
    captured = capsys.readouterr()
    assert "Car stopped" in captured.out
