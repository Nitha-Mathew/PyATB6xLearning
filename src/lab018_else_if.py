expected_output=input("Enter the expected output: ").strip()
actual_output=input("Enter the actual output: ").strip()

eo=expected_output.lower()
ao=actual_output.lower()

if eo==ao:
    print("Test passed-tiles matched")
else:
    print("Test failed")

