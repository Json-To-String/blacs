import sys
from labscript_utils.qtwidgets.dragdroptab import DragDropTabWidget
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QWidget,
)

from blacs.tab_base_classes import MyTab, Tab, Counter


class FakeConnection(object):
    properties = {}

    def __init__(self):
        self.BLACS_connection = "None"


class FakeConnectionTable(object):
    def __init__(self):
        pass

    def find_by_name(self, device_name):
        return FakeConnection()


def test_counter():
    test_counter = Counter()
    count = test_counter.get()
    assert count == 1, f"Counter logic wrong, got {count} instead"


def test_build_fake_tab():
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QVBoxLayout(window)
    notebook = DragDropTabWidget()
    layout.addWidget(notebook)
    connection_table = FakeConnectionTable()

    # TODO: Do more than just construct

    tab1 = Tab(
        notebook,
        settings={"device_name": "ExampleDevice", "connection_table": connection_table},
    )
    
    tab2 = Tab(
        notebook,
        settings={
            "device_name": "ExampleDevice2",
            "connection_table": connection_table,
        },
    )

    window.show()
    # app.exec_()
    tab1.close_tab()
    tab2.close_tab()
    app.quit()


# def run():
#     test_counter()
#     app.exec_()
# tab1.close_tab()
# tab2.close_tab()


# sys.exit(run())
