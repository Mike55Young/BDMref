# NSW BDM Reference Generator for Wikitree
__author__ = "Mike Young"
__Version__ = "2.7"

#
import tkinter as tk
import string
import time
import os
import win32clipboard
import webbrowser

outtext = ""

# Constants - These strings will normally come from the Config.ini file
# the values here will only be used if Config.ini is unreadable.
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
format_name = "Format.ini"
format_date = "dd mmm yyyy"
# End of Config defaults

# Dictionary of NSW Early Church Record codes
# Based on the NSW webpage: https://www.nsw.gov.au/family-and-relationships/family-history-search/early-church-codes
# Where multiple sites are listed I've chosen a representative one.
church_codes = {"AA": ["Baptist", "Sydney, St Andrews"],
    "AB": ["Baptist", "Field of Mars"],
    "AC": ["Baptist", "Sydney, St James"],
    "AD": ["Baptist", "Co. Cumberland"],
    "AE": ["Baptist", "Sydney, Macquarie St"],
    "AF": ["Baptist", "Sydney, St Lawrence's"],
    "AG": ["Baptist", "Sydney"],
    "AH": ["Baptist", "Parramatta"],
    "AI": ["Baptist", "Melbourne (Vic)"],
    "AJ": ["Baptist", "Sydney, St Phillip's"],
    "CA": ["Church of England", "Sydney, St Phillip's"],
    "CB": ["Church of England", "Parramatta, St John's"],
    "CC": ["Church of England", "Windsor, St Matthew's"],
    "CD": ["Church of England", "Castlereagh"],
    "CE": ["Church of England", "Richmond"],
    "CF": ["Church of England", "Liverpool, St Luke's"],
    "CG": ["Church of England", "Norfolk Island"],
    "CH": ["Church of England", "Newcastle"],
    "CI": ["Church of England", "Campbelltown"],
    "CJ": ["Church of England", "Sydney, St James'"],
    "CK": ["Church of England", "Port Macquarie"],
    "CL": ["Church of England", "Kelso"],
    "CM": ["Church of England", "Wilberforce"],
    "CN": ["Church of England", "Sackville Reach"],
    "CO": ["Church of England", "Moreton Bay (Qld)"],
    "CP": ["Church of England", "Sydney"],
    "CQ": ["Church of England", "Marsfield"],
    "CR": ["Church of England", "Narellan"],
    "CS": ["Church of England", "Pitt Town"],
    "CT": ["Church of England", "Hunter District"],
    "CU": ["Church of England", "Brisbane (Qld)"],
    "CV": ["Church of England", "Berrima"],
    "CW": ["Church of England", "Bathurst"],
    "CX": ["Church of England", "Castle Hill"],
    "CY": ["Church of England", "Lower Hawkesbury"],
    "CZ": ["Church of England", "Illawarra"],
    "EA": ["Hebrew", "Sydney"],
    "EB": ["Hebrew", "Port Macquarie"],
    "EC": ["Hebrew", "Maitland"],
    "ED": ["Hebrew", "Illawarra"],
    "EE": ["Hebrew", "Windsor"],
    "EF": ["Hebrew", "Bathurst"],
    "EG": ["Hebrew", "Parramatta"],
    "EH": ["Hebrew", "Shoalhaven"],
    "EI": ["Hebrew", "Singleton"],
    "EJ": ["Hebrew", "Goulburn"],
    "EK": ["Hebrew", "Melbourne (Vic)"],
    "EL": ["Hebrew", "Moreton Bay (Qld)"],
    "EM": ["Hebrew", "Scone"],
    "EN": ["Hebrew", "Yass"],
    "EO": ["Hebrew", "Tamworth"],
    "EP": ["Hebrew", "Queanbeyan"],
    "EQ": ["Hebrew", "Western NSW"],
    "ER": ["Hebrew", "Richmond River"],
    "ES": ["Hebrew", "Albury"],
    "ET": ["Hebrew", "Tumut"],
    "EU": ["Hebrew", "Manning River"],
    "GA": ["Independent (Congregational)", "Lake Macquarie"],
    "GB": ["Independent (Congregational)", "Sydney, Pitt St"],
    "GC": ["Independent (Congregational)", "Melbourne (Vic)"],
    "GD": ["Independent (Congregational)", "Parramatta"],
    "GE": ["Independent (Congregational)", "Alexandria"],
    "GF": ["Independent (Congregational)", "Sydney, St Phillip's Mariners' Church"],
    "GG": ["Independent (Congregational)", "Petersham"],
    "GH": ["Independent (Congregational)", "Maitland"],
    "GI": ["Independent (Congregational)", "Sydney, St Lawrence's"],
    "GJ": ["Independent (Congregational)", "Brisbane (Qld)"],
    "GK": ["Independent (Congregational)", "Ipswitch (Qld)"],
    "GL": ["Independent (Congregational)", "Newcastle"],
    "GM": ["Independent (Congregational)", "Saluafala, Island of Upolu, Samoa"],
    "GN": ["Independent (Congregational)", "Sydney, St James'"],
    "GO": ["Independent (Congregational)", "Wollongong"],
    "IA": ["Wesleyan Methodist", "Sydney"],
    "IB": ["Wesleyan Methodist", "Parramatta"],
    "IC": ["Wesleyan Methodist", "Lower Hawkesbury"],
    "ID": ["Wesleyan Methodist", "Macdonald River"],
    "IE": ["Wesleyan Methodist", "Sackville Reach"],
    "IF": ["Wesleyan Methodist", "Portland Head"],
    "IG": ["Wesleyan Methodist", "Bathurst"],
    "IH": ["Wesleyan Methodist", "Windsor"],
    "II": ["Wesleyan Methodist", "Mudgee"],
    "IJ": ["Wesleyan Methodist", "Wollongong"],
    "IK": ["Wesleyan Methodist", "Maitland"],
    "IL": ["Wesleyan Methodist", "Melbourne (Vic)"],
    "IM": ["Wesleyan Methodist", "Geelong (Vic)"],
    "IN": ["Wesleyan Methodist", "Camden"],
    "IO": ["Wesleyan Methodist", "Kempsey"],
    "IP": ["Wesleyan Methodist", "Newcastle"],
    "IQ": ["Wesleyan Methodist", "Goulburn"],
    "IR": ["Wesleyan Methodist", "Alexandria"],
    "IS": ["Wesleyan Methodist", "Brisbane (Qld)"],
    "IT": ["Wesleyan Methodist", "Queanbeyan"],
    "IU": ["Wesleyan Methodist", "Surry Hills"],
    "IV": ["Wesleyan Methodist", "Newtown"],
    "IW": ["Wesleyan Methodist", "Armidale"],
    "IX": ["Wesleyan Methodist", "Bowenfels"],
    "IY": ["Wesleyan Methodist", "Bega"],
    "IZ": ["Wesleyan Methodist", "Albury"],
    "JA": ["Presbyterian", "Sydney, Scots Church"],
    "JB": ["Presbyterian", "Sydney, St Andrew's Scots Church"],
    "JC": ["Presbyterian", "Wollongong"],
    "JD": ["Presbyterian", "Wiseman's Ferry"],
    "JE": ["Presbyterian", "Balmain"],
    "JF": ["Presbyterian", "Newcastle"],
    "JG": ["Presbyterian", "Alexandria"],
    "JH": ["Presbyterian", "Murrurundi"],
    "JI": ["Presbyterian", "Bathurst"],
    "JJ": ["Presbyterian", "Shoalhaven"],
    "JK": ["Presbyterian", "Sydney, St Stephen's"],
    "JL": ["Presbyterian", "Hawkesbury District"],
    "JM": ["Presbyterian", "Wilberforce"],
    "JN": ["Presbyterian", "Parramatta"],
    "JO": ["Presbyterian", "Windsor, St Mattew's"],
    "JP": ["Presbyterian", "Windsor, St Lawrence's"],
    "JQ": ["Presbyterian", "Sydney, St James'"],
    "JR": ["Presbyterian", "Seaham"],
    "JS": ["Presbyterian", "Portland Head"],
    "JT": ["Presbyterian", "Port Macquarie"],
    "JU": ["Presbyterian", ""],
    "JV": ["Presbyterian", "Richmond"],
    "JW": ["Presbyterian", "Houghton"],
    "JX": ["Presbyterian", "Yass"],
    "JY": ["Presbyterian", "Goulburn"],
    "JZ": ["Presbyterian", "Co. Cook"],
    "KA": ["Primitive Methodist", "Sydney"],
    "KB": ["Primitive Methodist", "Maitland"],
    "KC": ["Primitive Methodist", "Houghton"],
    "KD": ["Primitive Methodist", "Newcastle"],
    "KE": ["Primitive Methodist", "South West Sydney"],
    "LA": ["Roman Catholic", ""]}

