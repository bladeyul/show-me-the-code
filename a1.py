import uuid

def createUID(count):
	UIDs=[]
	for i in range(count):
		UIDs.append(uuid.uuid4())
	return UIDs



