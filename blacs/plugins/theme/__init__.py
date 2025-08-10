#####################################################################
#                                                                   #
# /plugins/theme/__init__.py                                        #
#                                                                   #
# Copyright 2013, Monash University                                 #
#                                                                   #
# This file is part of the program BLACS, in the labscript suite    #
# (see http://labscriptsuite.org), and is licensed under the        #
# Simplified BSD License. See the license.txt file in the root of   #
# the project for the full license.                                 #
#                                                                   #
#####################################################################
import logging
import os
from qtutils import *
from blacs.plugins import PLUGINS_DIR

name = "GUI Theme"
module = "theme" # should be folder name
logger = logging.getLogger('BLACS.plugin.%s'%module)

def load_theme(theme_name):
    theme_path = os.path.join(PLUGINS_DIR, module, "themes", f"{theme_name}_theme.qss")
    try:
        with open(theme_path, "r") as f:
            return f.read()
    except Exception as e:
        logger.warning(f"Could not load theme '{theme_name}': {e}")
        return ""


DEFAULT_STYLESHEET = """DigitalOutput {
    font-size: 12px;
    background-color: rgb(50,100,50,255);
    border: 1px solid rgb(50,100,50,128);
    border-radius: 3px;
    padding: 2px;
    color: #202020;
}

DigitalOutput:hover {
    background-color: rgb(50,130,50);
    border: None;
}

DigitalOutput:disabled{
   background-color: rgb(50,100,50,128);
   color: #505050;
}

DigitalOutput:checked {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 rgb(32,200,32), stop: 1 rgb(32,255,32));
    border: 1px solid #8f8f91;
    color: #000000;
}

DigitalOutput:hover:checked {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 rgb(32,200,32), stop: 1 rgb(120,255,120));
    border: 1px solid #8f8f91;
}

DigitalOutput:checked:disabled{
   background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 rgba(32,200,32,128), stop: 1 rgba(32,255,32,128));
   color: #606060;
}

InvertedDigitalOutput {
    font-size: 12px;
    background-color: rgb(70,100,170,255);
    border: 1px solid rgb(70,100,170,128);
    border-radius: 3px;
    padding: 2px;
    color: #202020;
}

InvertedDigitalOutput:hover {
    background-color: rgb(70, 130, 220);
    border: None;
}

InvertedDigitalOutput:disabled{
   background-color: rgba(70,100,170,128);
   color: #505050;
}

InvertedDigitalOutput:checked {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 rgb(50,150,221), stop: 1 rgb(32,192,255));
    border: 1px solid #8f8f91;
    color: #000000;
}

InvertedDigitalOutput:hover:checked {
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 rgb(50,150,221), stop: 1 rgb(120,192,255));
    border: 1px solid #8f8f91;
}

InvertedDigitalOutput:checked:disabled{
   background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                      stop: 0 rgba(50,150,221,128), stop: 1 rgba(32,192,255,128));
   color: #606060;
}
 """

# DARK_STYLESHEET = """
# # /* ===== Global & Widget Defaults ===== */
# # QWidget {
# #     background-color: #0f1115;
# #     color: #e6eef3;
# #     selection-background-color: #2b6ea3;
# #     selection-color: #ffffff;
# #     font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
# # }

# # /* ===== Push Buttons ===== */
# # QPushButton {
# #     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
# #                                       stop:0 #2a2e34, stop:1 #212427);
# #     border: 1px solid #2e3338;
# #     padding: 6px 10px;
# #     border-radius: 6px;
# #     color: #e6eef3;
# # }
# # QPushButton:hover { border-color: #3a7bd5; }
# # QPushButton:pressed { background-color: #1b1d20; }

# # /* ===== LineEdits, TextEdits ===== */
# # QLineEdit, QPlainTextEdit, QTextEdit {
# #     background-color: #0c0d0f;
# #     border: 1px solid #26282c;
# #     padding: 6px;
# #     border-radius: 4px;
# #     color: #e6eef3;
# # }
# # QLineEdit:focus, QTextEdit:focus { border-color: #3a7bd5; }