# Element type constants for the HTML parser
START_TAG = 1
END_TAG = 2
DATA = 3

# Output an error message
def output_error(t):
    msg_text.set(t)
    msgbox["fg"] = "red"
    output_text.set("")

# Functions to read the clipboard
# get the clipboard contents as text
def get_text():
    try:
        win32clipboard.OpenClipboard(0)
        src = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
    except TypeError:
        output_error("Unable to read clipboard")
        src = ""
    finally:
        win32clipboard.CloseClipboard()
    return(src)

# get the clipboard contents as html
def get_html():
    try:
        win32clipboard.OpenClipboard(0)
        html_format = win32clipboard.RegisterClipboardFormat("HTML Format")
        src = win32clipboard.GetClipboardData(html_format)
    except TypeError:
        output_error("Unable to read HTML clipboard")
        src = ""
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
# Function to return todays date in a specified format
def get_date(dform):
    # print "Inserting date with format", dform
    # Date format is flexible, and the following are recognised:
    # d - day of month - leading zero suppressed
    # dd - day of month - always 2 digits
    # m - month number - leading zero suppressed
    # mm - month number - always 2 digits
    # mmm - month name (3 letters)
    # mmmm - full month name
    # yy - year (2 digit)
    # yyyy - year (4 digit)
    # other characters including spaces are copied as is
    outdate = ""
    (year, month, day) = time.localtime()[0:3]
    i = 0
    while i < len(dform):
        if dform[i:i+2] == 'dd':
            d2 = '0' + str(day)
            outdate = outdate + d2[-2:]
            i = i + 2
        elif dform[i:i+1] == 'd':
            outdate = outdate + str(day)
            i = i + 1
        elif dform[i:i+4] == 'mmmm':
            outdate = outdate + ('January','February','March','April','May','June','July','August','September','October','November','December')[month-1]
            i = i + 4
        elif dform[i:i+3] == 'mmm':
            outdate = outdate + ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[month-1]
            i = i + 3
        elif dform[i:i+2] == 'mm':
            m2 = '0' + str(month)
            outdate = outdate + m2[-2:]
            i = i + 2
        elif dform[i:i+1] == 'm':
            outdate = outdate + str(month)
            i = i + 1
        elif dform[i:i+4] == 'yyyy':
            outdate = outdate + str(year)
            i = i + 4
        elif dform[i:i+2] == 'yy':
            outdate = outdate + str(year)[-2:]
            i = i + 2
        else:
			# copy other characters to output as is
            outdate = outdate + dform[i]
            i = i + 1
    return(outdate)

