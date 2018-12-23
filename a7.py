import os


def annotationClose(line,annotation):
	line=line.strip()
	if annotation:
		if line.endswith(annotation):
			return True
	return False

def isEmpty(line):
	if not len(line.strip()):
		return True

def isOneAnnotation(line):
	line=line.strip()
	if line.startswith("#") :
		return True
	return False

def isMultiAnnotation(line):
	line=line.strip()
	if line.startswith("\"\"\"") or line.startswith("\'\'\'"):
		return True
	return False

def multiAnnotation(line):
	line=line.strip()
	if line.startswith("\"\"\""):
		return "\"\"\""
	elif line.startswith("\'\'\'"):
		return "\'\'\'"
	else:
		return None

def calcu_code(file_path):

	with open(file_path) as fo:
		lines=fo.readlines()

		annotation=None

		a_count=0
		c_count=0
		e_count=0

		for line in lines:

			"""
			多行注释
			"""
			if annotation:
				if annotationClose(line,annotation):
					a_count+=1
					annotation=None
				elif isEmpty(line):
					e_count+=1
				else:
					a_count+=1

			#空行
			elif isEmpty(line):
				e_count+=1

			#注释
			elif isAnnotation(line):
				a_count+=1
				if isMultiAnnotation(line):
					annotation=multiAnnotation(line)

			else:
				c_count+=1
		return (a_count,c_count,e_count)


def mul_code(file_path):

	code_info={}

	for file_name in os.listdir(file_path):
		filePath=os.path.join(file_path,file_name)
		info=calcu_code(file_path)
		code_info[file_path]={"annotation":info[0],"code":info[1],"empty":info[2]}
	return code_info
		