# # /* ===== Tables, Headers ===== */
# # QHeaderView::section {
# #     background-color: #131417;
# #     color: #cfd8de;
# #     padding: 6px;
# #     border: 1px solid #232427;
# # }
# # QTableView, QTreeView, QListView {
# #     background-color: #0b0c0e;
# #     gridline-color: #17181b;
# #     alternate-background-color: #0f1013;
# # }
# # QTableView::item:selected, QTreeView::item:selected, QListView::item:selected {
# #     background-color: #2b6ea3;
# #     color: #fff;
# # }

# # /* ===== Combo & Spin Boxes ===== */
# # QComboBox, QSpinBox, QDoubleSpinBox {
# #     background-color: #0c0d0f;
# #     border: 1px solid #26282c;
# #     padding: 4px;
# #     color: #e6eef3;
# # }

# # /* ===== Checkboxes / Radios ===== */
# # QCheckBox, QRadioButton { spacing: 6px; }
# # QCheckBox::indicator, QRadioButton::indicator {
# #     background-color: transparent;
# #     border: 1px solid #3a3d42;
# # }

# # /* ===== Progress Bar ===== */
# # QProgressBar {
# #     border: 1px solid #2b2f34;
# #     background: #0c0d0f;
# #     text-align: center;
# #     border-radius: 6px;
# # }
# # QProgressBar::chunk {
# #     background-color: #3a7bd5;
# #     border-radius: 6px;
# # }

# # /* ===== Tabs ===== */
# # QTabWidget::pane { border: 1px solid #232427; }
# # QTabBar::tab {
# #     background: #0f1115;
# #     color: #cfd8de;
# #     padding: 8px;
# #     border: 1px solid #232427;
# #     border-bottom: none;
# #     border-top-left-radius: 6px;
# #     border-top-right-radius: 6px;
# # }
# # QTabBar::tab:selected { background: #16181c; }

# # /* ===== Dock Widgets ===== */
# # QDockWidget { titlebar-close-icon: url(:/icons/close.png); title: " "; }
# # QDockWidget::title { background: #101215; }

# # /* ===== Menus & Tooltips ===== */
# # QMenuBar, QMenu {
# #     background-color: #0f1115;
# #     color: #e6eef3;
# # }
# # QMenu::item:selected { background-color: #2b6ea3; color: #fff; }
# # QToolTip {
# #     background-color: #1c1f22;
# #     color: #e6eef3;
# #     border: 1px solid #3a3f45;
# #     padding: 6px;
# # }

# # /* ===== Scrollbars & Splitters ===== */
# # QScrollBar:vertical {
# #     background: #0f1115;
# #     width: 12px;
# # }
# # QScrollBar::handle:vertical {
# #     background: #2b2e33;
# #     min-height: 20px;
# #     border-radius: 6px;
# # }
# # QScrollBar::add-line, QScrollBar::sub-line { height: 0px; }
# # QSplitter::handle { background: #151618; }

# # /* ===== Status Bar ===== */
# # QStatusBar { background: #0f1115; color: #cfd8de; }

# # """

# BLUE_STYLESHEET = """
# /* ===== Global & Widget Defaults ===== */
# QWidget {
#     background-color: #0a0f1a;
#     color: #e1e8f0;
#     selection-background-color: #1e4a72;
#     selection-color: #ffffff;
#     font-family: "Segoe UI", "Helvetica Neue", Arial, sans-serif;
# }

# /* ===== Push Buttons ===== */
# QPushButton {
#     background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
#                                       stop:0 #1a2332, stop:1 #0f1520);
#     border: 1px solid #1e2b3d;
#     padding: 6px 10px;
#     border-radius: 6px;
#     color: #e1e8f0;
# }
# QPushButton:hover { border-color: #2563eb; }
# QPushButton:pressed { background-color: #0d1117; }

