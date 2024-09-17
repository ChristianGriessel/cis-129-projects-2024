import random
import time

alphabet = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
    'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
    'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
    'a': 27, 'b': 28, 'c': 29, 'd': 30, 'e': 31, 'f': 32, 'g': 33,
    'h': 34, 'i': 35, 'j': 36, 'k': 37, 'l': 38, 'm': 39, 'n': 40,
    'o': 41, 'p': 42, 'q': 43, 'r': 44, 's': 45, 't': 46, 'u': 47,
    'v': 48, 'w': 49, 'x': 50, 'y': 51, 'z': 52, ' ': 53,
    '.': 54, ',': 55, '!': 56, '?': 57, ':': 58, ';': 59,
    '-': 60, '(': 61, ')': 62, '[': 63, ']': 64, '{': 65, '}': 66,
    '\'': 67, '\"': 68, '@': 69, '#': 70, '$': 71, '%': 72, '^': 73,
    '&': 74, '*': 75, '_': 76, '+': 77, '=': 78, '/': 79, '\\': 80,
    '|': 81, '<': 82, '>': 83, '~': 84, '`': 85
}

the_same_alphabet_but_reversed = {
    1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H',
    9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
    16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V',
    23: 'W', 24: 'X', 25: 'Y', 26: 'Z',
    27: 'a', 28: 'b', 29: 'c', 30: 'd', 31: 'e', 32: 'f', 33: 'g',
    34: 'h', 35: 'i', 36: 'j', 37: 'k', 38: 'l', 39: 'm', 40: 'n',
    41: 'o', 42: 'p', 43: 'q', 44: 'r', 45: 's', 46: 't', 47: 'u',
    48: 'v', 49: 'w', 50: 'x', 51: 'y', 52: 'z', 53: ' ',
    54: '.', 55: ',', 56: '!', 57: '?', 58: ':', 59: ';',
    60: '-', 61: '(', 62: ')', 63: '[', 64: ']', 65: '{', 66: '}',
    67: '\'', 68: '\"', 69: '@', 70: '#', 71: '$', 72: '%', 73: '^',
    74: '&', 75: '*', 76: '_', 77: '+', 78: '=', 79: '/', 80: '\\',
    81: '|', 82: '<', 83: '>', 84: '~', 85: '`'
}

def optimal_the_same_alphabet_but_reversed_comber_function(value):
    return the_same_alphabet_but_reversed.get(value)

def main():
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis = ''
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        H())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        e())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        l())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        l2())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        o())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        space())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        w())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        o2())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        r())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        l3())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        d())
    print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis += optimal_the_same_alphabet_but_reversed_comber_function(
        exclimationpoint())

    print(print_openparenthesis_Hello_world_exlimationpoint_closeparenthesis + " :^)")


def H():
    while True:
        H_VALUE = random.randint(1, 85)
        print(H_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if H_VALUE == alphabet["H"]:
            print("H HAS BEEN FOUND")
            return H_VALUE
        else:
            continue

def e():
    while True:
        e_VALUE = random.randint(1, 85)
        print(e_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if e_VALUE == alphabet["e"]:
            print("e HAS BEEN FOUND")
            return e_VALUE
        else:
            continue

def l():
    while True:
        l_VALUE = random.randint(1, 85)
        print(l_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if l_VALUE == alphabet["l"]:
            print("l HAS BEEN FOUND")
            return l_VALUE
        else:
            continue

def l2():
    while True:
        l_VALUE = random.randint(1, 85)
        print(l_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if l_VALUE == alphabet["l"]:
            print("l HAS BEEN FOUND")
            return l_VALUE
        else:
            continue

def o():
    while True:
        o_VALUE = random.randint(1, 85)
        print(o_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if o_VALUE == alphabet["o"]:
            print("o HAS BEEN FOUND")
            return o_VALUE
        else:
            continue

def space():
    while True:
        space_VALUE = random.randint(1, 85)
        print(space_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if space_VALUE == alphabet[' ']:
            print("A SPACE HAS BEEN FOUND")
            return space_VALUE
        else:
            continue
def w():
    while True:
        w_VALUE = random.randint(1, 85)
        print(w_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if w_VALUE == alphabet["w"]:
            print("w HAS BEEN FOUND")
            return w_VALUE
        else:
            continue

def o2():
    while True:
        o_VALUE = random.randint(1, 85)
        print(o_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if o_VALUE == alphabet["o"]:
            print("o HAS BEEN FOUND")
            return o_VALUE
        else:
            continue

def r():
    while True:
        r_VALUE = random.randint(1, 85)
        print(r_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if r_VALUE == alphabet["r"]:
            print("r HAS BEEN FOUND")
            return r_VALUE
        else:
            continue

def l3():
    while True:
        l_VALUE = random.randint(1, 85)
        print(l_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if l_VALUE == alphabet["l"]:
            print("l HAS BEEN FOUND")
            return l_VALUE
        else:
            continue

def d():
    while True:
        d_VALUE = random.randint(1, 85)
        print(d_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if d_VALUE == alphabet["d"]:
            print("d HAS BEEN FOUND")
            return d_VALUE
        else:
            continue


def exclimationpoint():
    while True:
        ex_VALUE = random.randint(1, 85)
        print(ex_VALUE)
        time.sleep(random.uniform(0.1, 0.5))
        if ex_VALUE == alphabet["!"]:
            print("! HAS BEEN FOUND")
            return ex_VALUE
        else:
            continue

main()