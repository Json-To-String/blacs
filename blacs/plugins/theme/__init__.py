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
