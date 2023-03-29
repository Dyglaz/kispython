    # def generate_groups(groups, year):
    #     res = {}
    #     for spec, num in groups.items():
    #         res[spec] = ([f'{spec}-{i:02}-{year}' for i in range(1, num+1)])
    #     return res
    #
    #
    # def gen_view(groups_dict):
    #     for spec, groups in groups_dict.items():
    #         print(spec)
    #         for i in range(len(groups) // 10 + 1):
    #             print(*groups[i * 10:(i + 1) * 10])
    #             print()
    #
    #
    # groups = {'ИВБО': 8, 'ИКБО': 33, 'ИМБО': 2, 'ИНБО': 13}
    # year = 21
    # groups_d = generate_groups(groups, year)
    # gen_view(groups_d)







        #
#

# import sys
#
# def my_print(*objects , sep=' ', end='\n', file=sys.stdout, flush=False):
#     output = sep.join(map(str, objects))
#     output += end
#     file.write(output)
#     if flush:
#         file.flush()
#
# my_print('Hello', 'world', sep='\n', end='!', flush=True)
#
# from ctypes import *
#
# def decrypt(v, k):
#     v0, v1 = c_uint32(v[0]), c_uint32(v[1])
#     sum = 0xC6EF3720
#     delta = 0x9e3779b9
#     k0, k1, k2, k3 = k[0], k[1], k[2], k[3]
#
#     for i in range(32):
#         v1.value -= ((v0.value << 4) + k2) ^ (v0.value + sum) ^ ((v0.value >> 5) + k3)
#         v0.value -= ((v1.value << 4) + k0) ^ (v1.value + sum) ^ ((v1.value >> 5) + k1)
#         sum -= delta
#
#     return v0.value, v1.value
#
# key = [0x0, 0x4, 0x5, 0x1]
#
# encrypted_message = [
#     0xE3238557, 0x6204A1F8, 0xE6537611, 0x174E5747,
#     0x5D954DA8, 0x8C2DFE97, 0x2911CB4C, 0x2CB7C66B,
#     0xE7F185A0, 0xC7E3FA40, 0x42419867, 0x374044DF,
#     0x2519F07D, 0x5A0C24D4, 0xF4A960C5, 0x31159418,
#     0xF2768EC7, 0xAEAF14CF, 0x071B2C95, 0xC9F22699,
#     0xFFB06F41, 0x2AC90051, 0xA53F035D, 0x830601A7,
#     0xEB475702, 0x183BAA6F, 0x12626744, 0x9B75A72F,
#     0x8DBFBFEC, 0x73C1A46E, 0xFFB06F41, 0x2AC90051,
#     0x97C5E4E9, 0xB1C26A21, 0xDD4A3463, 0x6B71162F,
#     0x8C075668, 0x7975D565, 0x6D95A700, 0x7272E637
# ]
#
# for i in range(0, len(encrypted_message), 2):
#     encrypted_message[i:i+2] = decrypt(encrypted_message[i:i+2], key)
#
#
# for i in encrypted_message:
#     print(chr(i), end='')

# def main(inp):
#     table = []
#     for i in inp:
#         if i not in table:
#             table.append(i)
#     res = []
#     for i in range(len(table)):
#         line = table[i]
#         mail = line[0].split('[at]')[1]
#         num, date = line[1].split('#')
#         num = num.split()[1].replace('-', '')
#         date = date.replace('-', '.')
#         date = date[:-4] + date[-2:]
#         res.append([mail, num, date, line[2].split()[0]])
#     return res
#
# print(main([('gusak68[at]mail.ru', '630 082-0115#20-10-2002', 'Гушак В.Ч.', 'gusak68[at]mail.ru'),
#             ('tolizli68[at]mail.ru', '582 287-5807#25-04-2003', 'Толизли К.Г.', 'tolizli68[at]mail.ru'),
#             ('benic93[at]yahoo.com', '748 017-3777#18-06-2001', 'Бенич И.О.', 'benic93[at]yahoo.com'),
#             ('lulanz92[at]mail.ru', '387 959-0489#10-04-2002', 'Лулянц Г.Ш.', 'lulanz92[at]mail.ru'),
#             ('lulanz92[at]mail.ru', '387 959-0489#10-04-2002', 'Лулянц Г.Ш.', 'lulanz92[at]mail.ru')]))
#


