x_max = {'A': 1500, 'B': 1126, 'C': 1294, 'D': 1120, 'E': 753, 'F': 750, 'G': 1482, 'H': 1029, 'I': 319, 'J': 751,
         'K': 757, 'L': 750, 'M': 1495, 'N': 1129, 'O': 1503, 'P': 1004, 'Q': 1503, 'R': 1051, 'S': 1020, 'T': 1126,
         'U': 1130, 'V': 1130, 'W': 1500, 'X': 1124, 'Y': 1125, 'Z': 1124,
         'a': 755, 'b': 753, 'c': 647, 'd': 754, 'e': 742, 'f': 468, 'g': 757, 'h': 595, 'i': 79, 'j': 638, 'k': 456,
         'l': 0, 'm': 1005, 'n': 610, 'o': 741, 'p': 754, 'q': 1357, 'r': 483, 's': 508, 't': 500, 'u': 597, 'v': 747,
         'w': 1046, 'x': 747, 'y': 747, 'z': 757,
         '0': 1082, '1': 0, '2': 756, '3': 754, '4': 750, '5': 766, '6': 761, '7': 750, '8': 867, '9': 764,
         '!': 129, '"': 332, '#': 1072, '$': 1017, '%': 1262, '&': 1051, "'": 248, '(': 299, ')': 299,
         '*': 941, '+': 941, ',': 80, '-': 553, '.': 79, '/': 535, ':': 82, ';': 80, '<': 770, '=': 584,
         '>': 769, '?': 653, '@': 1854}


# Glyph 0-9
# 51 --> 0
def glyph_num_0():
    x = [534, 310, 0, 0, 0, 317, 541, 765, 1082, 1082, 1082, 772, 548]
    y = [0, 0, 438, 750, 1061, 1500, 1500, 1500, 1061, 750, 438, 0, 0]
    return x, y


# 52 --> 1
def glyph_num_1():
    x = [0, 0]
    y = [0, 1500]
    return x, y


# 53 --> 2
def glyph_num_2():
    x = [7, 7, 226, 382, 537, 756, 756, 756, 550, 0, 754]
    y = [1125, 1281, 1502, 1502, 1502, 1281, 1125, 940, 696, 0, 0]
    return x, y


def glyph_num_3():
    x = [[0, 0, 219, 375, 530, 749, 749, 749, 543, 394],[394,545, 754, 754, 754, 535, 380, 224, 5, 5]]
    y = [[1125, 1281, 1502, 1502, 1502, 1281, 1125, 976, 757, 749], [741,741, 526, 377, 221, 0, 0, 0, 222, 377]]
    return x, y


def glyph_num_4():
    x = [[498, 498], [0, 0, 750]]
    y = [[1500, 0], [1497, 750, 750]]
    return x, y


def glyph_num_5():
    x = [0, 132, 315, 501, 635, 766, 766, 766, 632, 502, 317, 139, 6, 7, 757]
    y = [131, -1, -1, -1, 133, 265, 452, 642, 776, 906, 906, 906, 786, 1500, 1500]
    return x, y


def glyph_num_6():
    x = [7, 15, 234, 384, 539, 761, 761, 761, 539, 384, 253, 146, 0, 0, 0, 385]
    y = [393, 543, 749, 749, 749, 530, 375, 219, 0, 0, 0, 93, 219, 464, 859, 1500]
    return x, y


def glyph_num_7():
    x = [377, 750, 0]
    y = [0, 1497, 1497]
    return x, y


# 59 --> 8
def glyph_num_8():
    x = [867, 189, 0, -2, -5, 68, 145, 296, 488, 594, 690, 694, 695, 695, 695, 661, 614, 488, 368, 278, 168, 168, 168,
         363, 494, 592, 700, 781]
    y = [1500, 686, 484, 355, 191, 98, 0, 0, 0, 81, 156, 281, 326, 339, 432, 499, 593, 686, 774, 900, 1054, 1185, 1315,
         1500, 1500, 1500, 1464, 1405]
    return x, y


# 60 --> 9
def glyph_num_9():
    x = [[763, 764], [384, 534, 756, 763], [0, 0, 227, 384], [377, 221, 0, 0], [764, 757, 529, 377]]
    y = [[1147, 0], [1500, 1500, 1296, 1147], [1128, 1282, 1500, 1500], [753, 753, 972, 1128], [1105, 956, 753, 753]]
    return x, y