# Copy the generated reference to the clipboard and the output box
def output_reference(out):
    output_text.set(out)
    root.clipboard_clear()
    root.clipboard_append(out)

def output_var(state_ref, state_url, value_dict, var_list):
    var_key = var_list[1]
    var_style = ""
    if var_key[-2] == ",":
        var_style = var_key[-1]
        var_key = var_key[:-2]
    if var_key == "title":
        var_value = state_ref
    elif var_key == "url":
        var_value = state_url
    elif var_key == "today":
        var_value = get_date(format_date)
    elif value_dict[var_key] != "":
        var_value = value_dict[var_key]
    else:
        var_value = ""
    if var_value != "":        
        if var_style == "C":
            var_value = var_value.title()
        elif var_style == "U":
            var_value = var_value.upper()
        elif var_style == "L":
            var_value = var_value.lower()
        return var_list[0] + var_value + var_list[2]
    else:
        return ""

def output_group(state_ref, state_url, value_dict, group_list):
    group_text = ""
    var_present = False
    for group_entry in group_list:
        if len(group_entry) > 1:
            group_text += group_entry[0]
            var_text = output_var(state_ref, state_url, value_dict, group_entry[1])
            if var_text != "":
                var_present = True
                group_text += var_text
        else:
            group_text += group_entry[0]
    if var_present:
        return group_text
    else:
        return ""

