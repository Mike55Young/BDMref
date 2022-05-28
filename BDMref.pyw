# NSW BDM Reference Generator for Wikitree
__author__ = "Mike Young"
__Version__ = "1.6"

#
import tkinter as tk
import string
import win32clipboard

outtext = ""

# Constants
nsw_ref = "New South Wales Family History - Births, Deaths and Marriages Search"
nsw_url = "https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search"
vic_ref = "Births Deaths and Marriages Victoria - Family History Search"
vic_url = "https://www.bdm.vic.gov.au/research-and-family-history/search-your-family-history"
qld_ref = "Queensland Government family history research service"
qld_url = "https://www.familyhistory.bdm.qld.gov.au/"

# Element type constants for the HTML parser
START_TAG = 1
END_TAG = 2
DATA = 3

# Functions to read the clipboard
# get the clipboard contents as text
def get_text():
    try:
        win32clipboard.OpenClipboard(0)
        src = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
    finally:
        win32clipboard.CloseClipboard()
    return(src)

# get the clipboard contents as html
def get_html():
    try:
        win32clipboard.OpenClipboard(0)
        html_format = win32clipboard.RegisterClipboardFormat("HTML Format")
        src = win32clipboard.GetClipboardData(html_format)
        # print(src)
    finally:
        win32clipboard.CloseClipboard()
    return(src)

# Handle state selection buttons being pressed
def nsw_panel():
    vic_frame.grid_remove()
    vic_button.config(relief = tk.RAISED)
    qld_frame.grid_remove()
    qld_button.config(relief = tk.RAISED)
    nsw_frame.grid(row=4, column=0)
    nsw_button.config(relief = tk.SUNKEN)
    msg_text.set("")

def vic_panel():
    nsw_frame.grid_remove()
    nsw_button.config(relief = tk.RAISED)
    qld_frame.grid_remove()
    qld_button.config(relief = tk.RAISED)
    vic_frame.grid(row=4, column=0)
    vic_button.config(relief = tk.SUNKEN)
    msg_text.set("")

def qld_panel():
    nsw_frame.grid_remove()
    nsw_button.config(relief = tk.RAISED)
    vic_frame.grid_remove()
    vic_button.config(relief = tk.RAISED)
    qld_frame.grid(row=4, column=0)
    qld_button.config(relief = tk.SUNKEN)
    msg_text.set("")

# Output functions --------------------------
# Copy the generated reference to the clipboard and the output box
def output_reference(out):
    output_text.set(out)
    root.clipboard_clear()
    root.clipboard_append(out)
    msg_text.set("Reference copied to clipboard")

def output_birth(state_ref, state_url, value_dict):
    out = state_ref + " (" + state_url + ") Birth registration # " + value_dict["reg no"]
    out += ", " + value_dict["family name"] + " " + string.capwords(value_dict["given name"])
    out += ", Father: " + string.capwords(value_dict["father"]) + ", Mother: " + string.capwords(value_dict["mother"])
    # Registry may be omitted so allow for that
    if value_dict["date"] != "":
        out += ", Date: " + value_dict["date"]
    if value_dict["district"] != "":
        out += ", Registry: " + string.capwords(value_dict["district"])
    output_reference(out)

def output_death(state_ref, state_url, value_dict):
    out = state_ref + " (" + state_url + ") Death registration # " + value_dict["reg no"]
    out += ", " + value_dict["family name"] + " " +  string.capwords(value_dict["given name"])
    out += ", Father: " + string.capwords(value_dict["father"]) + ", Mother: " + string.capwords(value_dict["mother"])
    if value_dict["date"] != "":
        out += ", Date: " + value_dict["date"]
    if value_dict["age"] != "":
        out += ", Age: " + value_dict["age"]
    if value_dict["location"] != "":
        out += ", Location: " + string.capwords(value_dict["location"])
    if value_dict["location death"] != "":
        out += ", Death Location: " + string.capwords(value_dict["location death"])
    if value_dict["district"] != "":
        out += ", Registry: " + string.capwords(value_dict["district"])
    output_reference(out)

def output_marriage(state_ref, state_url, value_dict):
    out = state_ref + " (" + state_url + ") Marriage registration # " + value_dict["reg no"]
    if value_dict["groom given"] != "":
        out += ", Groom: " + string.capwords(value_dict["groom given"]) + " " + string.capwords(value_dict["groom family"])
        out += ", Bride: " + string.capwords(value_dict["bride given"]) + " " + string.capwords(value_dict["bride family"])
    elif value_dict["family name"] != "":
        out += ", " + value_dict["family name"] + " " + string.capwords(value_dict["given name"])
        out += ", Spouse: " + string.capwords(value_dict["spouse given"]) + " " + string.capwords(value_dict["spouse family"])
    if value_dict["date"] != "":
        out += ", Date: " + value_dict["date"]
    if value_dict["district"] != "":
        out += ", Registry: " + string.capwords(value_dict["district"])
    output_reference(out)

