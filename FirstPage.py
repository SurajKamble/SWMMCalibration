import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui
from InputParams import InputData


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        newAction = QtGui.QAction(QtGui.QIcon('exit.png'), '&New', self)
        newAction.setShortcut('Ctrl+Q')
        newAction.setStatusTip('Browse new file')
        newAction.triggered.connect(self.new_btn_click)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAction)


        self.setGeometry(100, 100, 950, 900)
        self.setWindowTitle('Calibration of SWMM models')
        self.show()

    def new_btn_click(self):

        self.inp_fname = QtGui.QFileDialog.getOpenFileName(self, 'SWMM Input file',
                '/home')

        inp_data = InputData()
        inp_data.parse_input_data(self.inp_fname)
        print "In GUI"
        print inp_data.subcathments[0].Name
        self.t = tabdemo(inp_data.subcathments, inp_data.sub_areas, inp_data.inflitrations,
                    inp_data.lid_controls, inp_data.lid_usages)
        self.setCentralWidget(self.t)


class tabdemo(QTabWidget):

    def __init__(self, subcatchments, sub_areas, infiltrations, lid_controls, lid_usage,
                 parent=None):

        print "In tabs"
        print subcatchments[0].Name
        super(tabdemo, self).__init__(parent)


        self.Subcatchments = QWidget()
        self.SubAreas = QWidget()
        self.Infiltration = QWidget()
        self.LID_Controls = QWidget()
        self.LID_Usage = QWidget()

        self.addTab(self.Subcatchments, "Tab 1")
        self.addTab(self.SubAreas, "Tab 2")
        self.addTab(self.Infiltration, "Tab 3")
        self.addTab(self.LID_Controls, "Tab 4")
        self.addTab(self.LID_Usage, "Tab 5")

        self.SubcatchmentsUI(subcatchments)
        self.SubAreasUI(sub_areas)
        self.InfiltrationUI(infiltrations)
        self.LID_ControlsUI(lid_controls)
        self.LID_UsageUI(lid_usage)


    def SubcatchmentsUI(self, subcatchments):

        layout = QFormLayout()
        '''

        #for sub in subcatchments:
        print subcatchments[0].Name
        print subcatchments[0].Rain_Gage
        '''

        '''
        for sub in subcatchments:
            names.append(QLineEdit(self))

            rain_gages.append(QLineEdit(self))

            outlets.append(QLineEdit(self))
            areas.append(QLineEdit(self))
            impervs.append(QLineEdit(self))
            widths.append(QLineEdit(self))
            slopes.append(QLineEdit(self))
            curb_lens.append(QLineEdit(self))
            snow_packs.append(QLineEdit(self))

        for name in names:
            name.setText(subcatchments[0].Name)
            layout.addRow("Name", name)
        for rain_gage in rain_gages:
            rain_gage.setText()
            layout.addRow("Rain_Gage", rain_gage)
        layout.addRow("Outlet", )
        layout.addRow("", )
        layout.addRow("", )
        layout.addRow("", )
        layout.addRow("", )
        layout.addRow("", )
        layout.addRow("", )
        '''

        for sub in subcatchments:
            name = QLineEdit(self)
            name.setText(sub.Name)
            layout.addRow("Name", name)

            rain_gage = QLineEdit(self)
            rain_gage.setText(sub.Rain_Gage)
            layout.addRow("Rain_Gage", rain_gage)

            outlet = QLineEdit(self)
            outlet.setText(sub.Outlet)
            layout.addRow("Outlet", outlet)

            area = QLineEdit(self)
            area.setText(sub.Area)
            layout.addRow("Area", area)

            imperv = QLineEdit(self)
            imperv.setText(sub.Imperv)
            layout.addRow("%Imperv", imperv)

            width = QLineEdit(self)
            width.setText(sub.Width)
            layout.addRow("Width", width)

            slope = QLineEdit(self)
            slope.setText(sub.Slope)
            layout.addRow("Slope", slope)

            curb_len = QLineEdit(self)
            curb_len.setText(sub.CurbLen)
            layout.addRow("CurbLen", curb_len)

            snow_pack = QLineEdit(self)
            snow_pack.setText(sub.SnowPack)
            layout.addRow("SnowPack", snow_pack)

            sep = QLabel("\n" + "- " * 120 + "\n", self)
            layout.addRow(sep)

        self.setTabText(0, "Subcatchments")
        self.Subcatchments.setLayout(layout)


    def SubAreasUI(self, sub_areas):
        layout = QFormLayout()


        for sub in sub_areas:
            subcatchment = QLineEdit(self)
            subcatchment.setText(sub.Subcatchment)
            layout.addRow("Subcatchment", subcatchment)

            n_imperv = QLineEdit(self)
            n_imperv.setText(sub.N_Imperv)
            layout.addRow("N-Imperv", n_imperv)

            n_perv = QLineEdit(self)
            n_perv.setText(sub.N_Perv)
            layout.addRow("N-Perv", n_perv)

            s_imperv = QLineEdit(self)
            s_imperv.setText(sub.S_Imperv)
            layout.addRow("S-Perv", s_imperv)

            s_perv = QLineEdit(self)
            s_perv.setText(sub.S_Perv)
            layout.addRow("S-Perv", s_perv)

            pct_zero = QLineEdit(self)
            pct_zero.setText(sub.PctZero)
            layout.addRow("PctZero", pct_zero)

            route_to = QLineEdit(self)
            route_to.setText(sub.RouteTo)
            layout.addRow("RouteTo", route_to)

            pct_routed = QLineEdit(self)
            pct_routed.setText(sub.PctRouted)
            layout.addRow("PctRouted", pct_routed)

            sep = QLabel("\n" + "- " * 120 + "\n", self)
            layout.addRow(sep)

        self.setTabText(1, "SubAreas")
        self.SubAreas.setLayout(layout)


    def InfiltrationUI(self, infiltrations):
        layout = QFormLayout()

        for inf in infiltrations:
            subcatchment = QLineEdit(self)
            subcatchment.setText(inf.Subcatchment)
            layout.addRow("Subcatchment", subcatchment)

            suction = QLineEdit(self)
            suction.setText(inf.Suction)
            layout.addRow("Suction", suction)

            ksat = QLineEdit(self)
            ksat.setText(inf.Ksat)
            layout.addRow("Ksat", ksat)

            imd = QLineEdit(self)
            imd.setText(inf.IMD)
            layout.addRow("IMD", imd)

            sep = QLabel("\n" + "- " * 120 + "\n", self)
            layout.addRow(sep)

        self.setTabText(2, "Infiltration")
        self.Infiltration.setLayout(layout)


    def LID_ControlsUI(self, lid_controls):
        layout = QFormLayout()

        for lid in lid_controls:
            name = QLineEdit(self)
            name.setText(lid.Name)
            layout.addRow("Name", name)

            type_layer = QLineEdit(self)
            type_layer.setText(lid.Type_Layer)
            layout.addRow("Type/Layer", type_layer)

            for par in lid.Parameters.keys():

                parameter = QLineEdit(self)
                parameter.setText(lid.Parameters[par])
                layout.addRow(par, parameter)

            sep = QLabel("\n" + "- " * 120 + "\n", self)
            layout.addRow(sep)

        self.setTabText(3, "LID_Controls")
        self.LID_Controls.setLayout(layout)


    def LID_UsageUI(self, lid_usage):
        layout = QFormLayout()

        for lid in lid_usage:
            subcatchment = QLineEdit(self)
            subcatchment.setText(lid.Subcatchment)
            layout.addRow("Subcatchment", subcatchment)

            lid_process = QLineEdit(self)
            lid_process.setText(lid.LID_Process)
            layout.addRow("LID Process", lid_process)

            number = QLineEdit(self)
            number.setText(lid.Number)
            layout.addRow("Number", number)

            area = QLineEdit(self)
            area.setText(lid.Area)
            layout.addRow("Area", area)

            width = QLineEdit(self)
            width.setText(lid.Width)
            layout.addRow("Width", width)

            initsat = QLineEdit(self)
            initsat.setText(lid.InitSat)
            layout.addRow("InitSat", initsat)

            fromimp = QLineEdit(self)
            fromimp.setText(lid.FromImp)
            layout.addRow("FromImp", fromimp)

            toperv = QLineEdit(self)
            toperv.setText(lid.ToPerv)
            layout.addRow("ToPerv", toperv)

            rptfile = QLineEdit(self)
            rptfile.setText(lid.RptFile)
            layout.addRow("RptFile", rptfile)

            drainto = QLineEdit(self)
            drainto.setText(lid.DrainTo)
            layout.addRow("DrainTo", drainto)

            sep = QLabel("\n" + "- " * 120 + "\n", self)
            layout.addRow(sep)

        self.setTabText(4, "LID_Usage")
        self.LID_Usage.setLayout(layout)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()