def output_format(state_ref, state_url, value_dict, format_list):
    TYPE = 0
    VALUE = 1
    output_text = ""
    for format_entry in format_list:
        if format_entry[TYPE] == "text":
            output_text += format_entry[VALUE]
        elif format_entry[TYPE] == "group":
            output_text += output_group(state_ref, state_url, value_dict, format_entry[VALUE])
        elif format_entry[TYPE] == "var":
            output_text += output_var(state_ref, state_url, value_dict, format_entry[VALUE])
    output_reference(output_text)
    msg_text.set("Reference copied to clipboard")
    msgbox["fg"] = "green"
            
def parse_format(format_text):
    txt = ""
    nest_level = 0
    is_var = False
    format_list = []
    group_list = []
    var_list = []
    for c in format_text:
        if c == "{":
            if is_var:
                return ["Can't have a variable within another variable"]
            if nest_level == 0:
                if txt != "":
                    format_list.append(["text",txt])
                    txt = ""
            else:
                group_text = txt
                txt = ""
            nest_level += 1
        elif c == "|":
            if nest_level > 0:
                is_var = True
                var_list.append(txt)
                txt = ""
        elif c == "}":
            if is_var:
                var_list.append(txt)
                txt = ""
                if nest_level > 1:
                    group_list.append([group_text,var_list])
                    group_text = ""
                else:
                    format_list.append(["var", var_list])
                is_var = False
                var_list = []
            else:
                if txt != "":
                    group_list.append([txt])
                    txt = ""
                format_list.append(["group", group_list])
                group_list = []
            nest_level -= 1
        else:
            txt += c
    if txt != "":
        format_list.append(["text", txt])
    return format_list

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
                  "groom age": "",
                  "groom status": "",
                  "groom father": "",
                  "bride given": "",
                  "bride family": "",
                  "bride age": "",
                  "bride status": "",
                  "bride father": "",
                  "spouse given": "",
                  "spouse family": "",
                  "spouse": "",
                  "spouse gender": "",
                  "location": "",
                  "location birth": "",
                  "location death": "",
                  "date": "",
                  "year": "",
                  "dob": "",
                  "age": "",
                  "notes": "",
                  "relative": "",
                  "marital status": "",
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

# HTML parsing functions
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
    if i == -1:
        output_error("Not a valid NSW clip")
        value_dict["event"] = "Error"
        return value_dict
    while i >= 0:
        tag_name = get_key(tag_suffix)
        j = clip.find("</span>", i)
        tag_value = clip[i:j].replace("\\'", "'")
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

# Routine to handle names from the Victorian website.
# Names are in the format Surname, Given Names
# If the surname is omitted the website displays this as "<Unknown Family Name>" with the < and > converted to &lt; and &gt;
# If the given name is omitted the comma is omitted too.
def parse_vic_name(field_value, dict_key, value_dict):
    if field_value.find(",") >= 0:
        name_family, name_given = field_value.split(',')
    else:
        name_family = field_value
        name_given = ""
    if name_family == "&lt;Unknown Family Name&gt;":
        name_family = ""
    if name_family == "":
        value_dict[dict_key] = name_given.strip()
    elif name_given == "":
        value_dict[dict_key] = name_family.strip()
    else:
        value_dict[dict_key] = field_value.strip()

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
        output_error("Not enough columns copied - expecting 12, got " + str(len(field_list)))
        value_dict["event"] = "Error"
        return value_dict
        
    # Now store the columns into the respective dictionary items
    value_dict["family name"] = field_list[0]
    value_dict["given name"] = field_list[1]
    value_dict["event"] = field_list[2]
    if value_dict["event"] == "Marriage":
        parse_vic_name(field_list[3], "spouse", value_dict)
    else:
        parse_vic_name(field_list[3], "mother", value_dict)
    value_dict["mother family"] = field_list[4]
    parse_vic_name(field_list[5], "father", value_dict)
    value_dict["location birth"] = field_list[6]
    value_dict["location death"] = field_list[7]
    parse_vic_name(field_list[8], "death spouse", value_dict)
    value_dict["age"] = field_list[9]
    value_dict["date"] = field_list[10]
    value_dict["reg no"] = field_list[11]
    return value_dict

