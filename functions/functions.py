class Functions:

    def __str__(self):
        print(f"This class is used to store static methods. "
              f"Current methods are {[e for e in dir(self) if e not in dir(object)]}")


    @staticmethod
    def cifra(s: str, clave: int = 3):

        buff = []
        for c in s:
            num = ord(c)

        if 65 <= num < 91:
            new_num = ((num - 65 + clave) % 26) + 65
            buff.append(str(chr(new_num)))
        elif 97 <= num < 123:
            new_num = ((num - 97 + clave) % 26) + 97
            buff.append(str(chr(new_num)))
        else:
            buff.append(c)

        return ''.join(buff)
