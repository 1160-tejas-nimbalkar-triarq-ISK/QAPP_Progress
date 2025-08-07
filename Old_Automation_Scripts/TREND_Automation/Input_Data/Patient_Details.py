# Input_Excel/Patient_Details_Faker.py
import random
import string
from datetime import datetime
from faker import Faker


class Patient_data:
    fake = Faker()
    first_name = fake.first_name()
    print(first_name)
    last_name = fake.last_name()
    middle_name = fake.first_name()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime('%m-%d-%Y')
    print("DOB", dob)
    gender = random.choice(["Male", "Female"])
    address = fake.address()
    address_parts = address.split(',')
    state_and_zip = address_parts[-1].strip()
    zip_code = state_and_zip[-5:]
    mobile_number = random.randint(1000000000, 9999999999)
    Home_Number = random.randint(1000000000, 9999999999)
    office_number = random.randint(1000000000, 9999999999)
    fax_number = random.randint(1000000000, 9999999999)
    email = f"{first_name.lower()}{random.randint(1000, 9999)}@mailinator.com"

    Value_Program = "TREND"
    # PGP = "Martin Nelson"
    Patient_Name = first_name + " " + last_name
    random_digits = ''.join(random.choices(string.digits, k=10))

    random_suffix = random.choice(['XYK', 'XYL'])
    insurance_id = random_suffix + random_digits
    random_digits = ''.join(random.choices(string.digits, k=10))
    random_suffix = random.choice(['GID', 'ABC'])
    Group_id = random_suffix + random_digits
    todays_date = datetime.today().strftime('%m-%d-%y')
    Patient_Note = first_name + " " + last_name + " Patient is created through Automation script on " + str(todays_date)
    Episode_Description = "Bundle Payment Episode created on " + todays_date + " through Python automation"
    target_price = random.randint(500, 2000)
    Episode_Note = "Bundle Payment Episode With Low risk"
    programs = ["Blue Cross Blue Shield", "Medicare"]
    random_program = random.choice(programs)
    facility = ["AVIDITY CARE", "ACTIVE PHYSICAL THERAPY PLC"]
    random_facility = random.choice(facility)

   

