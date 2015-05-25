__author__ = 'chakib'
import random



class sat:
    def __init__(self, clauses=[]):
        self.clauses = clauses.copy()
        self.maxi = -1
        for i in clauses:
            for j in i:
                if abs(j) > self.maxi: self.maxi = abs(j)

    def interpreter(self, interpretation):
        cpt = 0
        return [self.satisfait(c, interpretation) for c in self.clauses]

    def satisfait(self, c, interpretation):
        var = False
        for i in c:
            if i < 0:
                var = var or not interpretation[abs(i) - 1]
            else:
                var = var or interpretation[abs(i) - 1]
            if var: return True
        return False

    def generate_solution(self):
        return [bool(random.getrandbits(1)) for _ in range(self.maxi)]


    def gsat(self, maxiteration=100, maxflip=30):
        solution = self.generate_solution()
        initial = self.interpreter(solution)
        l = initial
        testsolution = solution
        for i in range(maxiteration):

            for j in range(maxflip):
                if l.count(False) == 0: break
                var = self.get_random_var(l)
                testsolution[var] = not testsolution[var]
                l1 = self.interpreter(testsolution)
                if sum(l1) > sum(l):
                    l = l1
                else:
                    testsolution[var] = not testsolution[var]
            if sum(l) > sum(initial):
                solution = testsolution.copy()
                initial = l.copy()

            testsolution = self.generate_solution()
            l = self.interpreter(testsolution)

        return solution

    def get_random_var(self, evaluation):

        c = evaluation.index(False)
        i = abs(random.choice(self.clauses[c])) - 1
        return i


    def generate_problem(self, max_clauses=10, max_vars=10):
        l = []
        self.maxi = max_clauses
        x = list(range(-max_vars, max_vars + 1))
        x.remove(0)

        for i in range(max_clauses):
            l.append([random.choice(x) for _ in range(random.randint(3, max_vars / 2))])
        self.clauses = l
        return l

    def parser(self, nf):
        with open(nf, "r") as f:
            l = []
            for s in f.readlines():
                s = s.split()
                try:
                    c = int(s[0])
                    l.append(self.getclause(s))

                except ValueError:
                    continue

            return l

    def getclause(self, s):
        l = []

        for i in s:
            l.append(int(i))
        l.remove(0)
        return l


