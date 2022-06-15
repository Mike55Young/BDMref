# NSW BDM Reference Generator for Wikitree
__author__ = "Mike Young"
__Version__ = "1.9"

#
import tkinter as tk
import string
import win32clipboard

outtext = ""

# Constants
nsw_ref = "New South Wales Family History - Births, Deaths and Marriages Search"
nsw_url = "https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search"
qld_ref = "Queensland Government family history research service"
qld_url = "https://www.familyhistory.bdm.qld.gov.au/"
sa_ref = "Genealogy South Australia - Online Database Search"
sa_url = "https://www.genealogysa.org.au/resources/online-database-search"
vic_ref = "Births Deaths and Marriages Victoria - Family History Search"
vic_url = "https://www.bdm.vic.gov.au/research-and-family-history/search-your-family-history"
wa_ref = "Western Australia Department of Justice - Online Index Search"
wa_url = "https://www.wa.gov.au/organisation/department-of-justice/online-index-search-tool"

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
    finally:
        win32clipboard.CloseClipboard()
    return(src)

# Handle state selection buttons being pressed
def nsw_panel():
    nsw_frame.grid(row=4, column=0)
    nsw_button.config(relief = tk.SUNKEN)
    qld_frame.grid_remove()
    qld_button.config(relief = tk.RAISED)
    sa_frame.grid_remove()
    sa_button.config(relief = tk.RAISED)
    vic_frame.grid_remove()
    vic_button.config(relief = tk.RAISED)
    wa_frame.grid_remove()
    wa_button.config(relief = tk.RAISED)
    msg_text.set("")

def qld_panel():
    nsw_frame.grid_remove()
    nsw_button.config(relief = tk.RAISED)
    qld_frame.grid(row=4, column=0)
    qld_button.config(relief = tk.SUNKEN)
    sa_frame.grid_remove()
    sa_button.config(relief = tk.RAISED)
    vic_frame.grid_remove()
    vic_button.config(relief = tk.RAISED)
    wa_frame.grid_remove()
    wa_button.config(relief = tk.RAISED)
    msg_text.set("")

def sa_panel():
    nsw_frame.grid_remove()
    nsw_button.config(relief = tk.RAISED)
    qld_frame.grid_remove()
    qld_button.config(relief = tk.RAISED)
    sa_frame.grid(row=4, column=0)
    sa_button.config(relief = tk.SUNKEN)
    vic_frame.grid_remove()
    vic_button.config(relief = tk.RAISED)
    wa_frame.grid_remove()
    wa_button.config(relief = tk.RAISED)
    msg_text.set("")

def vic_panel():
    nsw_frame.grid_remove()
    nsw_button.config(relief = tk.RAISED)
    qld_frame.grid_remove()
    qld_button.config(relief = tk.RAISED)
    sa_frame.grid_remove()
    sa_button.config(relief = tk.RAISED)
    vic_frame.grid(row=4, column=0)
    vic_button.config(relief = tk.SUNKEN)
    wa_frame.grid_remove()
    wa_button.config(relief = tk.RAISED)
    msg_text.set("")

def wa_panel():
    nsw_frame.grid_remove()
    nsw_button.config(relief = tk.RAISED)
    qld_frame.grid_remove()
    qld_button.config(relief = tk.RAISED)
    sa_frame.grid_remove()
    sa_button.config(relief = tk.RAISED)
    vic_frame.grid_remove()
    vic_button.config(relief = tk.RAISED)
    wa_frame.grid(row=4, column=0)
    wa_button.config(relief = tk.SUNKEN)
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
    if value_dict["name"] != "":
        out += ", " + value_dict["name"]
    else:
        out += ", " + value_dict["family name"] + " " +  string.capwords(value_dict["given name"])
    if value_dict["gender"] != "":
        out += ", Gender: " + value_dict["gender"] 
    if value_dict["father"] != "":
        out += ", Father: " + string.capwords(value_dict["father"]) 
    if value_dict["mother"] != "":
        out += ", Mother: " + string.capwords(value_dict["mother"])
    if value_dict["parent"] != "":
        out += ", Father/parent: " + string.capwords(value_dict["parent"]) 
    if value_dict["mother family"] != "":
        out += " " + value_dict["mother family"]
    if value_dict["date"] != "":
        out += ", Date: " + value_dict["date"]
    if value_dict["location birth"] != "":
        out += ", Birth Location: " + value_dict["location birth"]
    if value_dict["district"] != "":
        out += ", Registry: " + string.capwords(value_dict["district"])
    output_reference(out)

