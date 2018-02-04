# Problem
When I work with my ideas that live in DXF files and need to be cut from plywood with the help of CO2 laser.
I ran into a small problem. I don't own a CO2 laser cutter so the designs have to be solid or it would cost me a fortune
to tune the designs by trial and error. My other python tool called [co2tools](https://github.com/Mambix/co2tools) allowed me to create STL files from my DXF drawings.

# Idea
Now I had to visualise the parts somehow to see if they fit together. I already use FreeCAD a lot as I use it to design 3D parts that I print on my 3D printer. So it was a no brainer to include it in my workflow. But how to easily load the files into FreeCAD? My first python scripts, before I refactored them and published them on gitHub, were simple FreeCAD macros that imported files for me, moved them if needed and applied color to them. But I wanted to go the YAML way as I already used it as my approach for the [co2tools](https://github.com/Mambix/co2tools) python library (my other project as mentioned above). 

# Solution
FreeCAD uses python internally as scripting language. Briliant! So all I needed to write is a workspace plugin that will load parts from YAML file.
**Which is exactly what I did!** This python code adds **new import filter to FreeCAD**, giving the user an option to load and manipulate objects from YAML file.
 That way the process can be fairly well automated, making it easier to design and check 3D parts before manufacturing. Hopefully lowering costs in the process.

This python code adds a new import filter to FreeCAD, giving the user an option to load and manipulate objects from YAML files. That way the process can be fairly well automated, making it easier to design and check 3D parts before manufacturing. Hopefully lowering costs in the process.

# Installation
In essence you need to: 
* Find your `Mod/` sub-folder or create one if it does not exist
* Clone this repository
* You will see a new folder called yaml-workspace in Mod folder. FreeCAD has good very tutorial on this topic [here](https://www.freecadweb.org/wiki/How_to_install_additional_workbenches).
It explains in detail how to do it based on what platform you're working on.

# Usage
As simple as opening new file (Ctrl+O on Windows) in FreeCAD and selecting your YAML file. If there are no errors, the python script will import your objects into a new document.

# YAML Structure
Example code:
```YML
settings:
  subDirectory: stl
import:
  DocumentName:
    GroupName:
      files:
        - movedRIGHT.stl
        - movedLEFT.stl
        - movedTOP.stl
      movedBOTTOM.stl:
        color: [.0, .0, 1.0]
      movedFRONT.stl:
        color: red
      movedBACK.stl:
        color: red
```

## Settings
This is where you can set a subfolder based on the folder where you load the .yml file from. Let's say you opened the YAML file from `C:\GIT\MyProject\3D-Printer.yml`.
When you define subDirectory for your STL files as `subDirectory: stl`, script will search for your files in `C:\GIT\MyProject\stl` directory.

## Import
This is where your import instructions go. `DocumentName` is what the script is going to name the new document it creates on import.
`GroupName` is the name of the group that will serve as a container of added objects. `files` section represents an array of files we want to add to FreeCAD document.
Note that there are no instruction here to color them or move/rotate them. It's just a simple import with default properties. Next instructions give you a bit more control over imported objects.
 `movedBOTTOM.stl` is the name of the file that will be imported as `C:\GIT\MyProject\stl\movedBOTTOM.stl` file. When imported it will be assigned blue color because array [0, 0, 1] represents #0000FF color.
 You can also use well known names like in the next file. `movedFRONT.stl` will be added to the document and painted red.

# End result
[![IMAGE ALT TEXT](http://img.youtube.com/vi/PO6Uz16cdP8/0.jpg)](http://www.youtube.com/watch?v=PO6Uz16cdP8 "Video Title")

# Contribution
Contributions to this repo are welcome. Please fork this repo and create a pull request.

# Issue
The code is still in very early stages so I don't expect this to work on all imports. 
I tested it on my projects and it looks like it is working good enough to be released to public for further testing.
 If you do run into problems please look through issues if it's not already reported or create new issue for it.
When opening issues I only ask that you give as much information as possible. Share your YAML file in the opened issue.
The more information I get the faster I can figure out what the problem is and fix it.

# Donations
You can also support this project by donating **Ethereum or any ERC20 tokens**.
ETH Wallet Address: 0x91400083bf0DaC3474B70550662D32473Ab97d3b
![0x91400083bf0DaC3474B70550662D32473Ab97d3b](https://s3-eu-west-1.amazonaws.com/backup.red-mamba.com/ETH/0x91400083bf0DaC3474B70550662D32473Ab97d3b.png)
**Contributions of any size are welcome. Thank you!**
