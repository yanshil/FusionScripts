#Author-yanshil
#Description-Modified from 'Get Physical Properties API Sample API Sample' BELOW
#Reference-https://help.autodesk.com/view/fusion360/ENU/?guid=GUID-ce341ee6-4490-11e5-b25b-f8b156d7cd97
import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        result = ''
        for selection in ui.activeSelections:
            selectedEnt = selection.entity
            if selectedEnt.objectType == adsk.fusion.Occurrence.classType() or selectedEnt.objectType == adsk.fusion.Component.classType():
                physicalProperties = selectedEnt.physicalProperties
                # Parameter Option: adsk.fusion.CalculationAccuracy.LowCalculationAccuracy, MediumCalculationAccuracy, HighCalculationAccuracym VeryHighCalculationAccuracy
                # Get data from physical properties
                area = physicalProperties.area
                density = physicalProperties.density
                mass = physicalProperties.mass
                volume = physicalProperties.volume
                
                # Get accuracy from physical properties
                accuracy = physicalProperties.accuracy

                # Get center of mass from physical properties
                cog = physicalProperties.centerOfMass

                # Get principal axes from physical properties
                (retVal, xAxis0, yAxis0, zAxis0) = physicalProperties.getPrincipalAxes()
                
                # Get the moments of inertia about the principal axes. Unit for returned values is kg/cm^2.
                (retVal,i1,i2,i3) = physicalProperties.getPrincipalMomentsOfInertia()
                ### TODO: NOTE: Problem is, IDK what exactly these 3 values are???
                ### They are neither MOI on World frame or COM frame.....

                # Get the radius of gyration about the principal axes. Unit for returned values is cm.
                (retVal, kx, ky, kz) = physicalProperties.getRadiusOfGyration()

                # Get the rotation from the world coordinate system of the target to the principal coordinate system.
                (retVal, rx, ry, rz) = physicalProperties.getRotationToPrincipal()

                # Get the moment of inertia about the world coordinate system.
                (retVal, xx, yy, zz, xy, yz, xz) = physicalProperties.getXYZMomentsOfInertia()

                result += 'Mass (kg) = {:4.3f}\n'.format(mass)
                result += 'MOI about Principal Axes (kg/cm^2)\n\ti1 = {:4.3f}, i2 = {:4.3f}, i3 = {:4.3f}\n'.format(i1, i2, i3)
                ui.messageBox(result, 'Selected Body: {}'.format(selectedEnt.name))
            else:
                result += 'Selected Object Type DO NOT support Physical Properties: ' + selectedEnt.objectType + '\n'
                ui.messageBox(result, 'Selection Result')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))