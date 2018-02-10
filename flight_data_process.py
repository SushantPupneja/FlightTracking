import os
import time
import json
import pandas as pd
path = "/home/ashok/Desktop/flightTracking"

# flight info will be stored in the form of key followed by a panda dataframe
flight_info_stack = {}

columns = ['hex', 'squawk', 'flight', 'lat', 'lon', 'nucp', 'seen_pos', 'altitude', 'vert_rate', 'track', 
'speed', 'messages', 'seen', 'rssi'] # columns for dataframe's to be created for each flight

def get_row(line):
	row = []
	for column in columns:
		try:
			row.append(line[column])
		except:
			row.append('')
	return row

	# [line['hex'], line['squawk'], line['flight'], line['mlat'], line['lon'], line['nucp'], line['seen_pos'],
	# 		line['altitude'], line['vert_rate'], line['track'], line['speed'], line['messages'], line['seen'],
	# 		line['rssi']]
def process_chunk(chunk):
	#get each line from chunk
	for line in chunk:
		print line["hex"]
		if line["hex"] not in flight_info_stack.keys():
			flight_info_stack[line["hex"]] = pd.DataFrame(columns=columns)

		if line["hex"] in flight_info_stack.keys():
			frame = flight_info_stack[line["hex"]]
			#create row for dataframe for this flight
			row = get_row(line)
			#add row in dataframe for this flight
			frame.loc[len(frame)] = row



#method to process data from file 
def process_file_data(filename):
	#read data from file
	print ("processing file ....... {}".format(filename))
	with open(filename, "r") as file_data:
		for chunks in file_data:
			flights_info = json.loads(chunks)
			chunk = flights_info["aircraft"]
			process_chunk(chunk)
			# print flight_info_stack



if __name__ == "__main__":
	#get files to process data
	list_files = os.listdir(path)
	if list_files:
		for file_name in list_files:
			#search  for data file in files with .json extension
			if ".json" in file_name and ".gz" not in file_name:
				#send file for processing
				print file_name
				process_file_data(file_name)
				break
		with open('flight_info.txt', 'a') as flight_info:
			flights_data = {}
			for key in flight_info_stack.keys():
				frame = flight_info_stack[key]
				flight_tracking_data =  frame.to_dict(orient="records")
				flights_data[key] = flight_tracking_data
			flight_info.write(json.dumps(flights_data))

	else:
		print("no files found to process ... exiting")