# Special Symbols
# 36 --> !
def glyph_symbol_exclamation():
    x = [[90, 91], [61, 50, 50], [90, 73, 61], [62, 73, 90], [50, 50, 62], [116, 105, 90], [129, 129, 116],
         [121, 129, 129], [90, 109, 121]]
    y = [[259, 1458], [15, 27, 43], [3, 3, 15], [72, 83, 83], [43, 60, 72], [14, 3, 3], [43, 26, 14], [68, 57, 43],
         [83, 83, 68]]
    return x, y


# 37 --> "
def glyph_symbol_double_quotes():
    x = [[0, 0], [332, 332]]
    y = [[1466, 950], [1466, 954]]
    return x, y


# 38 --> #
def glyph_symbol_hash():
    x = [[445, 148], [923, 621], [1072, 0], [1072, 0]]
    y = [[1500, 0], [1500, 0], [990, 990], [479, 479]]
    return x, y


# 39 --> $
def glyph_symbol_dollar():
    x = [[516, 516],
         [0, 147, 229, 297, 508, 718, 1017, 1017, 1017, 753, 509, 264, 1, 1, 1, 300, 510, 701, 760, 795, 1007]]
    y = [[1698, -204],
         [126, 36, 17, 2, 2, 2, 221, 376, 612, 696, 750, 805, 889, 1126, 1281, 1501, 1501, 1501, 1486, 1478, 1390]]
    return x, y


# 40 --> %
def glyph_symbol_percentage():
    x = [[146, 89, 0, 0, 0, 156, 313, 313, 313, 223, 166],
         [1095, 1037, 948, 948, 948, 1104, 1262, 1262, 1262, 1172, 1115], [1027, 260]]
    y = [[1367, 1367, 1251, 1096, 840, 840, 840, 1110, 1252, 1367, 1367],
         [597, 597, 481, 326, 70, 70, 70, 340, 482, 597, 597], [1500, 0]]
    return x, y


# 41 --> &
def glyph_symbol_ampersand():
    x = [1051, 349, 216, 216, 216, 362, 471, 557, 635, 721, 720, 699, 449, 355, 260, 162, 100, 0, 0, 0, 51, 80, 168,
         271, 388, 550, 656, 735, 812, 994, 1033]
    y = [30, 961, 1088, 1227, 1336, 1493, 1503, 1511, 1444, 1368, 1249, 1056, 905, 837, 769, 693, 605, 462, 337, 246,
         151, 98, 53, 0, 0, 0, 50, 87, 171, 367, 539]
    return x, y


# 42--> '
def glyph_symbol_single_quotes():
    x = [248, 248, 200]
    y = [1466, 1221, 947]
    return x, y


# 43 ->(
def glyph_symbol_1st_brace_open():
    x = [299, 179, 139, 0, 0, 0, 299]
    y = [1491, 1284, 1194, 878, 530, 49, -431]
    return x, y


# 44 -> )
def glyph_symbol_1st_brace_close():
    x = [0, 299, 299, 299, 161, 120, 0]
    y = [-431, 49, 530, 876, 1191, 1284, 1491]
    return x, y


# 45 --> *
def glyph_symbol_star():
    x = [[465, 465], [941, 0], [136, 797], [798, 133]]
    y = [[1188, 253], [728, 728], [1047, 386], [1058, 393]]
    return x, y


# 46 --> +
def glyph_symbol_plus():
    x = [[465, 465], [941, 0]]
    y = [[1188, 253], [728, 728]]
    return x, y


# 47 --> ,
def glyph_symbol_comma():
    x = [[11, 23, 40, 49, 24, 80, 80, 80, 79], [11, 0, 0], [12, 23, 40], [0, 0, 12], [40], [71, 79, 79], [40, 59, 71]]
    y = [[12, 0, 0, -57, -103, -48, 21, 31, 40], [12, 24, 40], [68, 80, 80], [40, 57, 68], [0], [65, 54, 40],
         [80, 80, 65]]
    return x, y


# 48 --> -
def glyph_symbol_dash():
    x = [0, 553]
    y = [621, 621]
    return x, y


# 49 --> .
def glyph_symbol_period():
    x = [[11, 0, 0], [40, 23, 11], [12, 23, 40], [0, 0, 12], [66, 55, 40], [79, 79, 66], [71, 79, 79], [40, 59, 71]]
    y = [[12, 24, 40], [0, 0, 12], [68, 80, 80], [40, 57, 68], [10, 0, 0], [40, 22, 10], [65, 54, 40], [80, 80, 65]]
    return x, y


