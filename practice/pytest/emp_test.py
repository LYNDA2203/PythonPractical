import pytest
from Employee import Employee

@pytest.mark.parametrize("initial_salary, new_salary, expected_salary, expected_output", [
    (30000, 45000, 45000, f"Salary update to : ₹45000"),
    (50000, -1000, 50000, "Error: Salary must be positive!!!"),
    (20000, 0, 20000, "Error: Salary must be positive!!!"),
])

def test_salary_update(initial_salary,new_salary,expected_salary,expected_output,capsys):
    emp = Employee("Lynda",initial_salary)
    emp.salary = new_salary
    captured = capsys.readouterr()#returns the statement in print().. and in console and throws error
    
    assert emp.salary == expected_salary
    assert expected_output in captured.out