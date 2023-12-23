import os
from datetime import datetime
import sys
now = datetime.today().strftime('%Y-%m-%d')

def change_extension(filename, new_extension):
    parts = filename.split('.')
    name_without_extension = '.'.join(parts[:-1])
    new_filename = f"{name_without_extension}.{new_extension}"
    return new_filename


if os.name=="nt":
	shell=0
else:
	shell=1

def clear():
	match shell:
		case 0:
			os.system("cls")
		case 1:
			os.system("clear")

def main():
	clear()
	print("Jumper Level Converter Tool\n")

	if len(sys.argv) > 1:
		fname = sys.argv[1]
	else:
		print("Please provide a path:")
		fname = input(f"{os.getcwd()}> ")

	with open(fname, "r") as jlevel:
		lvl = jlevel.readlines()

	x = 0
	y = 0
	newstr = f"/* created at {now}, from {fname}, using python. */"

	for line in lvl:
	    for char in line.strip():  # This will iterate over each character in the line
	        case = char
	        if case == "B":
	            newstr += f"instance_create({x},{y},ObjBrick); "
	        elif case == "A" or case == "a":
	            newstr += ""
	        elif case == "c":
	            newstr += f"instance_create({x},{y},ObjCoin); "
	        elif case == "C":
	            newstr += f"instance_create({x},{y},ObjBluCoin); "
	        elif case == "b":
	            newstr += f"instance_create({x},{y},ObjCrate); "
	        elif case == "J":
	            newstr += f"instance_create({x},{y},ObjJumper); "
	        elif case == "F":
	            newstr += f"instance_create({x},{y},ObjFlag); "
	        elif case == "×":
	            newstr += f"instance_create({x},{y},ObjSpikes); "
	        elif case == "m":
	            newstr += f"instance_create({x},{y},ObjMachineGunner); "
	        elif case == "l":
	            newstr += f"instance_create({x},{y},obj_lazergunner); "
	        elif case == "s":
	            newstr += f"instance_create({x},{y},ObjSiren); "
	        elif case == "t":
	            newstr += f"instance_create({x},{y},obj_attackmite_turret); "
	        elif case == "+":
	            newstr += f"instance_create({x},{y},ObjHealthKit); "

	        x += 32
	    y += 32
	    x = 0  # Reset x for the next row


	print(f" Created: {newstr}")
	sname = change_extension(fname,"JumperMap")

	with open(sname,"w") as sfile:
		sfile.write(newstr)

	print(f"\ninput : {fname} | output : {sname} \n\n")
	print("Done...")

main()
