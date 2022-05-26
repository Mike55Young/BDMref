# NSW BDM Reference Generator for Wikitree
__author__ = "Mike Young"
__Version__ = "1.6"

#
import tkinter as tk
import string
import win32clipboard

outtext = ""

# Constants
nsw_ref = "New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search) "
vic_ref = "Births Deaths and Marriages Victoria - Family History Search (https://www.bdm.vic.gov.au/research-and-family-history/search-your-family-history) "
qld_ref = " Queensland Government family history research service (https://www.familyhistory.bdm.qld.gov.au/) "

START_TAG = 1
END_TAG = 2
DATA = 3

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

# Function to parse html fragment and store the elements in a list for further analysis
def html_parse(s):
    # List to store the parsed html - each element is itself a list: element_type, tag, element_text
    # element_type can be "start tag", "data" or "end tag"
    # tag is the tag name e.g. "div", "span", "br"
    # element_text is the full text of the element or data (including the <> bits)
    html_list = []
    
    element = ""
    element_type = DATA
    for c in s:
        if c == "<":
            if element_type == DATA:
                if element != "":
                    html_list.append([element_type, "", element])
                    element = ""
                element_type = START_TAG
            element += c
        elif c == "/":
            if element == "<":
                element_type = END_TAG
            element += c
        elif c == ">":
            if element_type == DATA:
                element += c
            else:
                if element_type == START_TAG:
                    tag = element[1:].strip().split(" ")[0]
                else:
                    tag = element[2:].strip().split(" ")[0]
                element += c
                html_list.append([element_type, tag, element])
                element = ""
                element_type = DATA
        else:
            element += c
    return html_list

# handle state selection buttons being pressed
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
    
# Copy the generated reference to the clipboard and the output box
def output_reference(out):
    output_text.set(out)
    root.clipboard_clear()
    root.clipboard_append(out)
    msg_text.set("Reference copied to clipboard")

# Browsers are inconsisten in their handling of text clips from website pseudo tables
# the most reliable way to get the fields into the correct variables is to read the HTML clipboard
def get_pair(s):
    # extract the part of the wicketpath value from the last underscore to the close quote, and the value between the span tags
    # html has the format <span wicketpath="data_key_name">data_value</span>
    wpath = s.split('"')[1]
    tag_name = wpath.split('_')[-1]
    tag_value = s.split('>')[1]
    return tag_name, tag_value

def parse_nsw_html(clip):
    family_name = ""
    given_name = ""
    item_num = ""
    item_year = ""
    item_ref = ""
    father = ""
    mother = ""
    district = ""
    groom_family_name = ""
    groom_given_name = ""
    bride_family_name = ""
    bride_given_name = ""
    
    # find the strings starting with <span wicketpath...> and ending in </span>
    i = clip.find("<span wicketpath=")
    while i != -1:
        j = clip.find("</span>", i)
        tag_name, tag_value = get_pair(clip[i:j])
        # set a variable based on the returned name/value pair
        if tag_name == "subjectFamilyName":
            family_name = tag_value
        elif tag_name == "subjectGivenName":
            given_name = tag_value
        elif tag_name == "itemNum":
            item_num = tag_value
        elif tag_name == "itemYear":
            item_year = tag_value
        elif tag_name == "indexRef":
            item_ref = tag_value
        elif tag_name == "fatherName":
            father = tag_value
        elif tag_name == "motherName":
            mother = tag_value
        elif tag_name == "district":
            district = tag_value
        elif tag_name == "groomFamilyName":
            groom_family_name = tag_value
        elif tag_name == "groomGivenName":
            groom_given_name = tag_value
        elif tag_name == "brideFamilyName":
            bride_family_name = tag_value
        elif tag_name == "brideGivenName":
            bride_given_name = tag_value
        else:
            # just in case there is a field not previously used...
            print(tag_name + "=" + tag_value)
        i = clip.find("<span wicketpath=", i + 1)
    # return a dictionary of value pairs
    if item_ref != "":
        ref = item_num + "/" + item_year + " " + item_ref
    else:
        ref = item_num + "/" + item_year
    value_dict = {"name": family_name + " " + string.capwords(given_name),
                  "ref": ref,
                  "father": string.capwords(father),
                  "mother": string.capwords(mother),
                  "district": string.capwords(district),
                  "groom": string.capwords(groom_given_name + " " + groom_family_name),
                  "bride": string.capwords(bride_given_name + " " + bride_family_name)
                  }
    return value_dict

def gen_nsw_birth():
    clip = get_html()
    if clip == None:
        out = "Unable to read HTML clipboard"
        return
    value_dict = parse_nsw_html(str(clip))
    # print(value_dict)
    out = nsw_ref + "Birth registration # " + value_dict["ref"]
    out += ", " + value_dict["name"]
    out += ", Father: " + value_dict["father"] + ", Mother: " + value_dict["mother"]
    # Registry may be omitted so allow for that
    if value_dict["district"] != "":
        out += ", Registry: " + value_dict["district"]
    output_reference(out)

def gen_nsw_death():
    clip = get_html()
    if clip == None:
        out = "Unable to read HTML clipboard"
        return
    value_dict = parse_nsw_html(str(clip))
    # print(value_dict)
    out = nsw_ref + "Death registration # " + value_dict["ref"]
    out += ", " + value_dict["name"]
    out += ", Father: " + value_dict["father"] + ", Mother: " + value_dict["mother"]
    # Registry may be omitted so allow for that
    if value_dict["district"] != "":
        out += ", Registry: " + value_dict["district"]
    output_reference(out)

def gen_nsw_marriage():
    clip = get_html()
    if clip == None:
        out = "Unable to read HTML clipboard"
        return
    value_dict = parse_nsw_html(str(clip))
    # print(value_dict)
    out = nsw_ref + "Marriage registration # " + value_dict["ref"]
    out += ", Groom: " + value_dict["groom"] + ", Bride: " + value_dict["bride"]
    # Registry may be omitted so allow for that
    if value_dict["district"] != "":
        out += ", Registry: " + value_dict["district"]
    output_reference(out)

def gen_vic():
    text = get_text().decode('utf-8') + "\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n"
    field_list = text.split('\r\n')
    # allow for browser differences
    if field_list[0] == '':
        o = 1
    else:
        o = 0
    name1_list = field_list[3 + o].split(',')
    reg_type = field_list[2 + o]
    out = vic_ref + reg_type + " registration # "
    if reg_type == "Birth":
        name2_list = field_list[5 + o].split(',')
        out += field_list[8 + o] + ", " + field_list[1 + o] + " " + field_list[o]
        out += ", Mother: " + name1_list[1] + " " + field_list[4 + o]
        out += ", Father: " + name2_list[1]
        out += ", Location: " + field_list[6 + o]
    elif reg_type == "Marriage":
        out += field_list[6 + o] + ", Groom: " + field_list[1 + o] + " " + field_list[o]
        out += ", Bride: " + name1_list[1] + " " + name1_list[0]
    elif reg_type == "Death":
        name2_list = field_list[5 + o].split(',')
        out += field_list[10 + o] + ", " + field_list[1 + o] + " " + field_list[o]
        out += ", Mother: " + name1_list[1] + " " + field_list[4 + o]
        out += ", Father: " + name2_list[1]
        if field_list[7] != "":
            out += ", Location: " + field_list[6 + o]
        if field_list[9] != "":
            out += ", Age: " + field_list[8 + o]
    output_reference(out)

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
    out = qld_ref + reg_type + " registration #"
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
