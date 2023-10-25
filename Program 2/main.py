#Student Name:   James Seely
#Program Title:  Erewhon Mobile Data Plans.
#Description:    calculate the price of cellular data used in the billing period.


def main():
    # get ammount of data used
    dataUsed = float(input("Enter data usage (Mb): "))

    # calculat price
    # Up to and including 200Mb
    if( dataUsed <= 200 ):
        price = 20

    # Over 200Mb and up to and including 500Mb 
    elif( dataUsed <= 500 ):
        price = 0.105 * dataUsed

    # Over 500Mb and up to and including 1Gb 
    elif( dataUsed <= 1024 ):
        price = 0.110 * dataUsed

    # Over 1Gb
    else:
        price = 118

    print( "Total charge is $" + str(price) )


if __name__ == "__main__":
    main()