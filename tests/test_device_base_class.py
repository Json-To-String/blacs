from labscript_utils.connections import ConnectionTable
from labscript_utils.qtwidgets.dragdroptab import DragDropTabWidget
from blacs.device_base_class import DeviceTab, DeviceWorker
from PyQt5.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
    
)
from PyQt5.QtCore import (
    QTimer,
)
import sys

class MyDAQTab(DeviceTab):
    
    def initialise_GUI(self):
        # Create Digital Output Objects
        do_prop = {}
        for i in range(32):
            do_prop['port0/line%d'%i] = {}
        self.create_digital_outputs(do_prop)
            
        # Create Analog Output objects
        ao_prop = {}
        for i in range(4):
            ao_prop['ao%d'%i] = {'base_unit':'V',
                                    'min':-10.0,
                                    'max':10.0,
                                    'step':0.01,
                                    'decimals':3
                                }            
        self.create_analog_outputs(ao_prop)
        
        # Create widgets for output objects
        dds_widgets,ao_widgets,do_widgets = self.auto_create_widgets()
        
        # This function allows you do sort the order of widgets by hardware name.
        # it is pass to the Python 'sorted' function as key=sort when passed in as 
        # the 3rd item of a tuple p(the tuple being an argument of self.auto_place_widgets()
        #
        # This function takes the channel name (hardware name) and returns a string (or whatever) 
        # that when sorted alphabetically, returns the correct order
        def sort(channel):
            port,line = channel.replace('port','').replace('line','').split('/')
            port,line = int(port),int(line)
            return '%02d/%02d'%(port,line)
        
        # and auto place them in the UI
        self.auto_place_widgets(("DDS Outputs",dds_widgets),("Analog Outputs",ao_widgets),("Digital Outputs - Port 0",do_widgets,sort))
        
        # Set the primary worker
        self.create_worker("my_worker_name",DeviceWorker,{})
        self.primary_worker = "my_worker_name"    
        self.create_worker("my_secondary_worker_name",DeviceWorker,{})
        self.add_secondary_worker("my_secondary_worker_name")

        self.supports_remote_value_check(True)

        # Create buttons to test things!
        button1 = QPushButton("Transition to Buffered")
        button1.clicked.connect(lambda: self.transition_to_buffered('',Queue()))
        self.get_tab_layout().addWidget(button1)
        button2 = QPushButton("Transition to Manual")
        button2.clicked.connect(lambda: self.transition_to_manual(Queue()))
        self.get_tab_layout().addWidget(button2)

class MyDummyTab(DeviceTab):
    
    def initialise_GUI(self):
        # Create Digital Output Objects
        do_prop = {}
        for i in range(1):
            do_prop['port0/line%d'] = {}
        self.create_digital_outputs(do_prop)
            
        # Create Analog Output objects
        ao_prop = {}
        for i in range(1):
            ao_prop['ao%d'%i] = {'base_unit':'V',
                                    'min':-10.0,
                                    'max':10.0,
                                    'step':0.01,
                                    'decimals':3
                                }            
        self.create_analog_outputs(ao_prop)

        eo_prop = {
            'Enum1':{
                'options':['option 1', 'option 2'],
                'return_index':True,
            },
            'Enum2':{
                'options':{
                    'option 1':{'index':2, 'tooltip':'description 1'},
                    'option 2':4,
                }
            }
        }
        self.create_enum_outputs(eo_prop)

        # Create widgets for output objects
        dds_widgets,ao_widgets,do_widgets = self.auto_create_widgets()
        eo_widgets = self.auto_create_enum_widgets()
        
        # This function allows you do sort the order of widgets by hardware name.
        # it is pass to the Python 'sorted' function as key=sort when passed in as 
        # the 3rd item of a tuple p(the tuple being an argument of self.auto_place_widgets()
        #
        # This function takes the channel name (hardware name) and returns a string (or whatever) 
        # that when sorted alphabetically, returns the correct order
        def sort(channel):
            port,line = channel.replace('port','').replace('line','').split('/')
            port,line = int(port),int(line)
            return '%02d/%02d'%(port,line)
        
        # and auto place them in the UI
        self.auto_place_widgets(("DDS Outputs",dds_widgets),
                                ("Analog Outputs",ao_widgets),
                                ("Digital Outputs - Port 0",do_widgets),
                                ('Enums', eo_widgets))
        
        # Set the primary worker
        self.create_worker("my_worker_name",DeviceWorker,{})
        self.primary_worker = "my_worker_name"    
        self.create_worker("my_secondary_worker_name",DeviceWorker,{})
        self.add_secondary_worker("my_secondary_worker_name")

        self.supports_remote_value_check(True)

        # Create buttons to test things!
        button1 = QPushButton("Transition to Buffered")
        button1.clicked.connect(lambda: self.transition_to_buffered('',Queue()))
        self.get_tab_layout().addWidget(button1)
        button2 = QPushButton("Transition to Manual")
        button2.clicked.connect(lambda: self.transition_to_manual(Queue()))
        self.get_tab_layout().addWidget(button2)

connection_table = ConnectionTable('./tests/device_base_classes_connection_table.h5')

class MyWindow(QWidget):
    
    def __init__(self,*args,**kwargs):
        QWidget.__init__(self,*args,**kwargs)
        self.are_we_closed = False
        self.setGeometry(500, 500, 1920, 1080)
    
    def closeEvent(self,event):
        if not self.are_we_closed:        
            event.ignore()
            self.my_tab.close_tab()
            self.are_we_closed = True
            QTimer.singleShot(1000,self.close)
        else:
            event.accept()

    def add_my_tab(self,tab):
        self.my_tab = tab

def test_window():
        
    app = QApplication(sys.argv)
    window = MyWindow()
    layout = QVBoxLayout(window)
    notebook = DragDropTabWidget()
    layout.addWidget(notebook)

    tab1 = MyDAQTab(notebook,settings = {'device_name': 'ni_pcie_6363_0', 'connection_table':connection_table})
    tab2 = MyDummyTab(notebook,settings = {'device_name': 'intermediate_device', 'connection_table':connection_table})
    window.add_my_tab(tab1)
    window.show()
    import time
    time.sleep(4)
    app.quit()
    # def run():
    #     app.exec_()
        
    # sys.exit(run())