# 50 --> /
def glyph_symbol_forward_slash():
    x = [0, 535]
    y = [0, 1500]
    return x, y


# 61 --> :(colon)
def glyph_symbol_colon():
    x = [[14, 3, 3], [42, 26, 14], [14, 26, 42], [3, 3, 14], [69, 58, 42], [82, 82, 69], [73, 82, 82], [42, 61, 73],
         [11, 0, 0], [40, 23, 11], [12, 23, 40], [0, 0, 12], [66, 55, 40], [79, 79, 66], [71, 79, 79], [40, 59, 71]]
    y = [[12, 24, 40], [0, 0, 12], [68, 80, 80], [40, 57, 68], [10, 0, 0], [40, 22, 10], [65, 54, 40], [80, 80, 65],
         [605, 616, 633], [593, 593, 605], [661, 673, 673], [633, 649, 661], [603, 593, 593], [633, 615, 603],
         [657, 646, 633], [673, 673, 657]]
    return x, y


# 62 --> ; (semicolon)
def glyph_symbol_semicolon():
    x = [[11, 23, 40, 49, 24, 80, 80, 80, 79], [11, 0, 0], [12, 23, 40], [0, 0, 12], [40], [71, 79, 79], [40, 59, 71],
         [12, 0, 0], [40, 23, 12], [12, 23, 40], [0, 0, 12], [66, 55, 40], [79, 79, 66], [71, 79, 79], [40, 59, 71]]
    y = [[12, 0, 0, -57, -103, -48, 21, 31, 40], [12, 24, 40], [68, 80, 80], [40, 57, 68], [0], [65, 54, 40],
         [80, 80, 65], [605, 616, 633], [593, 593, 605], [661, 673, 673], [633, 649, 661], [603, 593, 593],
         [633, 615, 603], [657, 646, 633], [673, 673, 657]]
    return x, y


# 63 --> <
def glyph_symbol_angle_brace_open():
    x = [770, 0, 770]
    y = [1040, 724, 405]
    return x, y


# 64 --> =
def glyph_symbol_equal():
    x = [[0, 584], [0, 584]]
    y = [[884, 885], [439, 440]]
    return x, y


# 65 --> >
def glyph_symbol_angle_brace_close():
    x = [0, 769, 0]
    y = [405, 724, 1040]
    return x, y


# 66 --> ?
def glyph_symbol_question_mark():
    x = [[303, 303], [415, 303, 303], [598, 575, 512, 463, 415], [649, 653, 621, 598], [356, 475, 560, 640, 649],
         [0, 66, 169, 262, 356], [283, 272, 272], [312, 295, 283], [284, 295, 312], [272, 272, 284], [338, 327, 312],
         [351, 351, 338], [343, 351, 351], [312, 331, 343]]
    y = [[517, 314], [687, 620, 517], [812, 781, 743, 715, 687], [1026, 978, 844, 812], [1274, 1268, 1191, 1119, 1026],
         [1066, 1173, 1229, 1279, 1274], [12, 24, 40], [0, 0, 12], [68, 80, 80], [40, 57, 68], [10, 0, 0], [40, 22, 10],
         [65, 54, 40], [80, 80, 65]]
    return x, y


# 67 --> @
def glyph_symbol_at():
    x = [[1292, 1291, 1291, 1416, 1505, 1723, 1778, 1828, 1838, 1847, 1847, 1847, 1579, 1316, 928, 543, 0, 0, 0, 543,
          928, 1271, 1429, 1580, 1854], [1291, 1284, 1065, 915, 759, 538, 538, 538, 759, 915, 1064, 1283, 1291]]
    y = [[909, 160, -9, -9, -9, 154, 261, 372, 426, 471, 602, 971, 1214, 1453, 1453, 1453, 926, 553, 180, -347, -347,
          -347, -287, -229, 0], [516, 366, 160, 160, 160, 379, 535, 690, 909, 909, 909, 703, 554]]
    return x, y


# Glyph A-Z
# 68 --> A
def glyph_A():
    x = [[0, 752, 1500], [248, 1251]]
    y = [[0, 1501, 0], [496, 495]]
    return x, y