# /* ===== LineEdits, TextEdits ===== */
# QLineEdit, QPlainTextEdit, QTextEdit {
#     background-color: #070b14;
#     border: 1px solid #1a2332;
#     padding: 6px;
#     border-radius: 4px;
#     color: #e1e8f0;
# }
# QLineEdit:focus, QTextEdit:focus { border-color: #2563eb; }

# /* ===== Tables, Headers ===== */
# QHeaderView::section {
#     background-color: #0d1421;
#     color: #b8c5d6;
#     padding: 6px;
#     border: 1px solid #1a2332;
# }
# QTableView, QTreeView, QListView {
#     background-color: #060a12;
#     gridline-color: #0f1520;
#     alternate-background-color: #080d17;
# }
# QTableView::item:selected, QTreeView::item:selected, QListView::item:selected {
#     background-color: #1e4a72;
#     color: #fff;
# }

# /* ===== Combo & Spin Boxes ===== */
# QComboBox, QSpinBox, QDoubleSpinBox {
#     background-color: #070b14;
#     border: 1px solid #1a2332;
#     padding: 4px;
#     color: #e1e8f0;
# }

# /* ===== Checkboxes / Radios ===== */
# QCheckBox, QRadioButton { spacing: 6px; }
# QCheckBox::indicator, QRadioButton::indicator {
#     background-color: transparent;
#     border: 1px solid #2c3e50;
# }

# /* ===== Progress Bar ===== */
# QProgressBar {
#     border: 1px solid #1a2332;
#     background: #070b14;
#     text-align: center;
#     border-radius: 6px;
# }
# QProgressBar::chunk {
#     background-color: #2563eb;
#     border-radius: 6px;
# }

# /* ===== Tabs ===== */
# QTabWidget::pane { border: 1px solid #1a2332; }
# QTabBar::tab {
#     background: #0a0f1a;
#     color: #b8c5d6;
#     padding: 8px;
#     border: 1px solid #1a2332;
#     border-bottom: none;
#     border-top-left-radius: 6px;
#     border-top-right-radius: 6px;
# }
# QTabBar::tab:selected { background: #0f1520; }

# /* ===== Dock Widgets ===== */
# QDockWidget { titlebar-close-icon: url(:/icons/close.png); title: " "; }
# QDockWidget::title { background: #0a0f1a; }

# /* ===== Menus & Tooltips ===== */
# QMenuBar, QMenu {
#     background-color: #0a0f1a;
#     color: #e1e8f0;
# }
# QMenu::item:selected { background-color: #1e4a72; color: #fff; }
# QToolTip {
#     background-color: #0f1520;
#     color: #e1e8f0;
#     border: 1px solid #2c3e50;
#     padding: 6px;
# }

# /* ===== Scrollbars & Splitters ===== */
# QScrollBar:vertical {
#     background: #0a0f1a;
#     width: 12px;
# }
# QScrollBar::handle:vertical {
#     background: #1a2332;
#     min-height: 20px;
#     border-radius: 6px;
# }
# QScrollBar::add-line, QScrollBar::sub-line { height: 0px; }
# QSplitter::handle { background: #0f1520; }

# /* ===== Status Bar ===== */
# QStatusBar { background: #0a0f1a; color: #b8c5d6; }
# """

def is_default_stylesheet(stylesheet):
    """Return whether a stylesheet is the same as the default stylesheet, modulo whitespace"""

    def no_whitespace(s):
        return "".join(s.split())

    return no_whitespace(str(stylesheet)) == no_whitespace(DEFAULT_STYLESHEET) 


