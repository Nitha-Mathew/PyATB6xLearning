def check_status(status_code):
    match status_code:
        case 200:
            print("PASS")
        case 400:
            print("FAIL")
        case 500:
            print("FAIL")
        case _:
            print("UNKNOWN")

check_status(status_code=int(input("Enter the code")))