# 69 --> B
def glyph_B():
    # x = [[0,700],[2, 650, 826, 1045, 1045, 1045, 832, 678], [0, 0, 746, 902, 1126, 1121, 1116, 971, 841, 672]]
    # y = [[1500,1500],[749, 749, 749, 969, 1123, 1278, 1500, 1500], [1500, 0, 0, 0, 218, 371, 545, 653, 749, 749]]
    # x = [[0,700],[2, 650, 826, 1045, 1045, 1045, 832, 678], [0, 0,],[ 746, 902, 1126, 1121, 1116, 971, 841, 672]]
    # y = [[1500,1500],[749, 749, 749, 969, 1123, 1278, 1500, 1500], [1500, 0,],[ 0, 0, 218, 371, 545, 653, 749, 749]]
    x = [[0,700],[2, 650, 826, 1045, 1045, 1045, 832, 678], [0, 0],[0,746, 902,],[902, 1126, 1121, 1116, 971, 841, 672]]
    y = [[1500,1500],[749, 749, 749, 969, 1123, 1278, 1500, 1500], [1500, 0],[0,0, 0,],[0, 218, 371, 545, 653, 749, 749]]
    return x, y

'''def glyph_B():
    x = [[2, 672, 826, 1045, 1045, 1045,1000,632],[802, 1126, 1121, 1116, 971, 841, 500]]
    y = [[749, 749, 749, 969, 1123, 1278,1450,1500],[0, 118, 371, 545, 653, 849, 749]]
    return x, y'''
# 70 --> C
def glyph_C():
    x = [1291, 1069, 754, 444, 0, 0, 0, 444, 754, 1071, 1294]
    y = [226, 2, 2, 2, 441, 751, 1061, 1500, 1500, 1500, 1272]
    return x, y


# 71 --> D
def glyph_D():
    x = [[0, 0], [489, 0], [497, 774, 950, 1120, 1120, 1120, 946, 769, 489], [0, 497]]
    y = [[0, 1500], [0, 0], [1500, 1500, 1275, 1058, 734, 414, 209, 0, 0], [1500, 1500]]
    return x, y


# 72 --> E
def glyph_E():
    x = [[2, 500], [753, 0, 0, 753]]
    y = [[754, 754], [0, 0, 1500, 1500]]
    return x, y


# 73 --> F
def glyph_F():
    x = [[2, 499], [0, 0, 750]]
    y = [[751, 752], [0, 1500, 1500]]
    return x, y


# 74 --> G
def glyph_G():
    x = [[1365, 1259, 1099, 936, 754, 443, 0, 0, 0, 443, 754, 1008, 1415, 1482], [1482, 773]]
    y = [[1188, 1332, 1414, 1498, 1498, 1498, 1059, 749, 439, 0, 0, 0, 308, 552], [552, 552]]
    return x, y


# 75 --> H
def glyph_H():
    x = [[1029, 1028], [1028, 1], [0, 0]]
    y = [[1500, 0], [744, 744], [0, 1500]]
    return x, y


# 76 --> I
def glyph_I():
    x = [[159, 159], [319, 5], [314, 0]]
    y = [[0, 1500], [0, 0], [1500, 1500]]
    return x, y


def glyph_J():
    x = [0, 0, 222, 377, 532, 751, 751, 751]
    y = [371, 217, 0, 0, 0, 211, 364, 1500]
    return x, y


def glyph_K():
    x = [[757, 2, 757], [0, 0]]
    y = [[0, 746, 1500], [0, 1500]]
    return x, y


def glyph_L():
    x = [750, 0, 0]
    y = [0, 0, 1500]
    return x, y


def glyph_M():
    x = [0, 0, 751, 1495, 1495]
    y = [0, 1500, 0, 1500, 0]
    return x, y


def glyph_N():
    x = [1129, 1129, 0, 0]
    y = [1500, 0, 1500, 0]
    return x, y


def glyph_O():
    x = [[1503, 1503, 1072, 762], [752, 1063, 1503, 1503], [0, 0, 440, 752], [762, 449, 0, 0]]
    y = [[750, 438, 0, 0], [1500, 1500, 1061, 750], [750, 1061, 1500, 1500], [0, 0, 440, 750]]
    return x, y


def glyph_P():
    x = [0, 630, 784, 1004, 1004, 1004, 790, 637, 0, 0]
    y = [749, 749, 749, 969, 1123, 1278, 1500, 1500, 1500, 0]
    return x, y


def glyph_Q():
    x = [[1503, 1503, 1054, 742], [752, 1063, 1503, 1503], [0, 0, 440, 752], [742, 431, 0, 0], [1503, 1178]]
    y = [[750, 440, 0, 0], [1500, 1500, 1061, 750], [750, 1061, 1500, 1500], [0, 0, 438, 750], [0, 324]]
    return x, y


