from pfp import fizzbuzz
import sys

if __name__ == "__main__":
    number = sys.argv[1]
    print(",".join([str(item) for item in fizzbuzz(int(number))]))
