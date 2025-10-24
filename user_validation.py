import re
from datetime import datetime

class UserValidation:
    @staticmethod
    def validate_email(email: str) -> bool:
        if not email or not isinstance(email, str):
            return False
        email = email.strip()
        pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        return bool(re.fullmatch(pattern, email))

    @staticmethod
    def validate_username(username: str) -> bool:
        if not username or not isinstance(username, str):
            return False
        username = username.strip()
        pattern = r"^[A-Za-z0-9_]{3,20}$"
        return bool(re.fullmatch(pattern, username))

    @staticmethod
    def validate_phone_number(phone: str) -> bool:
        if not phone or not isinstance(phone, str):
            return False
        phone = phone.strip()
    
        if re.fullmatch(r"01[0|1|2|5]\d{8}$", phone):
            return True
        if re.fullmatch(r"20(10|11|12|15)\d{8}$", phone):
            return True
        return False

    @staticmethod
    def validate_national_id(national_id: str) -> bool:
        if not national_id or not isinstance(national_id, str) or not national_id.isdigit():
            return False
        if len(national_id) != 14:
            return False

        century = national_id[0]
        if century not in ["2", "3"]:
            return False

        try:
            year = int(national_id[1:3])
            month = int(national_id[3:5])
            day = int(national_id[5:7])
            datetime.strptime(f"{1900+year if century=='2' else 2000+year}-{month:02d}-{day:02d}", "%Y-%m-%d")
        except ValueError:
            return False

        governorate = int(national_id[7:9])
        if not (1 <= governorate <= 88):
            return False

        return True