# initialise a dictionary to transfer data from the parsing functions to the output functions
def init_value_dict():
    value_dict = {"family name": "",
                  "given name": "",
                  "event": "",
                  "reg no": "",
                  "father": "",
                  "mother": "",
                  "mother family": "",
                  "district": "",
                  "groom given": "",
                  "groom family": "",
                  "bride given": "",
                  "bride family": "",
                  "spouse given": "",
                  "spouse family": "",
                  "location": "",
                  "location death": "",
                  "date": "",
                  "age": "",
                  "death spouse": ""
                  }
    return value_dict

# Browsers are inconsisten in their handling of text clips from website pseudo tables
# the most reliable way to get the fields into the correct variables is to read the HTML clipboard

# NSW parsing functions
def get_pair(s):
    # extract the part of the wicketpath value from the last underscore to the close quote, and the value between the span tags
    # html has the format <span wicketpath="data_key_name">data_value</span>
    wpath = s.split('"')[1]
    tag_name = wpath.split('_')[-1]
    tag_value = s.split('>')[1]
    return tag_name, tag_value

def parse_nsw_html(clip):
    item_num = ""
    item_year = ""
    item_ref = ""
    value_dict = init_value_dict()
    
    # find the strings starting with <span wicketpath...> and ending in </span>
    i = clip.find("<span wicketpath=")
    while i != -1:
        j = clip.find("</span>", i)
        tag_name, tag_value = get_pair(clip[i:j])
        # set a variable based on the returned name/value pair
        if tag_name == "subjectFamilyName":
            value_dict["family name"] = tag_value
        elif tag_name == "subjectGivenName":
            value_dict["given name"] = tag_value
        elif tag_name == "itemNum":
            item_num = tag_value
        elif tag_name == "itemYear":
            item_year = tag_value
        elif tag_name == "indexRef":
            item_ref = tag_value
        elif tag_name == "fatherName":
            value_dict["father"] = tag_value
        elif tag_name == "motherName":
            value_dict["mother"] = tag_value
        elif tag_name == "district":
            value_dict["district"] = tag_value
        elif tag_name == "groomFamilyName":
            value_dict["groom family"] = tag_value
        elif tag_name == "groomGivenName":
            value_dict["groom given"] = tag_value
        elif tag_name == "brideFamilyName":
            value_dict["bride family"] = tag_value
        elif tag_name == "brideGivenName":
            value_dict["bride given"] = tag_value
        else:
            # just in case there is a field not previously used...
            print(tag_name + "=" + tag_value)
        i = clip.find("<span wicketpath=", j)
    if item_ref != "":
        value_dict["reg no"] = item_num + "/" + item_year + " " + item_ref
    else:
        value_dict["reg no"] = item_num + "/" + item_year
    # return a dictionary of value pairs
    return value_dict

def parse_vic_html(clip):
    value_dict = init_value_dict()
    field_list = []
    # Find strings bounded by <span> </span> and create a list corresponding to the columns on the page
    i = clip.find("<span>")
    while i != -1:
        j = clip.find("</span>", i)
        field_list.append(clip[i+6:j].strip())
        i = clip.find("<span>", j)
    if len(field_list) < 12:
        msg_text.set("Not enough columns copied - expecting 12, got " + str(len(field_list)))
        
    # Now store the columns into the respective dictionary items
    value_dict["family name"] = field_list[0]
    value_dict["given name"] = field_list[1]
    value_dict["event"] = field_list[2]
    # field 3 needs to be split and stored depending on the event type
    name_family, name_given = field_list[3].split(',')
    if value_dict["event"] == "Marriage":
        value_dict["spouse given"] = name_given.strip()
        value_dict["spouse family"] = name_family.strip()
    else:
        value_dict["mother"] = name_given
    value_dict["mother family"] = field_list[4]
    # field 5 needs to be split if it is non-blank
    if field_list[5] != "":
        name_family, name_given = field_list[5].split(',')
        value_dict["father"] = name_given.strip()
    value_dict["location"] = field_list[6]
    value_dict["location death"] = field_list[7]
    if field_list[8] != "<Unknown Family Name>":
        value_dict["death spouse"] = field_list[8]
    value_dict["age"] = field_list[9]
    value_dict["date"] = field_list[10]
    value_dict["reg no"] = field_list[11]
    return value_dict