def output_death(state_ref, state_url, value_dict):
    out = state_ref + " (" + state_url + ") Death registration # " + value_dict["reg no"]
    if value_dict["name"] != "":
        out += ", " + value_dict["name"]
    else:
        out += ", " + value_dict["family name"] + " " +  string.capwords(value_dict["given name"])
    if value_dict["gender"] != "":
        out += ", Gender: " + value_dict["gender"] 
    if value_dict["father"] != "":
        out += ", Father: " + string.capwords(value_dict["father"]) 
    if value_dict["mother"] != "":
        out += ", Mother: " + string.capwords(value_dict["mother"])
    if value_dict["parent"] != "":
        out += ", Father/parent: " + string.capwords(value_dict["parent"]) 
    if value_dict["mother family"] != "":
        out += " " + value_dict["mother family"]
    if value_dict["date"] != "":
        out += ", Date: " + value_dict["date"]
    if value_dict["age"] != "":
        out += ", Age: " + value_dict["age"]
    if value_dict["dob"] != "":
        out += ", Date of Birth: " + value_dict["dob"]
    if value_dict["location birth"] != "":
        out += ", Birth Location: " + value_dict["location birth"]
    if value_dict["location death"] != "":
        out += ", Death Location: " + value_dict["location death"]
    if value_dict["district"] != "":
        out += ", Registry: " + string.capwords(value_dict["district"])
    output_reference(out)

def output_marriage(state_ref, state_url, value_dict):
    out = state_ref + " (" + state_url + ") Marriage registration # " + value_dict["reg no"]
    if value_dict["groom given"] != "":
        out += ", Groom: " + string.capwords(value_dict["groom given"]) + " " + string.capwords(value_dict["groom family"])
        out += ", Bride: " + string.capwords(value_dict["bride given"]) + " " + string.capwords(value_dict["bride family"])
    elif value_dict["name"] != "":
        out += ", " + value_dict["name"]
    elif value_dict["family name"] != "":
        out += ", " + value_dict["family name"] + " " + string.capwords(value_dict["given name"])
        if value_dict["gender"] != "":
            out += ", Gender: " + value_dict["gender"]
        out += ", Spouse: " + string.capwords(value_dict["spouse given"]) + " " + string.capwords(value_dict["spouse family"])
    if value_dict["spouse"] != "":
        out += ", Spouse: " + string.capwords(value_dict["spouse"])
    if value_dict["spouse gender"] != "":
        out += ", Spouse gender: " + string.capwords(value_dict["spouse gender"])
    if value_dict["date"] != "":
        out += ", Date: " + value_dict["date"]
    if value_dict["location"] != "":
        out += ", Marriage Location: " + value_dict["location"]
    if value_dict["district"] != "":
        out += ", Registry: " + string.capwords(value_dict["district"])
    output_reference(out)

# initialise a dictionary to transfer data from the parsing functions to the output functions
def init_value_dict():
    value_dict = {"family name": "",
                  "given name": "",
                  "name": "",
                  "gender": "",
                  "event": "",
                  "reg no": "",
                  "father": "",
                  "mother": "",
                  "parent": "",
                  "mother family": "",
                  "district": "",
                  "groom given": "",
                  "groom family": "",
                  "bride given": "",
                  "bride family": "",
                  "spouse given": "",
                  "spouse family": "",
                  "spouse": "",
                  "spouse gender": "",
                  "location": "",
                  "location birth": "",
                  "location death": "",
                  "date": "",
                  "dob": "",
                  "age": "",
                  "death spouse": ""
                  }
    return value_dict

# Browsers are inconsisten in their handling of text clips from website pseudo tables
# the most reliable way to get the fields into the correct variables is to read the HTML clipboard

