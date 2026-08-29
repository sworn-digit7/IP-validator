import re
import sys


def main():
    print(validates(input("IPv4 Address: ")))



def validates(ip):
    try:
        matches = re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip)

        for i in range(1,5):
            if not 0 <= int(matches.group(i)) <= 255:
                return False

        return True

    except AttributeError:
        return False


if __name__ == "__main__":
    main()