# handlers for the generate buttons
def gen_nsw_birth():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        return
    value_dict = parse_nsw_html(str(clip))
    # print(value_dict)
    output_birth(nsw_ref, nsw_url, value_dict)

def gen_nsw_death():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        return
    value_dict = parse_nsw_html(str(clip))
    # print(value_dict)
    output_death(nsw_ref, nsw_url, value_dict)

def gen_nsw_marriage():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        return
    value_dict = parse_nsw_html(str(clip))
    # print(value_dict)
    output_marriage(nsw_ref, nsw_url, value_dict)

def gen_vic():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        return
    value_dict = parse_vic_html(clip.decode('utf-8'))
    if value_dict["event"] == "Birth":
        output_birth(vic_ref, vic_url, value_dict)
    elif value_dict["event"] == "Death":
        output_death(vic_ref, vic_url, value_dict)
    elif value_dict["event"] == "Marriage":
        output_marriage(vic_ref, vic_url, value_dict)
    else:
        msg_text.set("Unexpected event type: " + value_dict["event"])
    return

def gen_qld():
    text = get_text().decode('utf-8') + "\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n"
    field_list = text.split('\r\n')
    type_list = field_list[2].split(':')
    reg_type = type_list[1].strip().split(' ')[0]
    # Chrome doesn't see the column separation and combines the Registration number with the Products available field
    # The following code checks for this and adjusts the numbering of subsequent cells
    reg_num = field_list[3].split(':')[1]
    if reg_num[-18:] == "Products available":
        reg_num = reg_num[0:-18]
        o = -1
    else:
        o = 0
    out = qld_ref + " (" + qld_url + ") " + reg_type + " registration #"
    if reg_type == "Birth" or reg_type == "Death":
        out += reg_num + ", " + field_list[0].strip()
        out += ", " + field_list[5 + o].strip()
        out += ", " + field_list[6 + o].strip()
        out += ", " + field_list[1].strip()
    elif reg_type == "Marriage":
        out += reg_num + ", " + field_list[0].strip()
        out += ", " + field_list[5 + o].strip()
        out += ", " + field_list[1].strip()
    else:
        out += "** unknown type =" + reg_type + "."
    output_reference(out)


# Setup the window

root = tk.Tk()

root.title("Wikitree BDM Reference Generator v" + __Version__)
# common data
output_text = tk.StringVar()
msg_text = tk.StringVar()
msg_text.set("Click on a state")

# Message area
msgbox = tk.Label(root, textvariable=msg_text)
msgbox.grid(row=0, column=0)

# Buttons to select State
button_frame = tk.Frame(root)
button_frame.grid(row=1, column=0)
nsw_button = tk.Button(button_frame, text="NSW", command=nsw_panel, width=8)
nsw_button.grid(row=0, column=0, padx=5)
qld_button = tk.Button(button_frame, text="Qld", command=qld_panel, width=8)
qld_button.grid(row=0, column=1, padx=5)
vic_button = tk.Button(button_frame, text="Vic", command=vic_panel, width=8)
vic_button.grid(row=0, column=2, padx=5)
# other states will go here

# NSW frame
nsw_frame = tk.Frame(root)
tk.Label(nsw_frame, text="Copy a row on the browser, then click on the button below that corresponds to the entry type").grid(row=0, column=0, columnspan=3)
tk.Button(nsw_frame, text="Birth", command=gen_nsw_birth, width=15).grid(row=1, column=0, padx=5, pady=3)
tk.Button(nsw_frame, text="Death", command=gen_nsw_death, width=15).grid(row=1, column=1, padx=5, pady=3)
tk.Button(nsw_frame, text="Marriage", command=gen_nsw_marriage, width=15).grid(row=1, column=2, padx=5, pady=3)

# Vic frame
vic_frame = tk.Frame(root)
tk.Label(vic_frame, text="Copy a row on the browser, then click Generate").grid(row=0, column=0)
tk.Button(vic_frame, text="Generate", command=gen_vic).grid(row=1, column=0, padx=5, pady=3)

# Qld frame
qld_frame = tk.Frame(root)
tk.Label(qld_frame, text="Copy a row on the browser, then click Generate").grid(row=0, column=0)
tk.Button(qld_frame, text="Generate", command=gen_qld).grid(row=1, column=0, padx=5, pady=3)

# output area (optional - mostly for debug)
output_box = tk.Label(root, textvariable=output_text, width=70, height=5, wrap=490, justify="left", anchor="nw", relief="sunken")
output_box.grid(row=5, column=0, padx=2, pady=2)

root.mainloop()
