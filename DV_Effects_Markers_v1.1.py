#!/usr/bin/env python3

# Get pip on macos with 
# curl https://bootstrap.pypa.io/pip/3.6/get-pip.py -o get-pip.py
# python3 get-pip.py


# IMPORTING MODULES
# ////////////////////////////////////////////////////////////////////////////////
import subprocess
import sys


# Imports the timecode module. Installs it if it's not already.
try:
    from timecode import Timecode
except:
    name = 'timecode'
    def install(package):
        try:
            subprocess.check_call([sys.executable, "python3", "-m", "ensurepip"])
        except:
            pass
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    try:
        install("timecode")
    except:
        subprocess.check_call([sys.executable, "-m", "ensurepip"])
        subprocess.check_call([sys.executable, "-m", "pip", "install", 'timecode'])
    from timecode import Timecode


# GATHERES THE NECESSARY RESOLVE OBJECTS
# //////////////////////////////////////////////////////////////////////////////////
fu                  = resolve.Fusion()
projectManager      = resolve.GetProjectManager()
project             = projectManager.GetCurrentProject()
timeline            = project.GetCurrentTimeline()
fps                 = project.GetSetting('timelineFrameRate')    



# INITIAL VARIABLE
# /////////////////////////////////////////////////////////////////////////////////
ignore              = True
file        = "Select a file..."


# If any of these strings are found in a line of the Effects report, that entire line will be ignored.
skip = [
    "Resize", 
    "Timewarp", 
    "Color", 
    "Motion Adapter", 
    "Dissolve", 
    "Title"
    ]


# DEFINE THE COLOUR OF MARKERS FOR CERTAIN EFFECT TYPES
# ////////////////////////////////////////////////////////////////////////////////
titles =        "Sky"
other =         "Lavender"


# USER INTERFACE
# /////////////////////////////////////////////////////////////////////////////////////
ui                  = fu.UIManager
disp                = bmd.UIDispatcher(ui)


width = 800
height = 220

# STYLES
yellow = f"""
color: rgb(255, 255, 0);
font-family: Open Sans;
font-weight: bold;
font-size: 12px;
"""

# CREATE A WINDOW 
dlg = disp.AddWindow({  "WindowTitle": "DV Effect Markers v1.1", 
                        "ID": "MyWin",
                        "WindowOpacity" : 1,
                        "Geometry": [ 600, 400, width, height ],
                        'BackgroundColor': {'R':0.25, 'G':0.31, 'B':0.3, 'A':0.6},
                      },
                     
                     
# ADD UI ELEMENTS HERE
    [   
        
        ui.VGroup({"ID": "root", 
                   "Spacing": 10,
                   'MaximumSize': [width, height],
                   'MinimumSize': [width, height],
                   "Weight": 0}, # The spaces between each item
        [   
            ui.VGap(2),
            # First Horizontal Row
            ui.HGroup({ "ID": "H1",
                        "Spacing": 20,
                        "Weight": 0},
                      [
                        ui.Label({      "ID": "FolderLabel",
                                        "Text": "Sequence Report Location:",
                                        "Weight": 0}),
                        
                        ui.LineEdit({   "ID": "LineTxt", 
                                        "Text": file,
                                        "Editable" : False,
                                        'MaximumSize': [800, 20],
                                        "Weight": 1}),   
                        ]),
            ui.VGap(2),
            
            ui.Label({  "ID": "IgnoreLabel",
                        "Text": "Select effect types to ignore:",
                        "Weight": 0.25}),          
            
            # Second Horizontal Row
            ui.HGroup({ "ID": "H2",
                        "Spacing": 10,
                        "Weight": 1},
                      
                      [
                        ui.CheckBox({   "ID": "TimewarpCheckbox",
                                        "Text": "Timewarp",
                                        "Checkable": True,
                                        "Checked": True,
                                        "Weight": 0.25}),
                        
                        ui.ComboBox({ 'ID': 'combo_1',
                                     'MaximumSize': [100, height],
                                     "Alignment": { 'AlignLeft' : True }
                                     }),
                        
                        ui.CheckBox({   "ID": "MotionCheckbox",
                                        "Text": "Motion Adapters",
                                        "Checkable": True,
                                        "Checked": True,
                                        "Weight": 0.25}),
                        
                        ui.CheckBox({   "ID": "ColourCheckbox",
                                        "Text": "Colour",
                                        "Checkable": True,
                                        "Checked": True,
                                        "Weight": 0.25}),
                        
                        ui.CheckBox({   "ID": "ResizeCheckbox",
                                        "Text": "Resizes",
                                        "Checkable": True,
                                        "Checked": True,
                                        "Weight": 0.25}),
                        
                        ui.CheckBox({   "ID": "DissolveCheckbox",
                                        "Text": "Dissolve",
                                        "Checkable": True,
                                        "Checked": True,
                                        "Weight": 0.25}),                                
                      ]),
            # Third Horizontal Row
            ui.HGroup({"ID": "H3",
                       "Spacing": 10,
                       "Weight": 1},
                      [

                        ui.CheckBox({"ID": "TitleCheckbox",
                                  "Text": "Titles",
                                  "Checkable": True,
                                  "Checked": False,
                                  "Weight": 0.25}),
                        
                        ui.CheckBox({"ID": "BlurCheckbox",
                                  "Text": "Blurs",
                                  "Checkable": True,
                                  "Checked": False,
                                  "Weight": 0.25}),
                        
                        ui.CheckBox({"ID": "MatteKeyCheckbox",
                                  "Text": "Matte Keys",
                                  "Checkable": True,
                                  "Checked": False,
                                  "Weight": 0.25}),  
                        
                        ui.CheckBox({"ID": "SubCapCheckbox",
                                  "Text": "Sub Caps",
                                  "Checkable": True,
                                  "Checked": False,
                                  "Weight": 0.25}),
                        
                         ui.CheckBox({"ID": "PanzoomCheckbox",
                                  "Text": "Pan & Zooms",
                                  "Checkable": True,
                                  "Checked": False,
                                  "Weight": 0.25}),
                         ]),
            
            ui.Label({  "ID": "Empty",
                        "Weight": 1 }),
                        
            # Forth Horizontal Row
            ui.HGroup({"ID": "H4",
                       "Spacing": 10,
                       "Weight": 1},
                      [            
                        ui.Button({ "ID": "BrowseButton", 
                                "Text": "Browse", 
                                "Weight": 0,}),
                        
                        ui.Button({ "ID": "CancelButton", 
                                "Text": "Cancel", 
                                "Weight": 0}),
                        
                        ui.Button({ "ID": "GoButton",
                                "Text": "Go!", 
                                "Weight": 0,
                                "Checkable": True,}),                        
                        
                        ui.Label({"ID": "Processing",
                                  "Text": "Processing...",
                                  "Hidden": True,
                                  'StyleSheet': yellow,
                                  "Font": ui.Font({ 'Italic': True }),
                                  "Weight": 0.25}),                        
                        
                        ui.Label({"ID": "Empty",
                                "Weight": 1 }),
                        ])
        ]),
    ])


