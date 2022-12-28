import argparse


def main() -> str:
    s = "hello"
    print(s)
    return s


def args() -> None:
    parser = argparse.ArgumentParser(
        prog="YAML Bundler", description="Handle !include tag and bundle YAML files."
    )
    parser.add_argument("filename")
    parser.add_argument("-i", "--inplace", action="store_true")
    parser.add_argument("-o", "--out")
    args = parser.parse_args()
    print(str(args))


if __name__ == "__main__":
    args()
