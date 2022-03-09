# Notes on embedding 3d objects (.3VR) in ArcGIS Online and Storymaps

1. Use iPhone app like Polycam or "3D Scanner App"
2. Export in OBJ to CityEngine or ArcGIS Pro (may require 3D Analyst extension)
3. Note 1: "GeoVRML is the only format that has a defined coordinate system. Many 3D models are generated using local coordinate systems that center the XYZ axis on 0, 0, 0. Such features can be georeferenced to real-world coordinates" [(link)](https://pro.arcgis.com/en/pro-app/2.8/tool-reference/3d-analyst/import-3d-files.htm)
4. Note 2: The Esri .3vr file format can be written at least by CityEngine [(link)](https://doc.arcgis.com/en/cityengine/2019.0/help/help-export-360vr.htm).
5. Note 3: It appears that one cannot run CityEngine 2021.1 on Mac at all.  I tried running under Parallels Windows but apparently Parallels 16 only supports OpenGL 3.3 and CityEngine requires 4.1. CityEngine 2020.1 – it looks like it may still install on Macs natively (link).
6. 