def glyph_R():
    x = [[0, 670, 824, 1044, 1044, 1044, 830, 677, 0, 0], [1051, 494]]
    y = [[749, 749, 749, 969, 1123, 1278, 1500, 1500, 1500, 0], [0, 749]]
    return x, y


def glyph_S():
    x = [0, 136, 261, 324, 511, 722, 1020, 1020, 1020, 870, 728, 509, 283, 151, 4, 4, 4, 302, 513, 800, 923]
    y = [146, 39, 13, 0, 2, 3, 221, 376, 527, 637, 740, 769, 798, 883, 978, 1126, 1281, 1501, 1501, 1501, 1396]
    return x, y


def glyph_T():
    x = [[0, 1126], [565, 565]]
    y = [[1500, 1500], [0, 1500]]
    return x, y


def glyph_U():
    x = [1130, 1130, 1130, 796, 565, 333, 168, 0, 0, 0]
    y = [1500, 553, 322, 0, 0, 0, 160, 322, 553, 1500]
    return x, y


def glyph_V():
    x = [1130, 571, 0]
    y = [1500, 0, 1500]
    return x, y


def glyph_W():
    x = [0, 375, 752, 1127, 1500]
    y = [1500, 0, 1500, 0, 1500]
    return x, y


def glyph_X():
    x = [[0, 1118], [1124, 0]]
    y = [[1500, 0], [1500, 0]]
    return x, y


# 92 --> Y
def glyph_Y():
    x = [[0, 561, 1125], [561, 561]]
    y = [[1500, 737, 1500], [737, 0]]
    return x, y


# 93 --> Z
def glyph_Z():
    x = [1124, 0, 1123, 0]
    y = [0, 0, 1500, 1500]
    return x, y


# 94--> [
def glyph_symbol_3rd_brace_open():
    x = [217, 0, 0, 217]
    y = [1487, 1487, -88, -88]
    return x, y


# 95 --> \
def glyph_symbol_back_slash():
    x = [0, 522]
    y = [1500, 0]
    return x, y


# 96--> ]
def glyph_symbol_3rd_brace_close():
    x = [0, 217, 217, 0]
    y = [-88, -88, 1487, 1487]
    return x, y


# 97---> ^
def glyph_symbol_carrot():
    x = [487, 240, 0]
    y = [880, 1477, 880]
    return x, y


# 98---> -
def glyph_symbol_hyphen():
    x = [0, 1193]
    y = [-277, -277]
    return x, y


# 99 --> Back quote (`)
def glyph_symbol_back_quote():
    x = [231, 0]
    y = [1194, 1474]
    return x, y


# Glyph a-z
# 100 --> a
def glyph_a():
    x = [[754, 754], [754, 754], [377], [0, 0, 222, 377], [377, 221, 0, 0], [755, 755, 640, 528, 377],
         [377, 528, 755, 755]]
    y = [[375, 749], [0, 375], [749], [375, 530, 749, 749], [0, 0, 219, 375], [376, 530, 641, 749, 749],
         [0, 0, 221, 376]]
    return x, y


# 101 --> b
def glyph_b():
    x = [[0, 0], [0, 0], [0, 0, 100, 207, 376], [376, 224, 114, 0, 0], [753, 753, 531, 376], [376, 531, 753, 753]]
    y = [[395, 0], [1500, 395], [395, 237, 123, 0, 0], [749, 749, 648, 544, 395], [375, 530, 749, 749],
         [0, 0, 219, 375]]
    return x, y


# 102 --> c
def glyph_c():
    x = [645,  534, 377, 222, 0, 0, 0, 222, 377, 536, 647]
    y = [112, 0, 0, 0, 220, 375, 529, 749, 749, 749, 635]
    return x, y


# 103 --> d
def glyph_d():
    x = [[754, 754], [754, 754], [0, 0, 221, 377], [377, 221, 0, 0], [753, 752, 640, 525, 377], [377, 528, 751, 753]]
    y = [[394, 1500], [0, 394], [375, 530, 749, 749], [0, 0, 219, 375], [394, 247, 126, 0, 0], [749, 749, 539, 394]]
    return x, y


def glyph_e():
    x = [[6, 742], [742, 728, 616, 509, 377, 222, 0, 0, 0, 113, 230, 413, 493, 583, 680, 742]]
    y = [[429, 428], [428, 564, 658, 749, 749, 749, 530, 375, 216, 110, 0, 0, 0, 34, 72, 134]]
    return x, y


