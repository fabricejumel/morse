import GameLogic

""" Generic Python Module to be called by all MORSE components.
	It will locate the calling object in the dictionary,
	retrieve the stored instance and call its 'action' method. """

def robot_action(contr):
	""" Call the 'action' method of the correct robot. """
	obj = contr.owner

	# Get the intance of this objects class
	robot_object = GameLogic.robotDict[obj]
	robot_object.action()


def sensor_action(contr):
	""" Call the 'action' method of the correct sensor. """
	obj = contr.owner
	parent = obj.parent
	
	# Get the intance of this objects class
	sensor_object = GameLogic.componentDict[obj]
	sensor_object.action()
	
def actuator_action(contr):
	""" Call the 'action' method of the correct actuator. """
	obj = contr.owner
	parent = obj.parent
	
	# Get the intance of this objects class
	actuator_object = GameLogic.componentDict[obj]
	actuator_object.action()
