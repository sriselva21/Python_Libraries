"""This file validates given phone number is valid or not. If it's a valid number we can get the county/region,
time zone, carrier, valid number status"""
from phonenumbers import carrier, geocoder, parse, is_valid_number

phone_no = input('Enter the phone nuber with country code: ')
phone_no_par = parse(phone_no)
print(phone_no_par)

# find carrier of the given mobile number
print(carrier.name_for_number(phone_no_par, "en"))

# find country/region of the given mobile number+91
print(geocoder.description_for_number(phone_no_par,"en"))

# find given mobile number is valid or not
print(is_valid_number(phone_no_par))
