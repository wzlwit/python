import random


def generate_code(code_len=4):
    """
    generate verification code of indicated length

    param code_len: length(default: 4)

    return: random code made of digits and letters
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


print(generate_code())
