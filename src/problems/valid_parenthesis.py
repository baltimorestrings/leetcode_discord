import argparse

lookup_dict: dict[str, str] = {
    "}" : "{",
    ")": "(",
    "]": "["
}
def is_valid_parenthesis(parenthesis: str) -> bool:
    stack: list[str] = []
    for i in range(len(parenthesis)):
        if parenthesis[i] in "}])":
            if len(stack) == 0 or stack.pop() != lookup_dict[parenthesis[i]]:
                return False
        else:
            stack.append(parenthesis[i])
    return True

if __name__ == "__main__":
    a = argparse.ArgumentParser("parenthesis")
    a.add_argument("string", help="only {}[]()")
    args = a.parse_args()
    if not all(c in "()[]{}" for c in args.string):
        raise ValueError("bad input")
    print(is_valid_parenthesis(args.string))
