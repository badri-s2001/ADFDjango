"""
Program which connects python and MySQL Database
"""
import logging
from datetime import datetime
import re

logging.basicConfig(filename="log.txt",
                    filemode='w',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=1,
                    )


class User:
    """
    Used to add users to the database, validates and checks the eligibility
    """
    reason = ''

    def __init__(self, firstname, middlename, lastname, dateofbirth, gender, nationality, city, state, pincode,
                 qualification, salary, pannumber):
        self.first_name = firstname
        self.middle_name = middlename
        self.last_name = lastname
        self.date_of_birth = dateofbirth
        self.age = None
        self.gender = gender
        self.nationality = nationality
        self.city = city
        self.state = state
        self.pincode = pincode
        self.qualification = qualification
        self.salary = salary
        self.pan_number = pannumber
        self.success_or_failure = None

    def validate(self, name, item):
        """
        Performs validation for several types of items
        :param name: The type of item which you want to validate (ex: f_name, date_of_birth)
        :param item: The item which you want to validate
        :return: True if the item is valid , else returns False
        """

        f_name_pattern = r'^[a-zA-Z ]+$'
        l_name_pattern = r'^[a-zA-Z ]+$'
        gender_pattern = r'^(?:m|M|male|Male|f|F|female|Female)$'
        nationality_pattern = r'^(?:Indian|American)$'
        city_pattern = r'^[a-zA-Z ]+$'
        state_pattern = r'^(?:Andhra Pradesh|Arunachal Pradesh|Assam|Bihar|Chhattisgarh|Karnataka|Tamil Nadu|Telangana|West Bengal)$'
        qualification_pattern = r'^[a-zA-Z\. ]+$'
        pan_pattern = r'^[a-zA-Z0-9]{10}$'
        pin_code_pattern = r'^[0-9]{6}$'

        status = True

        if name == "f_name":
            logging.info("Validating first name")
            pat = re.compile(f_name_pattern)
            if re.fullmatch(pat, item):
                self.first_name = item
            else:
                self.reason += "First name is not valid. "
                status = False

        if name == "l_name":
            logging.info("Validating last name")
            pat = re.compile(l_name_pattern)
            if re.fullmatch(pat, item):
                self.last_name = item
            else:
                self.reason += "Last name is not valid. "
                status = False

        if name == "gender":
            logging.info("Validating gender")
            pat = re.compile(gender_pattern)
            if re.fullmatch(pat, item):
                self.gender = item
            else:
                self.reason += "Gender is not valid. "
                status = False

        if name == "nationality":
            logging.info("Validating nationality")
            pat = re.compile(nationality_pattern)
            if re.fullmatch(pat, item):
                self.nationality = item
            else:
                self.reason += "Nationality is not valid. "
                status = False

        if name == "city":
            logging.info("Validating city")
            pat = re.compile(city_pattern)
            if re.fullmatch(pat, item):
                self.city = item
            else:
                self.reason += "City is not valid. "
                status = False

        if name == "state":
            logging.info("Validating state")
            pat = re.compile(state_pattern)
            if re.fullmatch(pat, item):
                self.state = item
            else:
                self.reason += "State is not valid. "
                status = False

        if name == "qualification":
            logging.info("Validating qualification")
            pat = re.compile(qualification_pattern)
            if re.fullmatch(pat, item):
                self.qualification = item
            else:
                self.reason += "Qualification is not valid. "
                status = False

        if name == "pan_number":
            logging.info("Validating pan number")
            pat = re.compile(pan_pattern)
            if re.fullmatch(pat, item):
                self.pan_number = item
            else:
                self.reason += "Pan number is not valid. "
                status = False

        if name == "pin_code":
            logging.info("Validating pin code.")
            self.pincode = 0
            pat = re.compile(pin_code_pattern)
            if re.fullmatch(pat, item):
                self.pincode = int(item)
            else:
                self.reason += "Pin code is not valid. "
                status = False

        if name == "date_of_birth":
            logging.info("Validating date of birth")

            try:
                self.date_of_birth = datetime.strptime(item, "%Y-%m-%d")
            except ValueError:
                self.date_of_birth = datetime(1800, 1, 1)
                self.reason += "Invalid Input for DOB. "

            return status

        if name == "salary":
            logging.info("Validating salary")
            self.salary = 0
            if item == "":
                self.reason += "Salary is empty. "
                status = False
            elif int(item) < 10000:
                self.reason += "Salary is less than expected. "
                status = False
            elif int(item) > 90000:
                self.reason += "Salary is more than expected. "
                status = False
            else:
                self.salary = int(item)

            return status

        return status

    def calculate_age(self, birthdate):
        """
        Calculates the current age
        :param birthdate: The birthdate using which age will be calculated
        :return: The age after calculating it
        """
        logging.info("Validating age")
        today = datetime.today()
        self.age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return self.age

    def check_age_gender(self, age, gender):
        """
        Checks the age gender criteria
        :param age: The age of the user
        :param gender: The gender of the user
        :return: True if criteria is succeeded, else False
        """
        logging.info("Validating age gender criteria")
        status = True
        if age is not None and gender != "-":
            if age < 21 and (gender == "Male" or gender == "M" or gender == "m" or gender == "male"):
                self.reason += "Age should be 21 or above for male. "
                status = False
            if age < 18 and (gender == "Female" or gender == "F" or gender == "f" or gender == "female"):
                self.reason += "Age should be 18 or above for female. "
                status = False

        return status

    def check_success_or_failure(self):
        """
        Checks if the request is successful or failed
        :return: True if request is successful, else False
        """
        logging.info("Checking whether success or failure")
        status = True
        if self.reason == "":
            self.success_or_failure = "Success"
            self.reason = "-"
        else:
            self.success_or_failure = "Failure"
            status = False

        return status

    def validate_details(self):
        """
        Gets details of the user in the console
        :return: True after receiving all the input
        """
        logging.info("Getting details from user")
        self.validate("f_name", self.first_name)
        self.validate("l_name", self.last_name)
        self.validate("date_of_birth", self.date_of_birth)
        self.validate("gender", self.gender)
        self.validate("nationality", self.nationality)
        self.validate("city", self.city)
        self.validate("state", self.state)
        self.validate("pin_code", self.pincode)
        self.validate("qualification", self.qualification)
        self.validate("salary", self.salary)
        self.validate("pan_number", self.pan_number)
        self.calculate_age(self.date_of_birth)
        self.check_age_gender(self.age, self.gender)
        self.check_success_or_failure()

        return True