# find the next occurrence of a specified tag (or just the next tag if the name is null)
def get_tag(clip, tag_prefix, p):
    tag_suffix = ""
    s = "<" + tag_prefix
    i = clip.find(s, p)
    if i >= 0:
        i += 1
        j = clip.find(">", i)
        tag_text = clip[i:j]
        if tag_prefix == "":
            tag_prefix, tag_suffix = tag_text.split(" ",1)
        else:
            tag_suffix = tag_text[len(tag_prefix):]
        i = j + 1
    return i, tag_prefix, tag_suffix

# NSW parsing functions
def get_key(s):
    # extract the part of the wicketpath value from the last underscore to the close quote
    # html has the format <span wicketpath="data_key_name">
    wpath = s.split('"')[1]
    return wpath.split('_')[-1]

def parse_nsw_html(clip):
    item_num = ""
    item_year = ""
    item_ref = ""
    value_dict = init_value_dict()
    
    # find the strings starting with <span wicketpath...> and ending in </span>
    i, tag_prefix, tag_suffix = get_tag(clip, "span wicketpath=", 0)
    while i >= 0:
        tag_name = get_key(tag_suffix)
        j = clip.find("</span>", i)
        tag_value = clip[i:j]
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
        i, tag_prefix, tag_suffix = get_tag(clip, "span wicketpath=", j)
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
    i = clip.find("<span")
    while i != -1:
        i = clip.find(">", i)
        j = clip.find("</span>", i)
        field_list.append(clip[i+1:j].strip())
        i = clip.find("<span", j)
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
    value_dict["location birth"] = field_list[6]
    value_dict["location death"] = field_list[7]
    if field_list[8] != "<Unknown Family Name>":
        value_dict["death spouse"] = field_list[8]
    value_dict["age"] = field_list[9]
    value_dict["date"] = field_list[10]
    value_dict["reg no"] = field_list[11]
    return value_dict

def parse_qld_html(clip):
    value_dict = init_value_dict()
    i = clip.find('<a class="recordlink"')
    i = clip.find('href=', i + 20)
    q = clip[i + 5]
    j = clip.find(q, i + 6)
    value_dict.update({"url": clip[i + 6:j]})
    i = clip.find(">", j)
    j = clip.find("<", i)
    value_dict["name"] = clip[i + 1:j].strip()
    i = clip.find("<br>", j)
    while i != -1:
        i += 4
        j = clip.find("<", i)
        field_type, field_value = clip[i:j].strip().split(":")
        if field_type == "Event date":
            value_dict["date"] = field_value.strip()
        elif field_type == "Event type":
            value_dict["event"] = field_value.strip().split(" ")[0]
        elif field_type == "Registration details":
            value_dict["reg no"] = field_value.strip()
        elif field_type == "Mother":
            value_dict["mother"] = field_value.strip()
        elif field_type == "Father/parent":
            value_dict["parent"] = field_value.strip()
        elif field_type == "Date of birth":
            value_dict["dob"] = field_value.strip()
        elif field_type == "Spouse":
            value_dict["spouse"] = field_value.strip()
        else:
            msg_text.set("Unknown type: " + field_type)
        i = clip.find("<br>", j)
    return value_dict
 
