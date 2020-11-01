"""
Testing the first functionality (add).
"""

from domain.validators import StudentValidator, StudentValidatorException
from services.service import StudentService


def test_add_student():
    validator = StudentValidator()
    service = StudentService(validator)

    assert len(service.get_all_students()) == 0

    service.add_student("Zaris Neamtiu", 915)
    service.add_student("Pop", 920)

    list_students = service.get_all_students()

    assert list_students[0].name == "Zaris Neamtiu"
    assert list_students[0].group == 915

    assert list_students[1].name == "Pop"
    assert list_students[1].group == 920

    try:
        service.add_student("Zaris", -120)
        service.add_student("Zaris", "123")
        service.add_student(23, 120)
        service.add_student("Zaris4", 235)
        service.add_student("2Zaris4", 23124)
        assert False
    except StudentValidatorException:
        assert True
