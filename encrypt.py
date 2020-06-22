import io
from six import int2byte

dict_b = {
    5376: -1, 13312: 0, 13568: 1, 13824: 2, 14080: 3, 14336: 4, 14592: 5,
    14848: 6, 15104: 7, 15360: 8, 15616: 9, 15872: 10, 16128: 11, 16384: 12,
    16640: 13, 16896: 14, 17152: 15, 17408: 16, 17664: 17, 17920: 18, 18176:
        19, 18432: 20, 18688: 21, 18944: 22, 19200: 23, 19456: 24, 19968: 25,
    20224: 26, 20480: 27, 20736: 28, 20992: 29, 21248: 30, 21504: 31, 21760:
        32, 22016: 33, 22272: 34, 22528: 35, 22784: 36, 23040: 37, 23296: 38,
    23552: 39, 23808: 40, 24064: 41, 24320: 42, 24576: 43, 24832: 44, 25088:
        45, 25344: 46, 25600: 47, 25856: 48, 26112: 49, 26368: 50, 26624: 51,
    26880: 52, 27136: 53, 27392: 54, 27648: 55, 27904: 56, 28160: 57, 28416:
        58, 28672: 59, 28928: 60, 29184: 61, 29440: 62, 29696: 63, 29952: 64,
    30208: 65, 30464: 66, 30720: 67, 30976: 68, 31232: 69, 31488: 70, 31744:
        71, 32000: 72, 32256: 73, 32512: 74, 32768: 75, 33024: 76, 33280: 77,
    33536: 78, 33792: 79, 34048: 80, 34304: 81, 34560: 82, 34816: 83, 35072:
        84, 35328: 85, 35584: 86, 35840: 87, 36096: 88, 36352: 89, 36608: 90,
    36864: 91, 37120: 92, 37376: 93, 37632: 94, 37888: 95, 38144: 96, 38400:
        97, 38656: 98, 38912: 99, 39168: 100, 39424: 101, 39680: 102, 39936: 103,
    40192: 104, 40448: 105, 41216: 106, 41472: 107, 41728: 108, 42240: 109,
    67072: 110, 73728: 111, 73984: 112, 74240: 113, 77824: 114, 78080: 115,
    78336: 116, 78592: 117, 82944: 118, 83200: 119, 92160: 120, 92416: 121,
    131072: 122, 131328: 123, 131584: 124, 131840: 125, 132096: 126, 132352:
        127, 132608: 128, 132864: 129, 133120: 130, 133376: 131, 133632: 132,
    133888: 133, 134144: 134, 134400: 135, 134656: 136, 134912: 137, 135168:
        138, 135424: 139, 135680: 140, 135936: 141, 136192: 142, 136448: 143,
    136704: 144, 136960: 145, 137216: 146, 137472: 147, 137728: 148, 137984:
        149, 138240: 150, 138496: 151, 138752: 152, 139008: 153, 139264: 154,
    139520: 155, 139776: 156, 140032: 157, 140288: 158, 140544: 159, 140800:
        160, 141056: 161, 141312: 162, 141568: 163, 141824: 164, 142080: 165,
    142336: 166, 142592: 167, 142848: 168, 143104: 169, 143360: 170, 143616:
        171, 143872: 172, 144128: 173, 144384: 174, 144640: 175, 144896: 176,
    145152: 177, 145408: 178, 145664: 179, 145920: 180, 146176: 181, 146432:
        182, 146688: 183, 146944: 184, 147200: 185, 147456: 186, 147712: 187,
    147968: 188, 148224: 189, 148480: 190, 148736: 191, 148992: 192, 149248:
        193, 149504: 194, 149760: 195, 150016: 196, 150272: 197, 150528: 198,
    150784: 199, 151040: 200, 151296: 201, 151552: 202, 151808: 203, 152064:
        204, 152320: 205, 152576: 206, 152832: 207, 153088: 208, 153344: 209,
    153600: 210, 153856: 211, 154112: 212, 154368: 213, 154624: 214, 154880:
        215, 155136: 216, 155392: 217, 155648: 218, 155904: 219, 156160: 220,
    156416: 221, 156672: 222, 156928: 223, 157184: 224, 157440: 225, 157696:
        226, 157952: 227, 158208: 228, 158464: 229, 158720: 230, 158976: 231,
    159232: 232, 159488: 233, 159744: 234, 160000: 235, 160256: 236, 160512:
        237, 160768: 238, 161024: 239, 161280: 240, 161536: 241, 161792: 242,
    162048: 243, 162304: 244, 162560: 245, 162816: 246, 163072: 247, 163328:
        248, 163584: 249, 163840: 250, 164096: 251, 164352: 252, 164608: 253,
    164864: 254, 165120: 255}


def decrypt(strings):
    stream = io.BytesIO()
    done = False
    for ch in strings:
        b1 = ord(ch) & ((1 << 8) - 1)
        try:
            b2 = dict_b[ord(ch) - b1]
        except KeyError:
            raise ValueError('Error')
        b = int2byte(b1) if b2 == -1 else int2byte(b1) + int2byte(b2)
        if len(b) == 1:
            if done:
                raise ValueError('Error')
            done = True
        stream.write(b)
    return stream.getvalue()