def glyph_f():
    x = [[153, 153, 153, 244, 313, 390, 432, 468, 468], [314, 0]]
    y = [[0, 1334, 1401, 1500, 1500, 1500, 1449, 1404, 1334], [755, 755]]
    return x, y


def glyph_g():
    x = [[754, 746, 527, 377, 222, 0, 0, 0, 222, 377, 526, 746, 753], [158, 158, 333, 457, 581, 757, 757, 757]]
    y = [[356, 207, 0, 0, 0, 220, 375, 529, 749, 749, 749, 543, 394], [-445, -569, -747, -747, -747, -569, -445, 748]]
    return x, y


def glyph_h():
    x = [[0, 0], [595, 595, 595, 420, 296, 172, 0, 0]]
    y = [[0, 1500], [0, 450, 575, 752, 752, 752, 576, 452]]
    return x, y


def glyph_i():
    x = [[11, 0, 0], [40, 23, 11], [41, 40], [12, 23, 40], [0, 0, 12], [66, 55, 40], [79, 79, 66], [71, 79, 79],
         [40, 59, 71]]
    y = [[1061, 1073, 1089], [1049, 1049, 1061], [0, 748], [1117, 1129, 1129], [1089, 1106, 1117], [1059, 1049, 1049],
         [1089, 1071, 1059], [1114, 1103, 1089], [1129, 1129, 1114]]
    return x, y


def glyph_j():
    x = [[0, 0, 176, 300, 423, 599, 599, 599], [570, 559, 559], [598, 582, 570], [570, 582, 598], [559, 559, 570],
         [625, 613, 598], [638, 638, 625], [629, 638, 638], [598, 617, 629]]
    y = [[-445, -569, -747, -747, -747, -569, -445, 748], [1055, 1067, 1083], [1043, 1043, 1055], [1112, 1123, 1123],
         [1083, 1100, 1112], [1054, 1043, 1043], [1083, 1066, 1054], [1108, 1097, 1083], [1123, 1123, 1108]]
    return x, y


def glyph_k():
    x = [[0, 0], [456, 0], [0, 450]]
    y = [[1500, 0], [750, 386], [386, 0]]
    return x, y


def glyph_l():
    x = [0, 0]
    y = [0, 1500]
    return x, y


def glyph_m():
    x = [[1005, 1005, 1005, 859, 755, 651, 506, 506, 506, 359, 255, 151, 3, 3], [0, 0], [506, 506]]
    y = [[0, 521, 621, 765, 765, 765, 621, 521, 621, 765, 765, 765, 623, 524], [0, 750], [0, 521]]
    return x, y


def glyph_n():
    x = [[0, 0], [610, 610, 610, 435, 311, 186, 0, 0], [0]]
    y = [[0, 750], [0, 447, 572, 752, 752, 752, 575, 452], [750]]
    return x, y


def glyph_o():
    x = [[0, 0, 222, 377], [377, 221, 0, 0], [740, 732, 630, 525, 377], [377, 525, 741, 740]]
    y = [[375, 530, 749, 749], [0, 0, 219, 375], [369, 216, 109, 0, 0], [749, 749, 521, 369]]
    return x, y


def glyph_p():
    x = [[0, 0], [1, 8, 227, 377, 533, 754, 754, 754, 533, 377, 227, 8, 1]]
    y = [[-750, 753], [356, 206, 0, 0, 0, 219, 375, 530, 749, 749, 749, 543, 394]]
    return x, y


def glyph_q():
    x = [[759], [377, 527, 751, 759], [0, 0, 222, 377], [377, 222, 0, 0], [759, 752, 528, 377], [759], [758, 758],
         [758, 758], [1357, 1357, 1174, 1050, 927, 758, 758, 758]]
    y = [[390], [749, 749, 539, 390], [375, 529, 749, 749], [0, 0, 220, 375], [353, 205, 0, 0], [353], [404, 748],
         [349, 404], [-445, -569, -750, -750, -750, -570, -445, 349]]
    return x, y


def glyph_r():
    x = [[0, 0, 145, 243, 342, 483, 483], [0, 0]]
    y = [[514, 613, 765, 765, 765, 623, 524], [0, 748]]
    return x, y