c = [[435], [318], [-319], [317], [-39, -433], [37, -433], [39, -434], [-37, -434], [-434, 432], [-433, 432],
     [-79, -37], [-67, -37], [-68, 38], [-68, -79], [-79, -39], [-69, -39], [-76, -67], [-71, -67], [-74, -67],
     [-138, -67], [-72, 68], [-72, -138], [-72, -74], [-72, -76], [-76, -69], [-73, -69], [-74, -69], [-138, -69],
     [75, -138], [-75, 138], [75, -139], [-75, 139], [75, -147], [-75, 147], [-311, -75], [-307, -75], [312, 307],
     [-312, -307], [15, -315], [-15, 315], [15, -316], [-15, 316], [53, -93], [-53, 93], [53, -94], [-53, 94],
     [53, -98], [-53, 98], [53, -102], [-53, 102], [53, -105], [-53, 105], [53, -119], [-53, 119], [53, -121],
     [-53, 121], [53, -124], [-53, 124], [53, -129], [-53, 129], [53, -169], [-53, 169], [53, -207], [-53, 207],
     [53, -221], [-53, 221], [53, -244], [-53, 244], [53, -250], [-53, 250], [53, -304], [-53, 304], [53, -314],
     [-53, 314], [53, -330], [-53, 330], [53, -343], [-53, 343], [53, -345], [-53, 345], [53, -360], [-53, 360],
     [53, -378], [-53, 378], [60, 53], [263, 53], [176, 53], [182, 53], [188, 182], [-188, -182], [104, -187],
     [-104, 187], [104, -188], [-104, 188], [-196, -104], [-191, -104], [-193, -104], [184, -192], [-184, 192],
     [184, -193], [-184, 193], [184, -200], [-184, 200], [184, -203], [-184, 203], [34, 184], [-34, -184], [12, -190],
     [-12, 190], [12, -191], [-12, 191], [189, -196], [-189, 196], [189, -197], [-189, 197], [-271, -422], [195, -422],
     [271, -423], [-195, -423], [-423, 189], [-422, 189], [42, -80], [-42, 80], [42, -81], [-42, 81], [42, -84],
     [-42, 84], [42, -101], [-42, 101], [42, -112], [-42, 112], [42, -166], [-42, 166], [42, -195], [-42, 195],
     [42, -218], [-42, 218], [42, -241], [-42, 241], [42, -259], [-42, 259], [42, -291], [-42, 291], [42, -303],
     [-42, 303], [42, -313], [-42, 313], [42, -323], [-42, 323], [42, -344], [-42, 344], [42, -349], [-42, 349],
     [42, -357], [-42, 357], [42, -385], [-42, 385], [42, -404], [-42, 404], [286, 42], [267, 42], [43, 42], [278, 42],
     [347, 278], [-347, -278], [279, -347], [-279, 347], [279, -348], [-279, 348], [-369, -279], [-370, -279],
     [281, -284], [-281, 284], [281, -285], [-281, 285], [281, -301], [-281, 301], [281, -370], [-281, 370], [26, 281],
     [-26, -281], [7, -368], [-7, 368], [7, -369], [-7, 369], [-110, -43], [-46, -43], [41, -45], [-41, 45], [41, -46],
     [-41, 46], [-219, -41], [-211, -41], [204, -211], [-204, 211], [204, -212], [-204, 212], [214, 204], [-214, -204],
     [32, -214], [-32, 214], [32, -215], [-32, 215], [32, -228], [-32, 228], [5, -219], [-5, 219], [5, -220], [-5, 220],
     [44, -110], [-44, 110], [44, -111], [-44, 111], [-358, -44], [-355, -44], [350, -353], [-350, 353], [350, -354],
     [-350, 354], [350, -355], [-350, 355], [350, -367], [-350, 367], [9, 350], [-9, -350], [21, -358], [-21, 358],
     [21, -359], [-21, 359], [-270, -267], [-268, -267], [-272, -267], [194, -271], [-194, 271], [194, -272],
     [-194, 272], [-202, -194], [-203, -194], [25, -201], [-25, 201], [25, -202], [-25, 202], [331, 268], [324, 268],
     [332, 268], [402, 332], [-402, -332], [391, -402], [-391, 402], [391, -403], [-391, 403], [-400, -391],
     [-401, -391], [392, -397], [-392, 397], [392, -398], [-392, 398], [392, -401], [-392, 401], [392, -409],
     [-392, 409], [19, 392], [-19, -392], [17, -399], [-17, 399], [17, -400], [-17, 400], [326, 324], [-326, -324],
     [322, -325], [-322, 325], [322, -326], [-322, 326], [-389, -322], [-390, -322], [235, -386], [-235, 386],
     [235, -387], [-235, 387], [235, -390], [-235, 390], [383, 235], [-383, -235], [35, -382], [-35, 382], [35, -383],
     [-35, 383], [30, -388], [-30, 388], [30, -389], [-30, 389], [334, 331], [-334, -331], [83, -333], [-83, 333],
     [83, -334], [-83, 334], [-320, -83], [-321, -83], [86, -91], [-86, 91], [86, -92], [-86, 92], [86, -158],
     [-86, 158], [86, -321], [-86, 321], [28, 86], [-28, -86], [4, -317], [-4, 317], [4, -320], [-4, 320], [237, -269],
     [-237, 269], [237, -270], [-237, 270], [-242, -237], [-239, -237], [232, -238], [-232, 238], [232, -239],
     [-232, 239], [253, 232], [-253, -232], [6, -253], [-6, 253], [6, -254], [-6, 254], [6, -258], [-6, 258],
     [10, -242], [-10, 242], [10, -243], [-10, 243], [289, 286], [-289, -286], [287, -289], [-287, 289], [287, -290],
     [-287, 290], [-372, -287], [-373, -287], [292, -295], [-292, 295], [292, -296], [-292, 296], [292, -311],
     [-292, 311], [292, -373], [-292, 373], [27, 292], [-27, -292], [11, -371], [-11, 371], [11, -372], [-11, 372],
     [-180, -176], [-328, -176], [-276, -176], [178, -276], [-178, 276], [178, -277], [-178, 277], [178, -342],
     [-178, 342], [-405, -178], [-396, -178], [-398, -178], [18, -395], [-18, 395], [18, -396], [-18, 396], [394, -405],
     [-394, 405], [394, -406], [-394, 406], [-403, -410], [404, -410], [403, -411], [-404, -411], [-411, 394],
     [-410, 394], [177, -328], [-177, 328], [177, -329], [-177, 329], [-337, -177], [-376, -177], [-386, -177],
     [22, -376], [-22, 376], [22, -377], [-22, 377], [234, -337], [-234, 337], [234, -338], [-234, 338], [-325, -416],
     [323, -416], [325, -417], [-323, -417], [-417, 234], [-416, 234], [85, -179], [-85, 179], [85, -180], [-85, 180],
     [-89, -85], [-172, -85], [-91, -85], [23, -172], [-23, 172], [23, -173], [-23, 173], [82, -89], [-82, 89],
     [82, -90], [-82, 90], [-333, -428], [84, -428], [333, -429], [-84, -429], [-429, 82], [-428, 82], [181, -263],
     [-181, 263], [181, -264], [-181, 264], [248, 181], [-248, -181], [233, -248], [-233, 248], [233, -249],
     [-233, 249], [-261, -233], [-245, -233], [-238, -233], [33, -245], [-33, 245], [33, -246], [-33, 246], [236, -261],
     [-236, 261], [236, -262], [-236, 262], [-269, -420], [259, -420], [269, -421], [-259, -421], [-421, 236],
     [-420, 236], [-65, -60], [-122, -60], [-117, -60], [-127, -60], [63, -127], [-63, 127], [63, -128], [-63, 128],
     [63, -206], [-63, 206], [-210, -63], [-222, -63], [-212, -63], [29, -222], [-29, 222], [29, -223], [-29, 223],
     [40, -209], [-40, 209], [40, -210], [-40, 210], [-45, -430], [80, -430], [45, -431], [-80, -431], [-431, 40],
     [-430, 40], [62, -117], [-62, 117], [62, -118], [-62, 118], [62, -120], [-62, 120], [-283, -62], [-305, -62],
     [-285, -62], [31, -305], [-31, 305], [31, -306], [-31, 306], [280, -282], [-280, 282], [280, -283], [-280, 283],
     [-348, -412], [349, -412], [348, -413], [-349, -413], [-413, 280], [-412, 280], [61, -122], [-61, 122], [61, -123],
     [-61, 123], [-351, -61], [-361, -61], [-353, -61], [20, -361], [-20, 361], [20, -362], [-20, 362], [109, -351],
     [-109, 351], [109, -352], [-109, 352], [-111, -424], [112, -424], [111, -425], [-112, -425], [-425, 109],
     [-424, 109], [52, -64], [-52, 64], [52, -65], [-52, 65], [-293, -52], [-315, -52], [-295, -52], [288, -293],
     [-288, 293], [288, -294], [-288, 294], [-290, -418], [291, -418], [290, -419], [-291, -419], [-419, 288],
     [-418, 288], [2, -309], [-2, 309], [2, -310], [-2, 310], [58, -185], [-58, 185], [58, -186], [-58, 186],
     [58, -231], [-58, 231], [58, -298], [-58, 298], [58, -308], [-58, 308], [58, -364], [-58, 364], [58, -375],
     [-58, 375], [58, -393], [-58, 393], [49, 58], [59, 58], [54, 58], [-57, -54], [-209, -57], [-208, -57], [226, 208],
     [215, 208], [213, -226], [-213, 226], [213, -227], [-213, 227], [14, 213], [-14, -213], [126, 125], [-126, -125],
     [-128, -126], [-129, -126], [206, 205], [207, 205], [-352, -56], [-365, -56], [-354, -56], [8, -365], [-8, 365],
     [8, -366], [-8, 366], [-95, -59], [-87, -59], [-96, -59], [336, 96], [346, 336], [-406, -346], [-408, -346],
     [-409, -346], [3, -407], [-3, 407], [3, -408], [-3, 408], [-342, -341], [-343, -341], [-274, -273], [-275, -273],
     [78, -265], [-78, 265], [78, -266], [-78, 266], [78, -275], [-78, 275], [98, 78], [-98, -78], [277, 274],
     [-277, -274], [379, 335], [382, 335], [381, 379], [-381, -379], [1, -380], [-1, 380], [1, -381], [-1, 381],
     [-329, -414], [330, -414], [329, -415], [-330, -415], [-415, 327], [-414, 327], [-88, -87], [-90, -87],
     [-156, -87], [-92, -87], [16, -156], [-16, 156], [16, -157], [-16, 157], [-179, -426], [94, -426], [179, -427],
     [-94, -427], [-427, 88], [-426, 88], [106, 95], [-106, -95], [-108, -106], [-262, -108], [-255, -108], [257, 255],
     [258, 255], [251, -256], [-251, 256], [251, -257], [-251, 257], [13, 251], [-13, -251], [264, 260], [266, 260],
     [249, 247], [250, 247], [-197, -107], [-199, -107], [-200, -107], [36, -198], [-36, 198], [36, -199], [-36, 199],
     [-47, -49], [48, 47], [-48, -47], [115, 48], [-282, -115], [-299, -115], [-284, -115], [24, -299], [-24, 299],
     [24, -300], [-24, 300], [-120, -114], [-121, -114], [116, 113], [-116, -113], [118, 116], [119, 116], [-294, -51],
     [-309, -51], [-296, -51], [229, 74], [230, 74], [66, -132], [-66, 132], [66, -133], [-66, 133], [66, -135],
     [-66, 135], [66, -230], [-66, 230], [216, 66], [-216, -66], [-356, -216], [363, 356], [-363, -356], [-367, -363],
     [131, -136], [-131, 136], [131, -137], [-131, 137], [131, -140], [-131, 140], [131, -148], [-131, 148],
     [131, -229], [-131, 229], [302, 131], [297, 131], [-301, -297], [146, 71], [141, 71], [149, 71], [-142, 72],
     [-142, 149], [-142, 146], [146, 73], [143, 73], [149, 73], [144, -149], [-144, 149], [144, -150], [-144, 150],
     [152, 144], [-152, -144], [134, -151], [-134, 151], [134, -152], [-134, 152], [-240, -134], [254, 240], [97, -224],
     [-97, 224], [97, -225], [-97, 225], [97, -252], [-97, 252], [231, 97], [-231, -97], [-163, -141], [-160, 142],
     [-160, 153], [-154, -163], [-160, -163], [-163, -143], [99, -162], [-99, 162], [99, -163], [-99, 163], [-100, -99],
     [183, 100], [-183, -100], [-192, -183], [-158, -153], [-318, 160], [-174, 169], [-170, 173], [-318, 166],
     [130, -145], [-130, 145], [130, -146], [-130, 146], [228, 130], [217, 130], [70, -76], [-70, 76], [70, -77],
     [-70, 77], [-339, -70], [340, 339], [-340, -339], [-397, -340], [-384, -79], [-387, -79], [374, 384], [-374, -384],
     [-432, 435], [-435, 432], [433, 39, -37], [434, -39, 37], [-432, 434, 433], [37, 79, 67], [-38, 37, 39],
     [-38, -37, -39], [39, 79, 69], [-68, 67, 69], [-68, -67, -69], [-310, -308, -75], [-371, -313, -312],
     [-316, -314, -312], [314, 313, 312], [316, 313, 312], [314, 371, 312], [316, 371, 312], [422, 271, -195],
     [423, -271, 195], [-189, 423, 422], [279, 369, 370], [43, 110, 46], [41, 219, 211], [44, 358, 355],
     [194, 202, 203], [391, 400, 401], [322, 389, 390], [83, 320, 321], [237, 242, 239], [287, 372, 373],
     [410, 403, -404], [411, -403, 404], [-394, 411, 410], [416, 325, -323], [417, -325, 323], [-234, 417, 416],
     [428, 333, -84], [429, -333, 84], [-82, 429, 428], [420, 269, -259], [421, -269, 259], [-236, 421, 420],
     [430, 45, -80], [431, -45, 80], [-40, 431, 430], [412, 348, -349], [413, -348, 349], [-280, 413, 412],
     [424, 111, -112], [425, -111, 112], [-109, 425, 424], [418, 290, -291], [419, -290, 291], [-288, 419, 418],
     [-56, -55, -54], [57, 55, 54], [57, 56, 54], [-125, -205, -57], [-208, -226, -215], [126, 128, 129],
     [-205, -206, -207], [124, 123, 55], [-124, -123, 55], [-124, 123, -55], [124, -123, -55], [-336, -327, -96],
     [-336, -338, -96], [-336, -335, -96], [341, 273, 336], [-346, -273, -336], [-346, -341, -336], [341, 342, 343],
     [273, 274, 275], [-335, -379, -382], [414, 329, -330], [415, -329, 330], [-327, 415, 414], [426, 179, -94],
     [427, -179, 94], [-88, 427, 426], [-107, -103, -106], [108, 103, 106], [108, 107, 106], [-260, -247, -108],
     [-255, -257, -258], [-260, -264, -266], [-247, -249, -250], [105, 187, 103], [-105, -187, 103], [-105, 187, -103],
     [105, -187, -103], [-51, -50, -49], [47, 50, 49], [47, 51, 49], [114, 113, 48], [-115, -113, -48],
     [-115, -114, -48], [114, 120, 121], [-116, -118, -119], [93, 64, 50], [-93, -64, 50], [-93, 64, -50],
     [93, -64, -50], [-74, -229, -230], [-359, -357, -216], [-362, -360, -216], [-366, -364, -363], [367, 364, 363],
     [367, 366, 363], [-131, -302, -297], [-300, -298, -297], [301, 298, 297], [301, 300, 297], [-368, -303, -302],
     [-306, -304, -302], [304, 303, 302], [306, 303, 302], [304, 368, 302], [306, 368, 302], [-72, 71, 73],
     [-72, -71, -73], [-243, -241, -134], [-246, -244, -134], [256, 252, 240], [-254, -252, -240], [-254, -256, -240],
     [-153, -159, -141], [163, 159, 141], [163, 153, 141], [-154, -155, 161], [-154, -153, 159], [-154, 159, 161],
     [-142, 141, 143], [-142, -141, -143], [-153, -161, -143], [163, 161, 143], [163, 153, 143], [-201, -101, -99],
     [-190, -102, -99], [-198, -186, -183], [192, 186, 183], [192, 198, 183], [-157, -185, -153], [158, 185, 153],
     [158, 157, 153], [-317, -166, -159], [-173, -169, -159], [169, 166, 159], [173, 166, 159], [169, 317, 159],
     [173, 317, 159], [-167, -168, 319], [-167, -166, 317], [-167, 317, 319], [-318, -173, -169], [-167, -173, -169],
     [-160, 159, 161], [-160, -159, -161], [-319, -166, -161], [-173, -169, -161], [169, 166, 161], [173, 166, 161],
     [169, 319, 161], [173, 319, 161], [227, 225, 130], [-220, -218, -217], [-223, -221, -217], [221, 218, 217],
     [223, 218, 217], [221, 220, 217], [223, 220, 217], [-399, -344, -70], [-395, -345, -70], [-407, -393, -340],
     [397, 393, 340], [397, 407, 340], [-385, -388, -79], [-375, -380, -374], [-378, -377, -374], [377, 380, 374],
     [378, 380, 374], [377, 375, 374], [378, 375, 374], [307, 311, 308, 75], [307, 311, 310, 75], [104, 196, 191, 193],
     [267, 270, 268, 272], [-268, -331, -324, -332], [176, 180, 328, 276], [178, 405, 396, 398], [177, 337, 376, 386],
     [85, 89, 172, 91], [233, 261, 245, 238], [63, 210, 222, 212], [62, 283, 305, 285], [61, 351, 361, 353],
     [52, 293, 315, 295], [-58, -49, -59, -54], [208, 209, 205, 57], [208, 209, 125, 57], [56, 352, 365, 354],
     [59, 95, 87, 96], [335, 338, 327, 96], [346, 406, 408, 409], [255, 262, 247, 108], [255, 262, 260, 108],
     [107, 197, 199, 200], [115, 282, 299, 284], [51, 294, 309, 296], [356, 360, 357, 216], [356, 362, 357, 216],
     [356, 360, 359, 216], [356, 362, 359, 216], [-71, -146, -141, -149], [-73, -146, -143, -149], [240, 244, 241, 134],
     [240, 246, 241, 134], [240, 244, 243, 134], [240, 246, 243, 134], [-164, -153, -165, -159],
     [-164, -153, -163, -161], [-164, -153, -159, -161], [100, 102, 101, 99], [100, 190, 101, 99], [100, 102, 201, 99],
     [100, 190, 201, 99], [-174, -166, -175, -317], [-174, -166, -173, -319], [-174, -166, -317, -319],
     [-170, -166, -171, -317], [-170, -166, -169, -319], [-170, -166, -317, -319], [-217, -228, -225, -130],
     [-217, -228, -227, -130], [339, 345, 344, 70], [339, 395, 344, 70], [339, 345, 399, 70], [339, 395, 399, 70],
     [387, 384, 388, 79], [387, 384, 385, 79], [67, 76, 71, 74, 138], [69, 76, 73, 74, 138],
     [-53, -60, -263, -176, -182], [-42, -286, -267, -43, -278], [60, 65, 122, 117, 127], [87, 88, 90, 156, 92]]

l = sat()

l.generate_problem(1000, 100)


# print(l.generate_problem(100, 50))
# print(l.maxi)
x = l.gsat(1, 1)
# print(x)
s = l.parser("bench.cnf")
print(sum(l.interpreter(x)))
print(s)
# print(i)