class Plugin(object):
    def __init__(self,initial_settings):
        self.menu = None
        self.notifications = {}
        self.BLACS = None
        self.initial_settings = initial_settings
        
    def get_menu_class(self):
        return None
        
    def get_notification_classes(self):
        return []
        
    def get_setting_classes(self):
        return [Setting]
        
    def get_callbacks(self):
        return {'settings_changed':self.update_stylesheet}
        
    def update_stylesheet(self):
        if self.BLACS is not None:
            # show centralwidget as a workaround to fix stylsheets
            # not beeing applied under PyQt5 on first draw
            self.BLACS['ui'].centralwidget.show()
            stylesheet_settings = self.BLACS['settings'].get_value(Setting,"stylesheet")
            self.BLACS['ui'].centralwidget.setStyleSheet(self.unmodified_stylesheet + stylesheet_settings)
        
    def set_menu_instance(self,menu):
        self.menu = menu
                
    def set_notification_instances(self,notifications):
        self.notifications = notifications
        
    def plugin_setup_complete(self, BLACS):
        self.BLACS = BLACS
        self.unmodified_stylesheet = self.BLACS['ui'].centralwidget.styleSheet()
        self.update_stylesheet()
    
    def get_save_data(self):
        return {}
    
    def close(self):
        pass
        
    
class Setting(object):
    name = name

    def __init__(self, data):
        self.data = data
        if 'stylesheet' not in self.data or not self.data['stylesheet']:
            self.data['stylesheet'] = load_theme('default') or DEFAULT_STYLESHEET

    def on_set_default_theme(self):
        self.widgets['stylesheet'].setPlainText(load_theme('default'))
        
    def on_set_green_button_theme(self):
        self.widgets['stylesheet'].setPlainText(DEFAULT_STYLESHEET)

    def create_dialog(self, notebook):
        ui = UiLoader().load(os.path.join(PLUGINS_DIR, module, 'theme.ui'))
        # restore current stylesheet
        ui.stylesheet_text.setPlainText(self.data['stylesheet'])
        # Populate theme_combo with available .qss files
        theme_dir = os.path.join(PLUGINS_DIR, module, 'themes')
        themes = [f for f in os.listdir(theme_dir) if f.endswith('.qss')]
        theme_names = [os.path.splitext(f)[0].replace('_theme','') for f in themes]
        ui.theme_combo.clear()
        ui.theme_combo.addItems(theme_names)
        # Select current theme if possible
        current_theme = None
        for name in theme_names:
            if load_theme(name) == self.data['stylesheet']:
                current_theme = name
                break
        if current_theme:
            idx = theme_names.index(current_theme)
            ui.theme_combo.setCurrentIndex(idx)
        # Handler for theme selection
        def on_theme_selected(idx):
            theme_name = theme_names[idx]
            ui.stylesheet_text.setPlainText(load_theme(theme_name))
        ui.theme_combo.currentIndexChanged.connect(on_theme_selected)
        ui.example_button.clicked.connect(self.on_set_green_button_theme)
        
        # save reference to widget
        self.widgets = {}
        self.widgets['stylesheet'] = ui.stylesheet_text
        self.widgets['example_button'] = ui.example_button
        self.widgets['theme_combo'] = ui.theme_combo
        return ui, None
    
    def get_value(self,name):
        if name in self.data:
            return self.data[name]
        
        return None
    
    def save(self):
        stylesheet = str(self.widgets['stylesheet'].toPlainText())
        if not stylesheet.endswith('\n'):
            # This is a way to distinguish between an intentionally blank
            # stylesheet, and an empty string, which used to be what was
            # stored When the user had made no changes, which now we take to
            # imply that they want to use the default stylesheet:
            stylesheet += '\n'
        self.data['stylesheet'] = stylesheet
        data = self.data.copy()
        if is_default_stylesheet(stylesheet):
            # Only save if it is not the default stylesheet:
            del data['stylesheet']
        return data
        
    def close(self):
        self.widgets['example_button'].clicked.disconnect(self.on_set_green_button_theme)
