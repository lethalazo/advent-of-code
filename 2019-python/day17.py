import itertools

class Computer:

    def __init__(self, ic, pause_on_output):
        self.ic = ic.copy()
        self.pause_on_output = pause_on_output
        self.input = []
        self.pos = 0
        self.input_pos = 0
        self.output = []
        self.active = True
        self.rel_base = 0

    def add_input(self, value):
        self.input.append(value)
        return self

    def run(self):
        return self.run0(self.ic)

    def run0(self, ic):

        while self.pos < len(ic):
            # print(ic)
            cmd = str(ic[self.pos]).zfill(5)
            # print(cmd)
            # print(self.pos)
            code = int(cmd[3:5])
            # True - immediate, False - Position
            m1 = int(cmd[2])
            m2 = int(cmd[1])
            m3 = int(cmd[0])
            i1 = -1
            i2 = -1
            i3 = -1
            if self.pos + 1 < len(ic):
                i1 = self.pos + 1 if m1 == 1 else ic[self.pos + 1] + (0 if m1 == 0 else self.rel_base)
            if self.pos + 2 < len(ic):
                i2 = self.pos + 2 if m2 == 1 else ic[self.pos + 2] + (0 if m2 == 0 else self.rel_base)
            if self.pos + 3 < len(ic):
                i3 = self.pos + 3 if m3 == 1 else ic[self.pos + 3] + (0 if m3 == 0 else self.rel_base)

            if code == 99:
                self.active = False
                break

            elif code == 1:
                ic[i3] = ic[i1] + ic[i2]
                self.pos += 4

            elif code == 2:
                ic[i3] = ic[i1] * ic[i2]
                self.pos += 4

            elif code == 3:
                ic[i1] = self.input[self.input_pos]
                self.input_pos += 1
                self.pos += 2

            elif code == 4:
                self.output.append(ic[i1])
                self.pos += 2
                # N.B.: execution is paused on output
                if self.pause_on_output:
                    break

            elif code == 5:
                self.pos = self.pos + 3 if ic[i1] == 0 else ic[i2]

            elif code == 6:
                self.pos = ic[i2] if ic[i1] == 0 else self.pos + 3

            elif code == 7:
                ic[i3] = 1 if ic[i1] < ic[i2] else 0
                self.pos += 4

            elif code == 8:
                ic[i3] = 1 if ic[i1] == ic[i2] else 0
                self.pos += 4

            elif code == 9:
                self.rel_base += ic[i1]
                self.pos += 2

            else:
                raise Exception("Code is not supported")



input0 = "1,330,331,332,109,4356,1101,1182,0,16,1101,1449,0,24,101,0,0,570,1006,570,36,101,0,571,0,1001,570,-1,570,1001,24,1,24,1105,1,18,1008,571,0,571,1001,16,1,16,1008,16,1449,570,1006,570,14,21101,58,0,0,1106,0,786,1006,332,62,99,21102,333,1,1,21101,0,73,0,1106,0,579,1101,0,0,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,1001,574,0,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1106,0,81,21102,340,1,1,1105,1,177,21102,477,1,1,1105,1,177,21102,1,514,1,21102,176,1,0,1106,0,579,99,21102,184,1,0,1105,1,579,4,574,104,10,99,1007,573,22,570,1006,570,165,101,0,572,1182,21102,1,375,1,21101,0,211,0,1106,0,579,21101,1182,11,1,21101,222,0,0,1105,1,979,21102,388,1,1,21102,1,233,0,1106,0,579,21101,1182,22,1,21101,244,0,0,1106,0,979,21102,401,1,1,21102,255,1,0,1106,0,579,21101,1182,33,1,21101,266,0,0,1105,1,979,21101,414,0,1,21101,0,277,0,1106,0,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21102,1,1182,1,21101,0,313,0,1106,0,622,1005,575,327,1101,0,1,575,21101,0,327,0,1105,1,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,36,10,0,109,4,1201,-3,0,587,20101,0,0,-1,22101,1,-3,-3,21102,1,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2106,0,0,109,5,2101,0,-4,629,21001,0,0,-2,22101,1,-4,-4,21101,0,0,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,652,21002,0,1,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21101,0,702,0,1105,1,786,21201,-1,-1,-1,1105,1,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,731,1,0,1105,1,786,1105,1,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21102,756,1,0,1106,0,786,1106,0,774,21202,-1,-11,1,22101,1182,1,1,21101,0,774,0,1106,0,622,21201,-3,1,-3,1105,1,640,109,-5,2105,1,0,109,7,1005,575,802,20102,1,576,-6,21002,577,1,-5,1105,1,814,21102,1,0,-1,21102,1,0,-5,21102,1,0,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,57,-3,22201,-6,-3,-3,22101,1449,-3,-3,2101,0,-3,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21101,1,0,-1,1105,1,924,1205,-2,873,21101,0,35,-4,1106,0,924,2102,1,-3,878,1008,0,1,570,1006,570,916,1001,374,1,374,2101,0,-3,895,1101,0,2,0,2101,0,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20101,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,57,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,51,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1102,1,1,575,21101,0,973,0,1105,1,786,99,109,-7,2105,1,0,109,6,21101,0,0,-4,21102,1,0,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1105,1,1041,21101,-4,0,-2,1105,1,1041,21101,-5,0,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,1202,-2,1,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,1201,-2,0,0,1106,0,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1105,1,989,21102,439,1,1,1106,0,1150,21102,1,477,1,1106,0,1150,21102,1,514,1,21102,1149,1,0,1106,0,579,99,21101,1157,0,0,1106,0,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2102,1,-5,1176,2101,0,-4,0,109,-6,2106,0,0,42,9,48,1,7,1,48,1,7,1,48,1,7,1,48,1,7,1,48,1,7,1,48,1,7,1,48,1,7,1,44,13,44,1,3,1,20,1,29,7,20,1,31,1,24,1,31,1,24,1,31,1,24,1,31,1,24,1,31,1,24,1,31,9,16,1,39,1,10,7,33,9,8,1,39,1,5,1,1,1,8,1,39,1,5,1,1,1,8,1,39,1,5,1,1,1,8,1,39,1,5,12,39,1,7,1,7,12,29,1,7,1,7,1,10,1,29,1,7,1,7,1,10,1,29,11,5,1,10,1,37,1,1,1,5,1,10,1,37,1,1,1,5,1,10,1,37,1,1,1,5,1,10,1,37,9,10,1,39,1,16,11,23,7,26,1,23,1,32,1,13,9,1,1,32,1,13,1,7,1,1,1,32,1,13,1,7,1,1,1,32,1,13,1,7,1,1,1,32,9,5,1,7,1,1,1,40,1,5,1,7,1,1,1,40,1,5,1,3,7,40,1,5,1,3,1,3,1,42,1,1,13,42,1,1,1,3,1,3,1,46,7,3,1,48,1,7,1,48,1,7,1,48,1,7,1,48,1,7,1,48,1,7,1,48,9,18"
input0 = input0.split(",")
input0 = [int(x) for x in input0]
input0 = input0 + [0] * 10000
c = Computer(input0, False)
c.run()
print(c.output)
