import json
import os
import sys
import re


def check_user():
	if os.getuid() != 0:
		print("Permission Denied\nRun as Super User")
		sys.exit()

def read_conf(conf):
	with open(conf, 'r') as conf_file:
		data = conf_file.read()

	obj = json.loads(data)
	return obj


def get_app_name(obj):
	return obj["app_name"]


def search_running_app(app):
	command = "ps -ef | grep "+str(app) + " > temp.txt"
	os.system(command)

	f = open("temp.txt" , 'r')
	data = f.read().split("\n")
	f.close()

	p_ip = []
	for line in data:
		if re.findall(command , line):
			continue
		elif re.findall("grep "+str(app), line):
			continue
		elif(len(line.split()) > 0):
			p_ip.append(line.split()[1])

	return p_ip


def kill_app(pId):
	val = -1
	if len(pId) > 0:
		command = "sudo kill -9 "
		for id in pId:
			command = command + str(id) +" "

		val = os.system(command)
	return val


def statement(res):
	if res == 0:
		print("App Name:", app)
		print("Program ID(s):", pId)
		print("Program killed Successfully")
	elif res == -1:
		print(app, "is not currently running")
	else:
		print("Someting error happed")


def clean():
	if os.path.exists("temp.txt"):
		os.remove("temp.txt")


def tutorial():
	print("\n\nChange the appication name in the 'setting.json' file to kill your own program\n")


if __name__ == "__main__":
	conf_file = "settings.json"
	check_user()
	obj = read_conf(conf_file)
	app = get_app_name(obj)
	pId = search_running_app(app)
	res = kill_app(pId)

	statement(res)
	clean()

	tutorial()

