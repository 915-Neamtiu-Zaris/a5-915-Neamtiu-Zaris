"""
    Validators module
"""


class StoreException(Exception):
    pass


class StudentValidatorException(StoreException):
    pass


class StudentValidator:

    def validate(self, student):
        if not isinstance(student.group, int):
            raise StudentValidatorException("Group must be an integer.")

        if student.name.isdigit():
            raise StudentValidatorException("No numbers allowed in name.")

        if student.group <= 0:
            raise StudentValidatorException("Group must be positive.")
