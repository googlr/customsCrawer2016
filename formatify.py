import sys

file = open("2016MayResult_001.txt","r")
html = file.readlines()

result = open("2016MayResult_003.txt","w")


for line in html:
	new_line = line.strip()
	if len(new_line) == 0:
		print ""
		result.write("\n")
	else:
		line_data = new_line.replace(',','') + ","
		sys.stdout.write( line_data )
		sys.stdout.flush()
		#print line.strip()
		result.write( line_data )
	

file.close()
