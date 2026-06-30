import phonenumbers


def normalize_phone(phone):
    try:
        number = phonenumbers.parse(phone, "IN")

        if phonenumbers.is_valid_number(number):
            return phonenumbers.format_number(
                number,
                phonenumbers.PhoneNumberFormat.E164
            )

    except:
        pass

    return None