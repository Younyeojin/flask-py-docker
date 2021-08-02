def str_to_list(payload: str) -> []:
    return [i for i in payload if i.isalnum()]


def reverse_list(ls: []) -> None:
    # s[::-1]
    return


def list_to_str(ls: []) -> str:
    return ''


if __name__ == '__main__':
    ls = str_to_list(input("Input"))
    reversed_ls = reverse_list(ls)
    print(list_to_str(reversed_ls))
