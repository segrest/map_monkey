''' Python Code written by Brad Segrest, adapted with the help of Jimmy Alley\
Based on the Python Toolbox Template by ESRI'''

import os
import arcpy

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "County Query and Zoom Tool"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [coQuery,Test]
        #self.tools = [coQuery,tableToPointsFeature]
        #self.tools = [coQuery]

class coQuery(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "County Query and Zoom To"
        self.description = "This tool allows the user to select counties from a\
                            list that the map will select, zoom to, and mask \
                            the rest of the state. Two layers are required for\
                            this script to run. One is named 'County' and the\
                            Other is Named 'Mask'. The County layer should have\
                            a hollow symbology and the mask should be solid \
                            with a display transparency. A template layer can \
                            be found:\
                            \\\mgis\gisdata\Layerfiles\CountySelection.lyr\n\n\
                            \n\n\n\n\n\
                            Warning: If you are using ArcGIS 10.1 this tool \
                            behaves in an erratic manner. Please us the County\
                            Query and Zoom To Tool in the GIS_Tools toolbox. "
        self.canRunInBackground = False
        self.stylesheet = "\\\MGIS\GISData\Tools\Stylesheets\CoQuery_CustomToolStylesheet.xsl"
        


    def getParameterInfo(self):
        """Define parameter definitions"""
        # First parameter
        param0 = arcpy.Parameter(
        displayName="Add County Selection Layer",
        name="addLyr",
        datatype="Boolean",
        multiValue = "False",
        parameterType="Optional",
        #values=[True,False]
        direction="Input")

        # Second parameter
        param1 = arcpy.Parameter(
        displayName="Counties",
        name="county",
        datatype="GPString",
        multiValue = "True",
        parameterType="Required",
        direction="Input")
        param1.filter.type = "ValueList"
        param1.filter.list = ['Adams','Alcorn','Amite','Attala','Benton',\
                                'Bolivar','Calhoun','Carroll','Chickasaw',\
                                'Choctaw','Claiborne','Clarke','Clay','Coahoma'\
                                ,'Copiah','Covington','Desoto','Forrest',\
                                'Franklin','George','Greene','Grenada',\
                                'Hancock','Harrison','Hinds','Holmes',\
                                'Humphreys','Issaquena','Itawamba','Jackson',\
                                'Jasper','Jefferson','Jefferson_Davis','Jones',\
                                'Kemper','Lafayette','Lamar','Lauderdale',\
                                'Lawrence','Leake','Lee','Leflore','Lincoln',\
                                'Lowndes','Madison','Marion','Marshall',\
                                'Monroe','Montgomery','Neshoba','Newton',\
                                'Noxubee','Oktibbeha','Panola','Pearl_River',\
                                'Perry','Pike','Pontotoc','Prentiss','Quitman',\
                                'Rankin','Scott','Sharkey','Simpson','Smith',\
                                'Stone','Sunflower','Tallahatchie','Tate',\
                                'Tippah','Tishomingo','Tunica','Union',\
                                'Walthall','Warren','Washington','Wayne',\
                                'Webster','Wilkinson','Winston','Yalobusha',\
                                'Yazoo']

        # Second parameter
        param2 = arcpy.Parameter(
        displayName="Replace existing County Selection Layer",
        name="replaceLyr",
        datatype="Boolean",
        multiValue = "False",
        parameterType="Optional",
        direction="Input")
    
        params = [param0,param1,param2]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # Set overwrite option
        arcpy.env.overwriteOutput = True
                    
        # Set Script Parameters
        addLyr=parameters[0].altered
        county = parameters[1].valueAsText
        replaceLyr=parameters[2].altered
        #replaceLyr=parameters[0].altered
        #addLyr=addLyr.lower()
        #replaceLyr=replaceLyr.lower()
        zoom = county.split(";")
        mxd = arcpy.mapping.MapDocument("CURRENT")
        for i in zoom:
            zoom[zoom.index(i)]=i.title()
        sPar= str(zoom)
        sPar=sPar.replace('u"','').replace('"','').replace('[','(').replace(']',')')
        dataframe = arcpy.mapping.ListDataFrames(mxd)[0]

            

        if replaceLyr==True:
            for lyr in arcpy.mapping.ListLayers(mxd):
                if lyr.name == "CountySelection":
                    arcpy.mapping.RemoveLayer(dataframe, lyr)
                elif lyr.name == "County":
                    arcpy.mapping.RemoveLayer(dataframe, lyr)
                elif lyr.name == "Mask":
                    arcpy.mapping.RemoveLayer(dataframe, lyr)
                elif lyr.name == "State Boundary Mask":
                    arcpy.mapping.RemoveLayer(dataframe, lyr)
            addLayer=arcpy.mapping.Layer(r"\\mgis\GISData\Layerfiles\CountySelection.lyr")
            arcpy.mapping.AddLayer(dataframe, addLayer, "TOP")

        if addLyr==True:
            addLayer=arcpy.mapping.Layer(r"\\mgis\GISData\Layerfiles\CountySelection.lyr")
            arcpy.mapping.AddLayer(dataframe, addLayer, "TOP")

        layerName=[]
        for i in arcpy.mapping.ListLayers(mxd):
            layerName.append(i.name)

        if 'CountySelection' not in layerName:
            addLayer=arcpy.mapping.Layer(r"\\mgis\GISData\Layerfiles\CountySelection.lyr")
            #addLayer=arcpy.MakeFeatureLayer_management(r"\\mgis\GISData\Layerfiles\CountySelection.lyr","CountySelection")
            arcpy.mapping.AddLayer(dataframe, addLayer, "TOP")
            layerName.append('CountySelection')
            

        for lyr in arcpy.mapping.ListLayers(mxd):
            if lyr.name == "County":
                zTo='CONAME in '+sPar
                lyr.definitionQuery = zTo
                ext = lyr.getExtent()
                dataframe.extent = ext
            elif lyr.name == "Mask":
                xClude='CONAME not in '+sPar
                lyr.definitionQuery = xClude
        
        arcpy.RefreshActiveView()
        arcpy.RefreshTOC()
        
        return 

class Test(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Testing Here"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return
