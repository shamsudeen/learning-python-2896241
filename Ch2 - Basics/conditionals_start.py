#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#



def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    # if x < y:
    #     result = "x is smaller than y"
    # elif x > y:
    #     result = "x is larger than y"
    # else:
    #     result = "x and y are equal"

    # print(f"The result of the comparison is {result}")
    
    # # conditional statements let you use "a if C else b"
    # result = "x is less than y" if x  < y else "x is greater than or equal to y"    
    # print(f"Alternate way to express the same result:\n{result}")
    
    # match-case makes it easy to compare multiple values
    value = "three"
    match value:
        case "zero":
            result = 0
        case "one":
            result = 1
        case "two":
            result = 2
        case "tree"   | "four":
            result = (3, 4)
        case _:
            result = -1
            
    print(f"\nMatch Case Result: {result}\n")
if __name__ == "__main__":
    main()
