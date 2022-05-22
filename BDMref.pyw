# NSW BDM Reference Generator for Wikitree
# Author: Mike Young
#
import tkinter as tk
#import os
#from itertools import permutations
import string

# window size
# HEIGHT = 500
# WIDTH = 600

outtext = ""

# Constants
nsw_ref = "New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search) "
vic_ref = "Births Deaths and Marriages Victoria - Family History Search (https://www.bdm.vic.gov.au/research-and-family-history/search-your-family-history) "
#month_list = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#day_list = range(1, 32)
#ref_type_text = ""

# NSW Sample (Birth/Death) - name, reg no, father, mother, registry:
# DUNK BENJAMIN T
# 3063/1859 
# WILLIAM
# ELIZA
# CHIPPENDALE

# Vic Sample - surname, given names, rec type, mother, mother birth name, father, place, year, reg no:
# STANLAKE
# Eveline Amelia
# Birth
# <Unknown Family Name>, Amelia Tredwen
# PARDY
# <Unknown Family Name>, Charles
# CA RL
# 1878
# 1104/1878

# handle state buttons
def nsw_panel():
    vic_frame.grid_remove()
    nsw_frame.grid(row=4, column=0)

def vic_panel():
    nsw_frame.grid_remove()
    vic_frame.grid(row=4, column=0)

# Generate reference
def output_reference(out):
    output_text.set(out)
    root.clipboard_clear()
    root.clipboard_append(out)
    msg_text.set("Reference copied to clipboard")
    input_text.set("")

def gen_nsw_birth():
    text = input_text.get() + "\n\n\n\n"
    field_list = text.split('\n')
    name = field_list[0].strip()
    name_list = name.split(" ", 1)
    # print(field_list)
    out = nsw_ref + "Birth registration # " + field_list[1].strip() + ", " + name_list[0] + " " + string.capwords(name_list[1])
    out += ", Father: " + string.capwords(field_list[2]) + ", Mother: " + string.capwords(field_list[3])
    # Registry may be omitted so allow for that
    if field_list[4] != "":
        out += ", Registry: " + string.capwords(field_list[4])
    output_reference(out)

def gen_nsw_death():
    text = input_text.get() + "\n\n\n\n"
    field_list = text.split('\n')
    name = field_list[0].strip()
    name_list = name.split(" ", 1)
    # print(field_list)
    out = nsw_ref + "Death registration # " + field_list[1].strip() + ", " + name_list[0] + " " + string.capwords(name_list[1])
    out += ", Father: " + string.capwords(field_list[2]) + ", Mother: " + string.capwords(field_list[3])
    # Registry may be omitted so allow for that
    if field_list[4] != "":
        out += ", Registry: " + string.capwords(field_list[4])
    output_reference(out)

def gen_nsw_marriage():
    text = input_text.get() + "\n\n\n\n"
    field_list = text.split('\n')
    name = field_list[0].strip()
    name_list = name.split(" ", 1)
    # print(field_list)
    out = nsw_ref + "Marriage registration # " + field_list[0].strip()
    out += ", Groom: " + string.capwords(field_list[2]) + " " + string.capwords(field_list[1])
    out += ", Bride: " + string.capwords(field_list[4]) + " " + string.capwords(field_list[3])
    # Registry may be omitted so allow for that
    if field_list[5] != "":
        out += ", Registry: " + string.capwords(field_list[5])
    output_reference(out)

def gen_vic():
    text = input_text.get() + "\n\n\n\n\n\n"
    field_list = text.split('\n')
    name1_list = field_list[4].split(',')
    print(field_list)
    reg_type = field_list[3]
    out = vic_ref + reg_type + " registration # "
    if reg_type == "Birth":
        name2_list = field_list[6].split(',')
        out += field_list[9] + ", " + field_list[2] + " " + field_list[1]
        out += ", Mother: " + name1_list[1] + " " + field_list[5]
        out += ", Father: " + name2_list[1]
        out += ", Location: " + field_list[7]
    elif reg_type == "Marriage":
        out += field_list[7] + ", Groom: " + field_list[2] + " " + field_list[1]
        out += ", Bride: " + name1_list[1] + " " + name1_list[0]
    elif reg_type == "Death":
        name2_list = field_list[6].split(',')
        out += field_list[11] + ", " + field_list[2] + " " + field_list[1]
        out += ", Mother: " + name1_list[1] + " " + field_list[5]
        out += ", Father: " + name2_list[1]
        if field_list[7] != "":
            out += ", Location: " + field_list[7]
        if field_list[9] != "":
            out += ", Age: " + field_list[9]
    output_reference(out)


# Setup the window

root = tk.Tk()

root.title("Wikitree BDM Reference Generator")
# common data
output_text = tk.StringVar()
msg_text = tk.StringVar()
msg_text.set("Click on a state")
input_text = tk.StringVar()

#canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
#canvas.pack()

# Message area
msgbox = tk.Label(root, textvariable=msg_text)
msgbox.grid(row=0, column=0)

# Buttons to select State
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0)
tk.Button(button_frame, text="NSW", command=nsw_panel, width=8).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Vic", command=vic_panel, width=8).grid(row=0, column=1, padx=5)
# other states will go here

# Box for pasted text
tk.Label(root, text="Paste row from BDM website here").grid(row=2, column=0)
input_box = tk.Entry(root, textvariable=input_text, width=70)
input_box.grid(row=3, column=0, pady=3)

# NSW frame
nsw_frame = tk.Frame(root)
tk.Button(nsw_frame, text="Birth", command=gen_nsw_birth, width=15).grid(row=0, column=0, padx=5, pady=3)
tk.Button(nsw_frame, text="Death", command=gen_nsw_death, width=15).grid(row=0, column=1, padx=5, pady=3)
tk.Button(nsw_frame, text="Marriage", command=gen_nsw_marriage, width=15).grid(row=0, column=2, padx=5, pady=3)

# Vic frame
vic_frame = tk.Frame(root)
tk.Button(vic_frame, text="Generate", command=gen_vic).grid(row=0, column=0, padx=5, pady=3)

# output area (optional - mostly for debug)
output_box = tk.Label(root, textvariable=output_text, width=70, height=5, wrap=490, justify="left", anchor="nw", relief="sunken")
output_box.grid(row=5, column=0, padx=2, pady=2)

root.mainloop()
