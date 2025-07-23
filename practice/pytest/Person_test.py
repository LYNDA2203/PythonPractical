import pytest
from Person import  Employee,EmployeePersonJob,Manager,AssistantManager,SeniorManager

def test_employee():
    emp = Employee("Lynda" ,30000)
    assert emp.name == "Lynda".strip()
    assert emp.salary == 30000
    
def test_employee_person_job():
    emp = EmployeePersonJob("Geroge",50000)
    assert emp.name == "Geroge".strip()
    assert emp.salary == 50000
    
def test_manager():
    mgr = Manager("Anu",60000,"HR")
    assert mgr.name == "Anu".strip()
    assert mgr.salary == 60000
    assert mgr.department == "HR".strip()
    
def test_assistant_manager():
    asst_mgr = AssistantManager("Deju",45000,10)
    assert asst_mgr.name == "Deju".strip()
    assert asst_mgr.salary == 45000
    assert asst_mgr.team_size == 10
    
def test_senior_manager():
    sen_mgr = SeniorManager("David",700000,"Finance",20)
    assert sen_mgr.name == "David".strip()
    assert sen_mgr.salary == 700000
    assert sen_mgr.department == "Finance".strip()
    assert sen_mgr.team_size == 20
    