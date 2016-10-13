import re


class Subcatchment:
    def __init__(self, items):
        if len(items) < 9:
            items.append("")
        self.Name = items[0]
        self.Rain_Gage = items[1]
        self.Outlet = items[2]
        self.Area = items[3]
        self.Imperv = items[4]
        self.Width = items[5]
        self.Slope = items[6]
        self.CurbLen = items[7]
        self.SnowPack = items[8]

    def get_all(self):
        return self.Name, self.Rain_Gage, self.Outlet, self.Area, self.Imperv, self.Width, \
                self.Slope, self.CurbLen, self.SnowPack


class SubArea:
    def __init__(self, items):
        if len(items) < 8:
            items.append("")
        self.Subcatchment = items[0]
        self.N_Imperv = items[1]
        self.N_Perv = items[2]
        self.S_Imperv = items[3]
        self.S_Perv = items[4]
        self.PctZero = items[5]
        self.RouteTo = items[6]
        self.PctRouted = items[7]

    def get_all(self):
        return self.Subcatchment, self.N_Imperv, self.N_Perv, self.S_Imperv, self.S_Perv, \
                self.PctZero, self.RouteTo, self.PctZero


class Infiltration:
    def __init__(self, items):
        if len(items) < 4:
            items.append("")
        self.Subcatchment = items[0]
        self.Suction = items[1]
        self.Ksat = items[2]
        self.IMD = items[3]

    def get_all(self):
        return self.Subcatchment, self.Suction, self.Ksat, self.IMD


class LIDControls:
    def __init__(self, items):
        if len(items) < 3:
            items.append("")
        self.Name = items[0]
        self.Type_Layer = items[1]

        self.Parameters = self.lid_items(self.Name, self.Type_Layer, items[2:])

    def get_all(self):
        return self.Name, self.Type_Layer, self.Parameters

    def lid_items(self, name, type, items):
        if name == "GreenRoof":
            if type == "SURFACE":
                self.surface_pars = {'Berm_height': items[0]}
                self.surface_pars['Vegetation_Volume'] = items[1]
                self.surface_pars['Surface_Roughness'] = items[2]
                self.surface_pars['Surface_Slope'] = items[3]
                return self.surface_pars

            if type == "SOIL":
                self.soil_pars = {'Thickness': items[0]}
                self.soil_pars['Porosity'] = items[1]
                self.soil_pars['Field_Capacity'] = items[2]
                self.soil_pars['Wilting_Point'] = items[3]
                self.soil_pars['Conductivity'] = items[4]
                self.soil_pars['Conductivity_Slope'] = items[5]
                self.soil_pars['Suction_Head'] = items[6]
                return self.soil_pars

            if type == "DRAINMAT":
                self.drain_mat_pars = {'Thickness': items[0]}
                self.drain_mat_pars['Void_Fraction'] = items[1]
                self.drain_mat_pars['Roughness'] = items[2]
                return self.drain_mat_pars




class LIDUsage:
    def __init__(self, items):
        if len(items) < 10:
            items.append("")
        self.Subcatchment = items[0]
        self.LID_Process = items[1]
        self.Number = items[2]
        self.Area = items[3]
        self.Width = items[4]
        self.InitSat = items[5]
        self.FromImp = items[6]
        self.ToPerv = items[7]
        self.RptFile = items[8]
        self.DrainTo = items[9]

    def get_all(self):
        return self.Subcatchment, self.LID_Process, self.Number, self.Area, \
                self.Width, self.InitSat, self.FromImp, self.ToPerv, self.RptFile, self.DrainTo


class InputData:

    def __init__(self):
        pass

    def parse_input_data(self, inp_file):
        with open(inp_file, 'r') as inp_file:
            #all_inp_data = inp_file.read()

            #sections = all_inp_data.index("[SUBCATCHMENTS]")#re.findall(r'\[SUBCATCHMENTS\]', all_inp_data)
            #print all_inp_data[1244 + len("[SUBCATCHMENTS]")]

            lines = inp_file.readlines()
            print lines
            print "\n after"
            for line_num in range(len(lines)):
                if lines[line_num] == "[SUBCATCHMENTS]\n":
                    items = self.read_section_data(lines, line_num)
                    self.subcathments = []
                    for item in items:
                        if item != "":
                            self.subcathments.append(Subcatchment(item.split()))
                    for s in self.subcathments:
                        print s.get_all()


                if lines[line_num] == "[SUBAREAS]\n":
                    items = self.read_section_data(lines, line_num)
                    self.sub_areas = []
                    for item in items:
                        if item != "":
                            self.sub_areas.append(SubArea(item.split()))

                    for s in self.sub_areas:
                        print s.get_all()


                if lines[line_num] == "[INFILTRATION]\n":
                    items = self.read_section_data(lines, line_num)
                    self.inflitrations = []
                    for item in items:
                        if item != "":
                            self.inflitrations.append(Infiltration(item.split()))

                    for s in self.inflitrations:
                        print s.get_all()

                if lines[line_num] == "[LID_CONTROLS]\n":
                    items = self.read_section_data(lines, line_num)
                    self.lid_controls = []
                    for item in items:
                        if item != "" and len(item.split()) > 2:

                            self.lid_controls.append(LIDControls(item.split()))

                    for s in self.lid_controls:
                        print s.get_all()

                if lines[line_num] == "[LID_USAGE]\n":
                    items = self.read_section_data(lines, line_num)
                    self.lid_usages = []
                    for item in items:
                        if item != "":
                            self.lid_usages.append(LIDUsage(item.split()))

                    for s in self.lid_usages:
                        print s.get_all()

    def read_section_data(self, lines, line_num):
        data = ""

        while not (lines[line_num + 1].startswith("[")):
            data += lines[line_num]

            line_num += 1
        #print data

        #print data.split("\n")
        items = []
        for item in data.split("\n"):

            if not (item.startswith("[") or item.startswith(";")):
                items.append(item)
                #print item
        #print items
        return items


#parse_input_data("UMD0111.inp")