def glyph_s():
    x = [0, 73, 114, 148, 254, 359, 508, 508, 508, 377, 254, 132, 0, 0, 0, 150, 255, 402, 504]
    y = [62, 17, 8, 0, 0, 0, 110, 187, 305, 347, 374, 402, 444, 562, 640, 749, 749, 749, 694]
    return x, y


def glyph_t():
    x = [[255, 255], [500, 0]]
    y = [[0, 1127], [748, 748]]
    return x, y


def glyph_u():
    x = [[597, 597], [1, 0, 0, 175, 300, 423, 597, 597]]
    y = [[752, 0], [752, 302, 177, 0, 0, 0, 179, 304]]
    return x, y


def glyph_v():
    x = [0, 370, 747]
    y = [746, 0, 747]
    return x, y


def glyph_w():
    x = [1046, 764, 529, 239, 0]
    y = [737, 0, 733, 0, 752]
    return x, y


def glyph_x():
    x = [[0, 744], [746, 0]]
    y = [[747, 0], [749, 0]]
    return x, y


# 124 --> y
def glyph_y():
    x = [[370, 0], [747, 0]]
    y = [[0, 746], [747, -750]]
    return x, y


# 125 --> z
def glyph_z():
    x = [757, 0, 740, 0]
    y = [0, 0, 748, 748]
    return x, y


# 126 --> {
def glyph_symbol_2nd_brace_open():
    x = [412, 381, 270, 236, 209, 209, 209, 198, 181, 94, 0, 132, 178, 209, 209, 209, 213, 222, 264, 297, 381, 412]
    y = [1494, 1494, 1494, 1446, 1408, 1289, 1025, 958, 854, 735, 690, 635, 505, 417, 240, 43, 8, -68, -94, -114, -114,
         -114]
    return x, y


# 127--> |
def glyph_symbol_pipe():
    x = [0, 0]
    y = [1492, -338]
    return x, y


# 128 --> }
def glyph_symbol_2nd_brace_close():
    x = [0, 31, 142, 176, 203, 203, 203, 212, 241, 412, 278, 234, 203, 203, 203, 198, 189, 147, 115, 31, 0]
    y = [-114, -114, -114, -66, -28, 92, 345, 409, 618, 690, 754, 876, 960, 1141, 1330, 1374, 1450, 1475, 1494, 1494,
         1494]
    return x, y


# 129 --> ~
def glyph_symbol_tilde():
    x = [0, 106, 278, 387, 592, 703, 765, 898, 1023]
    y = [622, 742, 742, 742, 655, 608, 608, 608, 745]
    return x, y

def glyph_space():
    x=[0,755]
    y=[0,0]
    return x,y
