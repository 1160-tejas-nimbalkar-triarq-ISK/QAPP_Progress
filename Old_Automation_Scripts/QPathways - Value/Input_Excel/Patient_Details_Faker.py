# Input_Excel/Patient_Details_Faker.py
import random
import string
from datetime import datetime
from faker import Faker


class Patient_data:
    fake = Faker()
    first_name = fake.first_name()
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
    email = fake.email()
    PGP = "AWESOME THOUGHTS"
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


class Orders_Data:
    fake = Faker()
    Random_Number_HHA = random.randint(1000, 9999)
    Random_Number_PT = random.randint(1000, 9999)
    Random_Number_SNF = random.randint(1000, 9999)
    Range = random.randint(1, 4)
    Weeks = random.randint(1, 2)
    HHA_Order_Description = f"{Range}*{Weeks} Weeks EV order {Random_Number_HHA}"
    PT_Order_Description = f"{Range}*{Weeks} Weeks EV order {Random_Number_PT}"
    print(HHA_Order_Description)
    print(PT_Order_Description)
    Orders_Facility = "AMERICAN MEDICAL CENTER"
    Total_Ammount_Value = Range * Weeks * 10
    SNF_Order_Description = f"{Range} Days EV order{Random_Number_SNF}"


class Activities_Data:
    category_options = ["24-28 Hour follow up", "90 day follow up", "7-10 Day Follow up"]
    category = random.choice(category_options)
    Activity_Subject = f"Call Activity by TN {datetime.now().strftime('%H:%M:%S')}"
    Assigned_To_User = "Tejas Nimbalkar"
    Form = "History Tracking"
    Form_Subject = Form + "Patient Survey"


class Notes_Data:
    category_options = ["Discharge Note", "General", "Call Summary Note"]
    category = random.choice(category_options)
    fake = Faker()
    # Generate the note with the patient's name included
    Note = f"{Patient_data.Patient_Name}\n{fake.paragraph(nb_sentences=5)}"
    print(Note)


class Utilization_Data:
    Utilization_Facility = "AVIDITY CARE"
    Provider_name = "Tejas Nimbalkar"
