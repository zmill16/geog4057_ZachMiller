# -*- coding: utf-8 -*-

import arcpy
from project1 import importJSON


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Project1_Tool"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        input_json = arcpy.Parameter(
            name='input_json',
            displayName='Input JSON File',
            direction = 'Input',
            datatype= 'DEFile',
            parameterType='Required'
        )
        output_feature = arcpy.Parameter(
            name='output_feature',
            displayName='Output Feature Class',
            direction = 'Output',
            datatype= 'GPString',
            parameterType='Required'
        )
        workspace = arcpy.Parameter(
            name='workspace',
            displayName='Workspace',
            direction = 'Input',
            datatype= 'DEWorkspace',
            parameterType='Required'
        )
        params = [input_json,output_feature,workspace]
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        input = parameters[0].valueAsText
        output = parameters[1].valueAsText
        workspace = parameters[2].valueAsText
        importJSON(input=input,output=output,workspace=workspace)
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
