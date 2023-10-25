#Student Name:   James Seely
#Program Title:  Program 1, Assignment 2: Landscape Calculator
#Description:    Computes the price of landscaping.


def main():
    grass = {
        "fescue": 0.05,
        "bentgrass": 0.02,
        "campus": 0.01
    }

    houseNum = int(input("Enter house number: "))
    depth = float(input("enter property depth (feet): "))
    width = float(input("enter property width (feet): "))
    grassType = input("Enter type of grass (fescue, bentgrass, campus): ").lower()
    tree = int(input("Enter the number of trees:"))
    price = 1000

    if( depth * width > 5000 ):
        price += 500

    # calculate grass cost
    price += grass[grassType] * depth * width

    # calculate tree cost
    price += 100 * tree

    print(f"Total cost for house {houseNum} is: ${price}")


if __name__ == "__main__":
    main()