def parse_qld_html(clip):
    value_dict = init_value_dict()
    i = clip.find('<a class="recordlink"')
    if i == -1:
        output_error("Not a valid Queensland clip - expecting link to details page")
        value_dict["event"] = "Error"
        return value_dict
    i = clip.find('href=', i + 20)
    q = clip[i + 5]
    j = clip.find(q, i + 6)
    value_dict.update({"url": clip[i + 6:j]})
    i = clip.find(">", j)
    j = clip.find("<", i)
    value_dict["name"] = clip[i + 1:j].strip()
    i = clip.find("<br", j)
    while i != -1:
        i = clip.find(">", i) + 1
        j = clip.find("<", i)
        s = clip[i:j]
        if s.find(":") > 0:
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
        i = clip.find("<br", j)
        k = clip.find('<li class="related', j)
        if k > 0:
            if k < i or i == -1:
                i = k
    return value_dict
 
def parse_sa_list(clip):
    value_dict = init_value_dict()
    field_list = []
    # Find strings bounded by <td...> </td> and create a list corresponding to the columns on the page
    i = clip.find('<td')
    while i != -1:
        i = clip.find('>', i) + 1
        j = clip.find("</td>", i)
        field_list.append(clip[i:j].strip())
        i = clip.find('<td', j)
    if len(field_list) < 6:
        output_error("Should be at least 6 columns but found " + str(len(field_list)))
        value_dict["event"] = "Error"
        return value_dict
    # Now work out what record type we have.
    # If View Details is the last field copied we can find the type in there.
    if field_list[-1][:2] == '<a':
        i = field_list[-1].find("coid=") + 5
        j = field_list[-1].find("&", i)
        value_dict["event"] = string.capwords(field_list[-1][i:j])
        field_list = field_list[:-1]
    if field_list[-2].find("/") >=0:
        logged_in = False
    elif field_list[-1].find("/") >= 0:
        logged_in = True
    else:
        output_error("Book/Page not in expected position")
        value_dict["event"] = "Error"
        return value_dict
    if value_dict["event"] == "":
        if logged_in:
            if len(field_list) == 8:
                value_dict["event"] = "Death"
            elif len(field_list) == 9:
                if field_list[3] == 'M' or field_list[3] == 'F':
                    value_dict["event"] = "Birth"
                else:
                    value_dict["event"] = "Marriage"
            else:
                output_error("Should be 8 or 9 columns (excluding View Details) but found " + str(len(field_list)))
                value_dict["event"] = "Error"
                return value_dict
        else:
            if len(field_list) == 6:
                value_dict["event"] = "Death"
            elif len(field_list) == 7:
                if field_list[2] == 'M' or field_list[2] == 'F':
                    value_dict["event"] = "Birth"
                else:
                    value_dict["event"] = "Marriage"
            else:
                output_error("Should be 6 or 7 columns (excluding View Details) but found " + str(len(field_list)))
                value_dict["event"] = "Error"
                return value_dict
        
    # Now store the columns into the respective dictionary items
    if logged_in:
        if value_dict["event"] == "Birth":
            value_dict["family name"] = field_list[0]
            value_dict["given name"] = field_list[1]
            value_dict["date"] = field_list[2]
            value_dict["gender"] = field_list[3]
            value_dict["father"] = field_list[4]
            value_dict["mother"] = field_list[5]
            value_dict["location"] = field_list[6]
        elif value_dict["event"] == "Death":
            value_dict["family name"] = field_list[0]
            value_dict["given name"] = field_list[1]
            value_dict["date"] = field_list[2]
            value_dict["age"] = field_list[3]
            value_dict["gender"] = field_list[4]
            value_dict["relative"] = field_list[5]
        elif value_dict["event"] == "Marriage":
            value_dict["groom family"] = field_list[0]
            value_dict["groom given"] = field_list[1]
            value_dict["bride family"] = field_list[2]
            value_dict["bride given"] = field_list[3]
            value_dict["date"] = field_list[4]
            value_dict["groom father"] = field_list[5]
            value_dict["bride father"] = field_list[6]
        else:
            output_error("Sorry, list not working properly - use details")
            value_dict["event"] = "Error"
        # Last 2 are always district, book/page
        value_dict["district"] = field_list[-2]
        value_dict["reg no"] = field_list[-1]
    else:
        # Not logged in - fields are a bit different
        if value_dict["event"] == "Marriage":
            if field_list[0].find("(members only)") >= 0:
                value_dict["groom family"] = ""
            else:    
                value_dict["groom family"] = field_list[0]
            value_dict["groom given"] = field_list[1]
            if field_list[2].find("(members only)") >= 0:
                value_dict["bride family"] = ""
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
        value_dict["year"] = field_list[-1]
    return value_dict

