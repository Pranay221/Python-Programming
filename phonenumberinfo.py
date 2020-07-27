import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
ph = input("Please enter the phone number with country code: ")
phone_no = phonenumbers.parse(ph)

#country
print(geocoder.description_for_number(phone_no,'en'))

#carrier
print(carrier.name_for_number(phone_no, 'en'))