def return_manuscript_fonts(xxx):
    c1 = []
    c2 = []
    if xxx == 'A':
        c1, c2 = glyph_A()
    elif xxx == 'B':
        c1, c2 = glyph_B()
    elif xxx == 'C':
        c1, c2 = glyph_C()
    elif xxx == 'D':
        c1, c2 = glyph_D()
    elif xxx == 'E':
        c1, c2 = glyph_E()
    elif xxx == 'F':
        c1, c2 = glyph_F()
    elif xxx == 'G':
        c1, c2 = glyph_G()
    elif xxx == 'H':
        c1, c2 = glyph_H()
    elif xxx == 'I':
        c1, c2 = glyph_I()
    elif xxx == 'J':
        c1, c2 = glyph_J()
    elif xxx == 'K':
        c1, c2 = glyph_K()
    elif xxx == 'L':
        c1, c2 = glyph_L()
    elif xxx == 'M':
        c1, c2 = glyph_M()
    elif xxx == 'N':
        c1, c2 = glyph_N()
    elif xxx == 'O':
        c1, c2 = glyph_O()
    elif xxx == 'P':
        c1, c2 = glyph_P()
    elif xxx == 'Q':
        c1, c2 = glyph_Q()
    elif xxx == 'R':
        c1, c2 = glyph_R()
    elif xxx == 'S':
        c1, c2 = glyph_S()
    elif xxx == 'T':
        c1, c2 = glyph_T()
    elif xxx == 'U':
        c1, c2 = glyph_U()
    elif xxx == 'V':
        c1, c2 = glyph_V()
    elif xxx == 'W':
        c1, c2 = glyph_W()
    elif xxx == 'X':
        c1, c2 = glyph_X()
    elif xxx == 'Y':
        c1, c2 = glyph_Y()
    elif xxx == 'Z':
        c1, c2 = glyph_Z()

    elif xxx == 'a':
        c1, c2 = glyph_a()
    elif xxx == 'b':
        c1, c2 = glyph_b()
    elif xxx == 'c':
        c1, c2 = glyph_c()
    elif xxx == 'd':
        c1, c2 = glyph_d()
    elif xxx == 'e':
        c1, c2 = glyph_e()
    elif xxx == 'f':
        c1, c2 = glyph_f()
    elif xxx == 'g':
        c1, c2 = glyph_g()
    elif xxx == 'h':
        c1, c2 = glyph_h()
    elif xxx == 'i':
        c1, c2 = glyph_i()
    elif xxx == 'j':
        c1, c2 = glyph_j()
    elif xxx == 'k':
        c1, c2 = glyph_k()
    elif xxx == 'l':
        c1, c2 = glyph_l()
    elif xxx == 'm':
        c1, c2 = glyph_m()
    elif xxx == 'n':
        c1, c2 = glyph_n()
    elif xxx == 'o':
        c1, c2 = glyph_o()
    elif xxx == 'p':
        c1, c2 = glyph_p()
    elif xxx == 'q':
        c1, c2 = glyph_q()
    elif xxx == 'r':
        c1, c2 = glyph_r()
    elif xxx == 's':
        c1, c2 = glyph_s()
    elif xxx == 't':
        c1, c2 = glyph_t()
    elif xxx == 'u':
        c1, c2 = glyph_u()
    elif xxx == 'v':
        c1, c2 = glyph_v()
    elif xxx == 'w':
        c1, c2 = glyph_w()
    elif xxx == 'x':
        c1, c2 = glyph_x()
    elif xxx == 'y':
        c1, c2 = glyph_y()
    elif xxx == 'z':
        c1, c2 = glyph_z()

    elif xxx == '0':
        c1, c2 = glyph_num_0()
    elif xxx == '1':
        c1, c2 = glyph_num_1()
    elif xxx == '2':
        c1, c2 = glyph_num_2()
    elif xxx == '3':
        c1, c2 = glyph_num_3()
    elif xxx == '4':
        c1, c2 = glyph_num_4()
    elif xxx == '5':
        c1, c2 = glyph_num_5()
    elif xxx == '6':
        c1, c2 = glyph_num_6()
    elif xxx == '7':
        c1, c2 = glyph_num_7()
    elif xxx == '8':
        c1, c2 = glyph_num_8()
    elif xxx == '9':
        c1, c2 = glyph_num_9()

    elif xxx == '!':
        c1, c2 = glyph_symbol_exclamation()
    elif xxx == '"':
        c1, c2 = glyph_symbol_double_quotes()
    elif xxx == '#':
        c1, c2 = glyph_symbol_hash()
    elif xxx == '$':
        c1, c2 = glyph_symbol_dollar()
    elif xxx == '%':
        c1, c2 = glyph_symbol_percentage()
    elif xxx == '&':
        c1, c2 = glyph_symbol_ampersand()
    elif xxx == "'":
        c1, c2 = glyph_symbol_single_quotes()
    elif xxx == '(':
        c1, c2 = glyph_symbol_1st_brace_open()
    elif xxx == ')':
        c1, c2 = glyph_symbol_1st_brace_close()
    elif xxx == '*':
        c1, c2 = glyph_symbol_star()
    elif xxx == '+':
        c1, c2 = glyph_symbol_plus()
    elif xxx == ',':
            c1, c2 = glyph_symbol_comma()
    elif xxx == '-':
            c1, c2 = glyph_symbol_dash()
    elif xxx == '.':
            c1, c2 = glyph_symbol_period()
    elif xxx == '/':
            c1, c2 = glyph_symbol_forward_slash()
    elif xxx == ':':
        c1, c2 = glyph_symbol_colon()
    elif xxx == ';':
        c1, c2 = glyph_symbol_semicolon()
    elif xxx == '<':
        c1, c2 = glyph_symbol_angle_brace_open()
    elif xxx == '=':
        c1, c2 = glyph_symbol_equal()
    elif xxx == '>':
        c1, c2 = glyph_symbol_angle_brace_close()
    elif xxx == '?':
        c1, c2 = glyph_symbol_question_mark()
    elif xxx == '@':
        c1, c2 = glyph_symbol_at()
    elif xxx=='space':
        c1,c2=glyph_space()

    else:
        c1 = []
        c2 = []
        
    # elif xxx == '':
    #     c1, c2 =

    return c1, c2