dlg.Find("combo_1").AddItems(["Blue","Cyan","Green","Yellow","Red","Pink","Purple","Fuchsia","Rose","Lavender","Sky","Mint","Lemon","Sand","Cocoa","Cream"]),
# GUI ELEMENT EVENT FUNCTIONS
# ///////////////////////////////////////////////////////////////////////////////////
 
itm = dlg.GetItems()

# THE WINDOW WAS CLOSED
def _func(ev):
    disp.ExitLoop()
dlg.On.MyWin.Close = _func
 
# CANCEL BUTTON IS CLICKED
def _func(ev):
    disp.ExitLoop()
dlg.On.CancelButton.Clicked = _func

# OK BUTTON IS CLICKED
def _func(ev):
    print("OK clicked")
    disp.ExitLoop()
    dlg.On.OKButton.Clicked = _func

# BROWSE BUTTON WAS CLICKED
def _func(ev):
    global file
    print('Browse Button Clicked')
    file = str(fu.RequestFile()).replace("\\", "\\\\")
    # file = str(file).replace("\\", "\\\\")
    if file != None:
        print("[File]" + file)
        itm["LineTxt"].Text = file
dlg.On.BrowseButton.Clicked = _func

# WARNING DIALOG
def warning(text):        
    dlg = disp.AddWindow({  "WindowTitle": "Warning!", 
                            "ID": "Warning",
                            "Geometry": [ 100, 100, 600, 100 ]}, 
                            [
                            ui.VGroup({ "ID": "root2", 
                                        "Spacing": 10,
                                        "Weight": 1}, 
                                        [
                                        ui.Label({  "ID": "WarningText",
                                                    "Text": text,
                                                    "Weight": 0.25}),
                                        
                                        ui.Button({ "ID": "OKButton", 
                                                    "Text": "OK", 
                                                    "Weight": 0}),
                                        ])
                            ])        
                

# GO BUTTON WAS CLICKED
def _func(ev):
    print("Go Button pressed")
    if file == "Select a file...":
        warning("Please select a file...")
    itm["BrowseButton"].Hidden = True
    itm["Processing"].Hidden = False
    itm["GoButton"].Hidden = True
    Go()
dlg.On.GoButton.Clicked = _func


# OPEN REPORT FILE AND PARSING OUT TIMECODES AND EFFECT NAMES TO THEN SEND TO RESOLVE AS MARKERS
# /////////////////////////////////////////////////////////////////////////////////
def Go():
    global ignore
    print("Go Function launched")
    try:
        print(type(file))
        print(file)  
        with open(file, "r", encoding = "utf8", errors = 'ignore') as report:
            for line in report:
         
                # Remove stupid hidden characters added by Avid
                line.replace('\x00','')
                line = ''.join(s for s in line if ord(s)>31 and ord(s)<126)
                
                # Stops reading once this line is found
                if "##########################" in line:
                    ignore = True
                
                # Do all the important stuff
                if not ignore:
                    tcsplit = line.split()
                    if tcsplit != []:
                        tc = tcsplit[1]
                        zerotc = "00:" + tc.split(":", 1)[1]
                        
                        tc = Timecode(fps, zerotc)

                        frames = tc.frames - 1
                    
                    namesplit = line.split("       ")
                    if namesplit != ['']:
                        name = namesplit[2]
                    
                    if tcsplit !=[]:
                        if not any(value in line for value in skip):
                                timeline.AddMarker(frames, other, name, '', 1)
                        if "Title" in line:
                            timeline.AddMarker(frames, titles, name, '', 1)
                
                # Begin reading lines after this line is found
                if "__ TRACK __" in line:
                    ignore = False
        disp.ExitLoop()
    except:
        warning("An error occured... Whoever programed this thing must be an idiot...")
        pass
    
    
# LAUNCHES UI
# ///////////////////////////////////////////////////////////////////////////////////////////////    
dlg.Show()
disp.RunLoop()
dlg.Hide()

