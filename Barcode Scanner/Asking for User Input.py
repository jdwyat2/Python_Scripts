import time

while True:
	filename = "G:\Current Desktop\Scripts\Barcode Scanner\Test.txt"
	person = raw_input("Patient ID: ")
	room = raw_input("Room: ")
	time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time()))
	print person + ","+room+","+"\n"
	print time
	raw_input("stop")

	file = open(filename,"w")
	file.write(person+","+room+","+time+"\n")

	