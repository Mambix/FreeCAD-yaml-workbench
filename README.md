# YAML Workspace
A FreeCAD addon that loads and manipulates objects via YAML

## Problem
When I work with my ideas that live in DXF files and need to be cut from plywood with the help of CO2 laser.
I ran into a small problem. I don't own a CO2 laser cutter so the designs have to be solid or it would cost me a fortune
to tune the designs by trial and error. My other python tool called [co2tools](https://github.com/Mambix/co2tools) allowed me to create STL files from my DXF drawings.

## Idea
Now I had to visualise the parts somehow to see if they fit together. I already use FreeCAD a lot as I use it to design 3D parts that I print on my 3D printer. So it was a no brainer to include it in my workflow. But how to easily load the files into FreeCAD? My first python scripts, before I refactored them and published them on gitHub, were simple FreeCAD macros that imported files for me, moved them if needed and applied color to them. But I wanted to go the YAML way as I already used it as my approach for the [co2tools](https://github.com/Mambix/co2tools) python library (my other project as mentioned above).

## Solution
FreeCAD uses python internally as scripting language. Briliant! So all I needed to write is a workspace plugin that will load parts from YAML file.
**Which is exactly what I did!** This python code adds **new import filter to FreeCAD**, giving the user an option to load and manipulate objects from YAML file.
 That way the process can be fairly well automated, making it easier to design and check 3D parts before manufacturing. Hopefully lowering costs in the process.

This python code adds a new import filter to FreeCAD, giving the user an option to load and manipulate objects from YAML files. That way the process can be fairly well automated, making it easier to design and check 3D parts before manufacturing. Hopefully lowering costs in the process.

## Installation

### FreeCAD Addon Manager
Use the FreeCAD built-in [Addon Manager](https://github.com/FreeCAD/FreeCAD-addons#1-builtin-addon-manager) to seamlessly install this Addon.
Found in **Tools -> Addon Manager**

### Manual Installation
In essence you need to:
* Find your `Mod/` sub-folder or create one if it does not exist
* Clone this repository
* You will see a new folder called `yaml-workspace` in the `Mod` folder. FreeCAD has good very tutorial on this topic [here](https://www.freecadweb.org/wiki/How_to_install_additional_workbenches).
It explains in detail how to do it based on what platform you're working on.

## Usage
As simple as opening new file (Ctrl+O on Windows) in FreeCAD and selecting your YAML file. If there are no errors, the python script will import your objects into a new document.

## YAML Structure
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
      HDD.step:
        - objectName: HDD_0
          color: yellow
          transparency: 25
          placement: [-25.0, 65.05, 159.0]
          rotationAngle: 180
          rotationVector: [.0, .0, 1.0]
        - objectName: HDD_1
          color: yellow
          transparency: 25
          placement: [-25.0, 34.19, 159.0]
          rotationAngle: 180
          rotationVector: [.0, .0, 1.0]
        - objectName: HDD_2
          color: yellow
          transparency: 25
          placement: [-25.0, 3.33, 159.0]
          rotationAngle: 180
          rotationVector: [.0, .0, 1.0]
```

### Settings
This is where you can set a subfolder based on the folder where you load the .yml file from. Let's say you opened the YAML file from `C:\GIT\MyProject\3D-Printer.yml`.
When you define subDirectory for your STL files as `subDirectory: stl`, script will search for your files in `C:\GIT\MyProject\stl` directory.

### Import
This is where your import instructions go. `DocumentName` is what the script is going to name the new document it creates on import.
`GroupName` is the name of the group that will serve as a container of added objects. `files` section represents an array of files we want to add to FreeCAD document.
Note that there are no instruction here to color them or move/rotate them. It's just a simple import with default properties. Next instructions give you a bit more control over imported objects.
 `movedBOTTOM.stl` is the name of the file that will be imported as `C:\GIT\MyProject\stl\movedBOTTOM.stl` file. When imported it will be assigned blue color because array [0, 0, 1] represents #0000FF color.
 You can also use well known names like in the next file. `movedFRONT.stl` will be added to the document and painted red.
 `HDD.step` demonstrates how a model can be imported multiple times at different locations using different settings.

 ### Common library folder
If you need to import same object(s) to different projects you can now do this easilly from default library folder.
Place your models into `~/.FreeCAD/Mod/yaml-workspace` and reference them simply by name in your `.co2tools.yml` configuration file.
If the script does not find a file specified in the `sourceDirectory` location it will check `~/.FreeCAD/Mod/yaml-workspace` folder.
If it can not be found there an error will be printed to console.

### Importing parts
With the support for common library folder there was also a new fearture added that allows you to import parts.
Before you were limited to importing Meshes from .stl files. This logic was now uptated in a way that if the file
ends with `.stp`, `.igs`, `.iges` or `.step`.

### Simple solids
It is now possible to insert simple objects like `cylinder`, `sphere`, `ellipsoid`, `box`, `cone`, `torus`, `prism` and `wedge`.

Examples (`color`, `transparency`, `placement`, `rotationAngle`, and `rotationVector` are available to all imported object):
```yaml
import:
  DocumentName:
    GroupName:
      CYLINDER_NAME:
        solid: cylinder
        radius: 6.0
        height: 410.0
        angle: 120 #optional
        placement: [.0, .0, .0]
      SPHERE_NAME:
        solid: sphere
        radius: 6.0
        angle1: 45 #optional
        angle2: 120 #optional
        angle3: 180 #optional
        placement: [.0, .0, .0]
      ELLIPSOID_NAME:
        solid: ellipsoid
        radius1: 6.0
        radius2: 12.0
        radius3: 9.0
        angle1: 45 #optional
        angle2: 120 #optional
        angle3: 180 #optional
        placement: [.0, .0, .0]
      BOX_NAME:
        solid: box
        length: 6.0
        width: 24.0
        height: 12.0
        placement: [.0, .0, .0]
      CONE_NAME:
        solid: cone
        radius1: 6.0
        radius2: 12.0
        height: 12.0
        angle: 120 #optional
        placement: [.0, .0, .0]
      TORUS_NAME:
        solid: torus
        radius1: 6.0
        radius2: 12.0
        angle1: 45 #optional
        angle2: 120 #optional
        angle3: 180 #optional
        placement: [.0, .0, .0]
      PRISM_NAME:
        solid: prism
        polygon: 6 #hexagon
        radius: 12.0
        height: 24.0
        placement: [.0, .0, .0]
      WEDGE_NAME:
        solid: wedge
        xmin: 6.0
        ymin: 12.0
        zmin: 24.0
        x2min: 15.0
        y2min: 16.0
        xmax: 36.0
        ymax: 42.0
        zmax: 54.0
        x2max: 115.0
        y2max: 116.0
        placement: [.0, .0, .0]
```

## End result
[![IMAGE ALT TEXT](http://img.youtube.com/vi/PO6Uz16cdP8/0.jpg)](http://www.youtube.com/watch?v=PO6Uz16cdP8 "Video Title")

## Contribution
Contributions to this repo are welcome. Please fork this repo and create a pull request.

## Known Issues
The code is still in very early stages so I don't expect this to work on all imports.
I tested it on my projects and it looks like it is working good enough to be released to public for further testing.
 If you do run into problems please look through issues if it's not already reported or create new issue for it.
When opening issues I only ask that you give as much information as possible. Share your YAML file in the opened issue.
The more information I get the faster I can figure out what the problem is and fix it.

- Random boolean operation: https://github.com/mikedh/trimesh/issues/1096#issuecomment-752147059
  - a workaround has been added to the code for this that in some extreme cases might return anwanted results

## Developers
Addon creator: [@Mambix](https://github.com/Mambix)
Logo creator: @bitacovir via [FreeCAD community](https://forum.freecadweb.org/viewtopic.php?f=34&t=37049)

## Donations
You can also support this project by donating **Ethereum or any ERC20 tokens**.
ETH Wallet Address: 0x91400083bf0DaC3474B70550662D32473Ab97d3b

![0x91400083bf0DaC3474B70550662D32473Ab97d3b](https://s3-eu-west-1.amazonaws.com/backup.red-mamba.com/ETH/0x91400083bf0DaC3474B70550662D32473Ab97d3b.png)

**Contributions of any size are welcome. Thank you!**

## License
GNU Lesser General Public License v2.1
