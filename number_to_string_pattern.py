c_num = 702

def convert_col_name(c):
    res = ""

    while c > 0:
        rem = c%26

        if rem == 0:
            res = "Z" + res
            c = int(c/26) - 1
        else:
            res = chr(rem-1 + ord("A")) + res
            c = int(c/26)

    return res

print(convert_col_name(c_num))