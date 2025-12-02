class InvalidAgeException(Exception):  #Inheritance
    pass
def age_of_drink(age):
    if age<25:
        raise InvalidAgeException("Forbidden Age")
    print("Age allowed")
age_of_drink(98)