# class StateMachine:
#     def __init__(self):
#         self.state = "A"
#
#     def sway(self):
#         if self.state == "A":
#             self.state = "B"
#             return 0
#         if self.state == "B":
#             self.state = "C"
#             return 1
#         if self.state == "C":
#             return 4
#         if self.state == "D":
#             self.state = "E"
#             return 5
#         if self.state == "E":
#             self.state = "F"
#             return 6
#         if self.state == "F":
#             self.state = "G"
#             return 8
#         raise MealyError("sway")
#
#     def pull(self):
#         if self.state == "B":
#             self.state = "G"
#             return 2
#         if self.state == "C":
#             self.state = "D"
#             return 3
#         if self.state == "E":
#             self.state = "C"
#             return 7
#         if self.state == "G":
#             self.state = "D"
#             return 9
#         raise MealyError("pull")
#
#
# class MealyError(Exception):
#     pass
#
#
# def main():
#     return StateMachine()
#
#
# def raises(method, error):
#     output = None
#     try:
#         output = method()
#     except Exception as e:
#         assert type(e) == error
#     assert output is None
#
#
# def test():
#     o = main()
#     assert o.sway() == 0
#     assert o.sway() == 1
#     assert o.sway() == 4
#     assert o.pull() == 3
#     assert o.sway() == 5
#     assert o.sway() == 6
#     assert o.sway() == 8
#     assert o.pull() == 9
#     assert o.sway() == 5
#     assert o.pull() == 7
#     o = main()
#     assert o.sway() == 0
#     assert o.pull() == 2
#     o = main()
#     raises(lambda: o.pull(), MealyError)
#     assert o.sway() == 0
#     assert o.pull() == 2
#     raises(lambda: o.sway(), MealyError)


    pairs = "..LEXEGEZACEBISO" \
            "USESARMAINDIREA." \
            "ERATENBERALAVETI" \
            "EDORQUANTEISRION"


    class SeedType:
        def __init__(self, w0, w1, w2):
            self.w0 = w0
            self.w1 = w1
            self.w2 = w2


    class FastSeedType:
        def __init__(self, a, b, c, d):
            self.a = a
            self.b = b
            self.c = c
            self.d = d


    class PlanSys:
        def __init__(self):
            self.x = 0
            self.y = 0
            self.economy = 0
            self.govtype = 0
            self.techlev = 0
            self.population = 0
            self.productivity = 0
            self.radius = 0
            self.goatsoupseed = FastSeedType(0, 0, 0, 0)
            self.name = ""


    def tweakseed(s):
        temp = s.w0 + s.w1 + s.w2
        s.w0 = s.w1
        s.w1 = s.w2
        s.w2 = temp


    def makesystem(s):
        thissys = PlanSys()
        longnameflag = s.w0 & 64

        thissys.x = (s.w1 >> 8) % 2 ** 32
        thissys.y = (s.w0 >> 8) % 2 ** 32

        thissys.govtype = (s.w1 >> 3) & 7

        thissys.economy = (s.w0 >> 8) & 7
        if thissys.govtype <= 1:
            thissys.economy |= 2

        thissys.techlev = ((s.w1 >> 8) & 3) + (thissys.economy ^ 7)
        thissys.techlev += thissys.govtype >> 1
        if thissys.govtype & 1 == 1:
            thissys.techlev += 1

        thissys.population = 4 * thissys.techlev + thissys.economy
        thissys.population += thissys.govtype + 1

        thissys.productivity = (thissys.economy ^ 7 + 3) * (thissys.govtype + 4)
        thissys.productivity *= thissys.population * 8

        thissys.radius = 256 * (((s.w2 >> 8) & 15) + 11) + thissys.x

        thissys.goatsoupseed.a = s.w1 & 0xFF
        thissys.goatsoupseed.b = s.w1 >> 8
        thissys.goatsoupseed.c = s.w2 & 0xFF
        thissys.goatsoupseed.d = s.w2 >> 8

        pair1 = 2 * ((s.w2 >> 8) & 31)
        tweakseed(s)
        pair2 = 2 * ((s.w2 >> 8) & 31)
        tweakseed(s)
        pair3 = 2 * ((s.w2 >> 8) & 31)
        tweakseed(s)
        pair4 = 2 * ((s.w2 >> 8) & 31)
        tweakseed(s)

        thissys.name = pairs[pair1:pair1 + 2] + pairs[pair2:pair2 + 2] + pairs[pair3:pair3 + 2]
        if longnameflag:
            thissys.name += pairs[pair4:pair4 + 2]
        thissys.name = thissys.name.replace(".", "")

        return thissys


    def normalize(values):
        min_value = min(values)
        max_value = max(values)
        normalized_values = [(v - min_value) / (max_value - min_value) for v in values]
        scaled_values = [(v * 256) for v in normalized_values]

        return scaled_values


    seed = SeedType(0x5A4A, 0x0248, 0xB753)
    systems = [makesystem(seed) for i in range(256)]
    xs, ys = zip(*((system.x, system.y) for system in systems))
    xs = normalize(xs)
    ys = normalize(ys)
    names = [system.name for system in systems]

    fig, ax = plt.subplots()
    fig.set_size_inches(32, 16)
    ax.scatter(xs, ys, color='white', s=2)
    ax.set_facecolor("black")

    for i, name in enumerate(names):
        ax.annotate(name, (xs[i], ys[i]),
                    xytext=(xs[i] + 0.05, ys[i] + 0.05),
                    color='lightblue',
                    fontsize=12,
                    fontname='Times New Roman')

    plt.show()