def parse_sa_html(clip):
    value_dict = init_value_dict()
    field_list = []
    # Find strings bounded by <td class=""> </td> and create a list corresponding to the columns on the page
    i = clip.find('<td class="">')
    while i != -1:
        i += len('<td class="">')
        j = clip.find("</td>", i)
        field_list.append(clip[i:j].strip())
        i = clip.find('<td class="">', j)
    if len(field_list) < 6:
        msg_text.set("Should be at least 6 columns but found " + str(len(field_list)))
        return value_dict
    # Now work out what record type we have.
    # If View Details is the last field copied we can find the type in there.
    if field_list[-1][0:1] == '<a':
        i = field_list[-1].find("coid=") + 5
        j = field_list[-1].find("&", i)
        value_dict["event"] = string.capwords(field_list[-1][i:j])
        field_list = field_list[:-2]
    elif len(field_list) == 6:
        value_dict["event"] = "Death"
    elif len(field_list) == 7:
        if field_list[2] == 'M' or field_list[2] == 'F':
            value_dict["event"] = "Birth"
        else:
            value_dict["event"] = "Marriage"
    else:
        msg_text.set("Should be 6 or 7 columns (excluding View Details) but found " + str(len(field_list)))
        
    # Now store the columns into the respective dictionary items
    if value_dict["event"] == "Marriage":
        if field_list[0].find("(members only)") > 0:
            value_dict["groom family"] = '(members only)'
        else:    
            value_dict["groom family"] = field_list[0]
        value_dict["groom given"] = field_list[1]
        if field_list[2].find("(members only)") > 0:
            value_dict["bride family"] = '(members only)'
        else:    
            value_dict["bride family"] = field_list[2]
        value_dict["bride given"] = field_list[3]
    else:
        value_dict["family name"] = field_list[0]
        value_dict["given name"] = field_list[1]
        value_dict["gender"] = field_list[2]
        if value_dict["event"] == "Birth":
            value_dict["father"] = field_list[3]
    # Last 3 are always district, book/page and year
    value_dict["district"] = field_list[-3]
    value_dict["reg no"] = field_list[-2]
    value_dict["date"] = field_list[-1]
    return value_dict

def parse_wa_html(clip):
    value_dict = init_value_dict()
    field_list = []
    # Find strings bounded by <td ...> </td>
    # The opening td contains an attribute with prefix cdk-column- that indicates the data type
    i = clip.find("<td")
    while i != -1:
        i = clip.find("cdk-column-", i) + len("cdk-column-")
        j = clip.find(" ", i)
        field_type = clip[i:j]
        i = clip.find(">", j)
        j = clip.find("</td>", i)
        field_value = clip[i + 1:j].strip()
        if field_type == "surname":
            value_dict["family name"] = field_value
        elif field_type == "givenNames":
            value_dict["given name"] = field_value
        elif field_type == "gender" or field_type == "gender01":
            value_dict["gender"] = field_value
        elif field_type == "father":
            value_dict["father"] = field_value
        elif field_type == "mother":
            value_dict["mother"] = field_value
        elif field_type == "birthPlace":
            value_dict["location birth"] = field_value
            value_dict["event"] = "Birth"
        elif field_type == "deathPlace":
            # this is actually the birth location as shown on the website column heading (verified with a known overseas birth)
            value_dict["location birth"] = field_value
            value_dict["event"] = "Death"
        elif field_type == "marriagePlace":
            value_dict["location"] = field_value
            value_dict["event"] = "Marriage"
        elif field_type == "yearOfBirth" or field_type == "yearOfDeath" or field_type == "yearOfMarriage":
            value_dict["date"] = field_value
        elif field_type == "age":
            value_dict["age"] = field_value
        elif field_type == "spouseSurname":
            value_dict["spouse family"] = field_value
        elif field_type == "spouseGivenNames":
            value_dict["spouse given"] = field_value
        elif field_type == "gender02":
            value_dict["spouse gender"] = field_value
        elif field_type == "registrationDistrict":
            value_dict["district"] = field_value
        elif field_type == "registrationNumber":
            reg_no = field_value
        elif field_type == "registrationYear":
            reg_year = field_value
        else:
            msg_text.set("Unknown type: " + field_type)
        i = clip.find("<td", j)
    value_dict["reg no"] = reg_no + "/" + reg_year
    return value_dict

# handlers for the generate buttons
def gen_nsw_birth():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        output_text.set("")
        return
    value_dict = parse_nsw_html(str(clip))
    # print(value_dict)
    output_birth(nsw_ref, nsw_url, value_dict)

def gen_nsw_death():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        output_text.set("")
        return
    value_dict = parse_nsw_html(str(clip))
    # print(value_dict)
    output_death(nsw_ref, nsw_url, value_dict)

def gen_nsw_marriage():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        output_text.set("")
        return
    value_dict = parse_nsw_html(str(clip))
    # print(value_dict)
    output_marriage(nsw_ref, nsw_url, value_dict)

def gen_vic():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        output_text.set("")
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
        output_text.set("")
    return