def parse_sa_detail(clip):
    value_dict = init_value_dict()
    field_list = []
    # parse the detail output
    i = clip.find('<span class="gsa_field_name')
    if i == -1:
        output_error("Not a valid SA Detail clip - gsa fields missing")
        value_dict["event"] = "Error"
        return value_dict
    while i != -1:
        i = clip.find('>', i)
        j = clip.find('</span>', i)
        field_name = clip[i+1:j]
        i = clip.find('<span class="gsa_field_value', j)
        i = clip.find('>', i)
        j = clip.find('</span>', i)
        field_value = clip[i+1:j]
        if field_value.find("(members only)") >= 0:
            field_value = ""
        if field_name == "Groom Surname:":
            value_dict["groom family"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Groom Given Names:":
            value_dict["groom given"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Bride Surname:":
            value_dict["bride family"] = field_value
        elif field_name == "Bride Given Names:":
            value_dict["event"] = "Marriage"
            value_dict["bride given"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Marriage Date:":
            value_dict["date"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Marriage Place:":
            value_dict["location"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Groom Age:":
            value_dict["groom age"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Groom Marital Status:":
            value_dict["groom status"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Groom Father:":
            value_dict["groom father"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Bride Age:":
            value_dict["bride age"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Bride Marital Status:":
            value_dict["bride status"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Bride Father:":
            value_dict["bride father"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Surname:":
            value_dict["family name"] = field_value
        elif field_name == "First Names:":
            value_dict["given name"] = field_value
        elif field_name == "Given Names:":
            value_dict["given name"] = field_value
        elif field_name == "Date of Birth:":
            value_dict["date"] = field_value
        elif field_name == "Gender:":
            value_dict["gender"] = field_value
        elif field_name == "Father:":
            value_dict["father"] = field_value
        elif field_name == "Mother:":
            value_dict["mother"] = field_value
        elif field_name == "Birth Residence:":
            value_dict["location"] = field_value
            value_dict["event"] = "Birth"
        elif field_name == "Death Date:":
            value_dict["date"] = field_value
            value_dict["event"] = "Death"
        elif field_name == "Age:":
            value_dict["age"] = field_value
        elif field_name == "Marital Status:":
            value_dict["marital status"] = field_value
        elif field_name == "Relative:":
            value_dict["relative"] = field_value
        elif field_name == "Place of Death:":
            value_dict["location death"] = field_value
            value_dict["event"] = "Death"
        elif field_name == "District:":
            value_dict["district"] = field_value
        elif field_name == "Book/Page:":
            value_dict["reg no"] = field_value
        elif field_name == "Notes:":
            value_dict["notes"] = field_value
        elif field_name == "Marriage Year:":
            value_dict["year"] = field_value
            value_dict["event"] = "Marriage"
        elif field_name == "Birth Year:":
            value_dict["year"] = field_value
            value_dict["event"] = "Birth"
        elif field_name == "Death Year:":
            value_dict["year"] = field_value
            value_dict["event"] = "Death"
        i = clip.find('<span class="gsa_field_name', j)
    if value_dict["event"] == "":
        output_error("Unable to determine event type - no event-specific field found")
        value_dict["event"] = "Error"
    return value_dict

def parse_sa_html(clip):
    if clip.find("<table") > 0:
        return parse_sa_list(clip)
    elif clip.find('<div class="gsa') > 0:
        return parse_sa_detail(clip)
    else:
        value_dict = init_value_dict()
        output_error("Not a valid SA clip.")
        value_dict["event"] = "Error"
        return value_dict

def parse_wa_html(clip):
    value_dict = init_value_dict()
    field_list = []
    # Find strings bounded by <td ...> </td>
    # The opening td contains an attribute with prefix cdk-column- that indicates the data type
    i = clip.find("<td")
    if i == -1:
        output_error("Not a valid WA clip - no table entries found")
        value_dict["event"] = "Error"
        return value_dict
    if clip.find("cdk-") == -1:
        output_error("Not a valid WA clip - cannot find field identifiers")
        value_dict["event"] = "Error"
        return value_dict
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
    if clip == "":
        return
    value_dict = parse_nsw_html(str(clip))
    if value_dict["event"] != "Error":
        output_format(nsw_ref, nsw_url, value_dict, birth_format)
    else:
        output_reference(str(clip) + "\n" + str(value_dict))

def gen_nsw_death():
    clip = get_html()
    if clip == "":
        return
    value_dict = parse_nsw_html(str(clip))
    if value_dict["event"] != "Error":
        output_format(nsw_ref, nsw_url, value_dict, death_format)
    else:
        output_reference(str(clip) + "\n" + str(value_dict))

def gen_nsw_marriage():
    clip = get_html()
    if clip == "":
        return
    value_dict = parse_nsw_html(str(clip))
    if value_dict["event"] != "Error":
        output_format(nsw_ref, nsw_url, value_dict, marriage_format)
    else:
        output_reference(str(clip) + "\n" + str(value_dict))

def gen_vic():
    clip = get_html()
    if clip == "":
        return
    value_dict = parse_vic_html(clip.decode('utf-8'))
    if value_dict["event"] == "Birth":
        output_format(vic_ref, vic_url, value_dict, birth_format)
    elif value_dict["event"] == "Death":
        output_format(vic_ref, vic_url, value_dict, death_format)
    elif value_dict["event"] == "Marriage":
        output_format(vic_ref, vic_url, value_dict, marriage_format)
    elif value_dict["event"] != "Error":
        output_error("Unexpected event type: " + value_dict["event"])
    else:
        output_reference(str(clip) + "\n" + str(value_dict))
    return

def gen_qld():
    clip = get_html()
    if clip == "":
        return
    value_dict = parse_qld_html(clip.decode('utf-8'))
    if value_dict["event"] == "Birth":
        output_format(qld_ref, value_dict["url"], value_dict, birth_format)
    elif value_dict["event"] == "Death":
        output_format(qld_ref, value_dict["url"], value_dict, death_format)
    elif value_dict["event"] == "Marriage":
        output_format(qld_ref, value_dict["url"], value_dict, marriage_format)
    elif value_dict["event"] != "Error":
        output_error("Unexpected event type: " + value_dict["event"])
    else:
        output_reference(str(clip) + "\n" + str(value_dict))
    return

def gen_sa():
    clip = get_html()
    if clip == "":
        return
    value_dict = parse_sa_html(clip.decode('utf-8'))
    if value_dict["event"] == "Birth":
        output_format(sa_ref, sa_url, value_dict, birth_format)
    elif value_dict["event"] == "Death":
        output_format(sa_ref, sa_url, value_dict, death_format)
    elif value_dict["event"] == "Marriage":
        output_format(sa_ref, sa_url, value_dict, marriage_format)
    elif value_dict["event"] != "Error":
        output_error("Unexpected event type: " + value_dict["event"])
    else:
        output_reference(str(clip) + "\n" + str(value_dict))
    return

def gen_wa():
    clip = get_html()
    if clip == "":
        return
    value_dict = parse_wa_html(clip.decode('utf-8'))
    if value_dict["event"] == "Birth":
        output_format(wa_ref, wa_url, value_dict, birth_format)
    elif value_dict["event"] == "Death":
        output_format(wa_ref, wa_url, value_dict, death_format)
    elif value_dict["event"] == "Marriage":
        output_format(wa_ref, wa_url, value_dict, marriage_format)
    elif value_dict["event"] != "Error":
        output_error("Unexpected event type: " + value_dict["event"])
    else:
        output_reference(str(clip) + "\n" + str(value_dict))
    return

def open_nsw_web():
    webbrowser.open(nsw_url)
    
def open_qld_web():
    webbrowser.open(qld_url)

def open_sa_web():
    webbrowser.open(sa_url)

def open_vic_web():
    webbrowser.open(vic_url)

def open_wa_web():
    webbrowser.open(wa_url)

# Load the Config.ini file
mypath = os.path.dirname(os.path.realpath(__file__))

try:
    f = open(mypath + "/Config.ini","r")
    config_data = f.read()
    f.close()
    config_lines = config_data.split("\n")
except:
    msg_txt.set(mypath + "/Config.ini is empty or missing")
    config_lines = []

for config_entry in config_lines:
    if config_entry != "":
        # ignore lines starting in # - they are comments
        if config_entry[0] != "#":
            config_key, config_value = config_entry.split("=")
            if config_key == "format":
                format_name = config_value
            elif config_key == "date":
                format_date = config_value
            elif config_key == "nsw_ref":
                nsw_ref = config_value
            elif config_key == "nsw_url":
                nsw_url = config_value
            elif config_key == "qld_ref":
                qld_ref = config_value
            elif config_key == "qld_url":
                qld_url = config_value
            elif config_key == "sa_ref":
                sa_ref = config_value
            elif config_key == "sa_url":
                sa_url = config_value
            elif config_key == "vic_ref":
                vic_ref = config_value
            elif config_key == "vic_url":
                vic_url = config_value
            elif config_key == "wa_ref":
                wa_ref = config_value
            elif config_key == "wa_url":
                wa_url = config_value

# Now read the Format file
try:
    f = open(mypath + "/" + format_name,"r")
    format_data = f.read()
    f.close()
except:
    msg_txt.set(mypath + "/" + format_name + " is empty or missing")
    format_data = ""

i = format_data.find("\nBirth")
j = format_data.find("\nDeath")
k = format_data.find("\nMarriage")
i1 = format_data.find("\n", i+1)
j1 = format_data.find("\n", j+1)
k1 = format_data.find("\n", k+1)
birth_format = parse_format(format_data[i1+1:j])
death_format = parse_format(format_data[j1+1:k])
marriage_format = parse_format(format_data[k1+1:])

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
tk.Button(nsw_frame, text="Open BDM Website", command=open_nsw_web, width=20).grid(row=2, column=0, columnspan=3, padx=5)

# Qld frame
qld_frame = tk.Frame(root)
tk.Label(qld_frame, text="Copy a row on the browser, then click Generate").grid(row=0, column=0)
tk.Button(qld_frame, text="Generate", command=gen_qld).grid(row=1, column=0, padx=5, pady=3)
tk.Button(qld_frame, text="Open BDM Website", command=open_qld_web, width=20).grid(row=2, column=0, padx=5)

# Vic frame
vic_frame = tk.Frame(root)
tk.Label(vic_frame, text="Copy a row on the browser, then click Generate").grid(row=0, column=0)
tk.Button(vic_frame, text="Generate", command=gen_vic).grid(row=1, column=0, padx=5, pady=3)
tk.Button(vic_frame, text="Open BDM Website", command=open_vic_web, width=20).grid(row=2, column=0, padx=5)

# SA frame
sa_frame = tk.Frame(root)
tk.Label(sa_frame, text="Copy a row on the browser, then click Generate").grid(row=0, column=0)
tk.Button(sa_frame, text="Generate", command=gen_sa).grid(row=1, column=0, padx=5, pady=3)
tk.Button(sa_frame, text="Open BDM Website", command=open_sa_web, width=20).grid(row=2, column=0, padx=5)

# WA frame
wa_frame = tk.Frame(root)
tk.Label(wa_frame, text="Copy a row on the browser, then click Generate").grid(row=0, column=0)
tk.Button(wa_frame, text="Generate", command=gen_wa).grid(row=1, column=0, padx=5, pady=3)
tk.Button(wa_frame, text="Open BDM Website", command=open_wa_web, width=20).grid(row=2, column=0, padx=5)

# output area (optional - mostly for debug, but it does allow you to check the result before pasting it)
output_box = tk.Label(root, textvariable=output_text, width=70, height=7, font=("", 12), wrap=600, justify="left", anchor="nw", relief="sunken")
output_box.grid(row=5, column=0, padx=2, pady=2)

root.mainloop()
