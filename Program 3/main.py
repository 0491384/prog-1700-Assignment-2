#Student Name:   James Seely
#Program Title:  Auto insurance calculator.
#Description:    calculate the price of insurance based on risk and vehicle cost.


def main():
    gender = input("Are you `male` or `female`: ").lower()
    age = int(input("Enter your age: "))
    price = float(input("enter price of the vehicle: $"))

    if( gender == "male" ):
        if( age >= 15 ) and ( age < 25 ):
            price = (price * 0.25) / 12
        elif( age >= 25 ) and ( age < 40 ):
            price = (price * 0.17) / 12
        elif( age >= 40 ) and ( age < 70 ):
            price = (price * 0.10) / 12

    elif( gender == "female" ):
        if( age >= 15 ) and ( age < 25 ):
            price = (price * 0.20) / 12
        elif( age >= 25 ) and ( age < 40 ):
            price = (price * 0.15) / 12
        elif( age >= 40 ) and ( age < 70 ):
            price = (price * 0.10) / 12
        
    print(f"{price:.2f}")


if __name__ == "__main__":
    main()