def word():
		file_name = input ("name you file ")
		print ("opening " + file_name)
		f= open(file_name + ".txt","a+")
		content = input ("type \n")
		f.write(content + "\n")
		print (content)
		f.close()