def gen_qld():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        output_text.set("")
        return
    value_dict = parse_qld_html(clip.decode('utf-8'))
    qld_url = value_dict["url"]
    if value_dict["event"] == "Birth":
        output_birth(qld_ref, qld_url, value_dict)
    elif value_dict["event"] == "Death":
        output_death(qld_ref, qld_url, value_dict)
    elif value_dict["event"] == "Marriage":
        output_marriage(qld_ref, qld_url, value_dict)
    else:
        msg_text.set("Unexpected event type: " + value_dict["event"])
        output_text.set("")
    return

def gen_sa():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        output_text.set("")
        return
    value_dict = parse_sa_html(clip.decode('utf-8'))
    if value_dict["event"] == "Birth":
        output_birth(sa_ref, sa_url, value_dict)
    elif value_dict["event"] == "Death":
        output_death(sa_ref, sa_url, value_dict)
    elif value_dict["event"] == "Marriage":
        output_marriage(sa_ref, sa_url, value_dict)
    elif value_dict["event"] != "":
        msg_text.set("Unexpected event type: " + value_dict["event"])
        output_text.set("")
    else:
        output_text.set("")
    return

def gen_wa():
    clip = get_html()
    if clip == None:
        msg_text.set("Unable to read HTML clipboard")
        output_text.set("")
        return
    value_dict = parse_wa_html(clip.decode('utf-8'))
    if value_dict["event"] == "Birth":
        output_birth(wa_ref, wa_url, value_dict)
    elif value_dict["event"] == "Death":
        output_death(wa_ref, wa_url, value_dict)
    elif value_dict["event"] == "Marriage":
        output_marriage(wa_ref, wa_url, value_dict)
    else:
        msg_text.set("Unexpected event type: " + value_dict["event"])
        output_text.set("")
    return

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
sa_button = tk.Button(button_frame, text="SA", command=sa_panel, width=8)
sa_button.grid(row=0, column=2, padx=5)
vic_button = tk.Button(button_frame, text="Vic", command=vic_panel, width=8)
vic_button.grid(row=0, column=3, padx=5)
wa_button = tk.Button(button_frame, text="WA", command=wa_panel, width=8)
wa_button.grid(row=0, column=4, padx=5)
# other states will go here

# NSW frame
nsw_frame = tk.Frame(root)
tk.Label(nsw_frame, text="Copy a row on the browser, then click on the button below that corresponds to the entry type").grid(row=0, column=0, columnspan=3)
tk.Button(nsw_frame, text="Birth", command=gen_nsw_birth, width=15).grid(row=1, column=0, padx=5, pady=3)
tk.Button(nsw_frame, text="Death", command=gen_nsw_death, width=15).grid(row=1, column=1, padx=5, pady=3)
tk.Button(nsw_frame, text="Marriage", command=gen_nsw_marriage, width=15).grid(row=1, column=2, padx=5, pady=3)

# Qld frame
qld_frame = tk.Frame(root)
tk.Label(qld_frame, text="Copy a row on the browser, then click Generate").grid(row=0, column=0)
tk.Button(qld_frame, text="Generate", command=gen_qld).grid(row=1, column=0, padx=5, pady=3)

# Vic frame
vic_frame = tk.Frame(root)
tk.Label(vic_frame, text="Copy a row on the browser, then click Generate").grid(row=0, column=0)
tk.Button(vic_frame, text="Generate", command=gen_vic).grid(row=1, column=0, padx=5, pady=3)

# SA frame
sa_frame = tk.Frame(root)
tk.Label(sa_frame, text="Copy a row on the browser, then click Generate").grid(row=0, column=0)
tk.Button(sa_frame, text="Generate", command=gen_sa).grid(row=1, column=0, padx=5, pady=3)

# WA frame
wa_frame = tk.Frame(root)
tk.Label(wa_frame, text="Copy a row on the browser, then click Generate").grid(row=0, column=0)
tk.Button(wa_frame, text="Generate", command=gen_wa).grid(row=1, column=0, padx=5, pady=3)

# output area (optional - mostly for debug, but it does allow you to check the result before pasting it)
output_box = tk.Label(root, textvariable=output_text, width=70, height=5, wrap=490, justify="left", anchor="nw", relief="sunken")
output_box.grid(row=5, column=0, padx=2, pady=2)

root.mainloop()
