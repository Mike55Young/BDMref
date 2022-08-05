# NSW BDM Date Finder
# Copyright (C) 2022 Mike Young

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
__author__ = "Mike Young"
__Version__ = "1.0"

# Constants
DAY = 0
MONTH = 1
YEAR = 2

#
import tkinter as tk
import datetime

start_date = datetime.date(2000,1,1)
mid_date = datetime.date(2000,1,1)
end_date = datetime.date(2000,1,1)

# Output an error message
def output_error(t):
    msg_text.set(t)
    msgbox["fg"] = "red"
    output_text.set("")

# Output functions --------------------------
def date_txt(dateval):
    return(str(dateval.day) + " " + str(dateval.month) + " " + str(dateval.year))

# Function to return the midpoint between two dates
def mid_point(start_date, end_date):
    mid_date = start_date
    date_diff = end_date - start_date
    days_diff = date_diff.days
    if days_diff > 1:
        mid_date = start_date + datetime.timedelta(days=days_diff//2)
        date_range_text.set("Try: " + date_txt(mid_date) + " to 31 12 " + str(end_date.year))
    else:
        date_range_text.set("Event was on " + date_txt(start_date))
    return(mid_date)

def set_year(year):
    global start_date
    global mid_date
    global end_date
    year = int(year_entry.get())
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    mid_date = mid_point(start_date, end_date)
    
def event_found():
    global start_date
    global mid_date
    global end_date
    # adjust lower bound up
    start_date = mid_date
    mid_date = mid_point(start_date, end_date)
    
def event_not_found():
    global start_date
    global mid_date
    global end_date
    # adjust upper bound down
    end_date = mid_date
    mid_date = mid_point(start_date, end_date)

# Setup the window
root = tk.Tk()

root.title("NSW BDM Date Finder v" + __Version__)
# common data
msg_text = tk.StringVar()
year_text = tk.StringVar()
date_range_text = tk.StringVar()
msg_text.set("Input the year to search")

# Message area
msgbox = tk.Label(root, textvariable=msg_text)
msgbox.grid(row=0, column=0)

# Year entry
year_frame = tk.Frame(root)
tk.Label(year_frame, text="Year:").grid(row=0, column=0)
year_entry = tk.Entry(year_frame, textvariable=year_text, width=10)
year_entry.bind('<Return>',set_year)
year_entry.focus_set()
year_entry.grid(row=0, column=1)
year_frame.grid(row=1, column=0)

# Date Range
tk.Label(root, textvariable=date_range_text).grid(row=2, column=0)

# Selection buttons
select_frame = tk.Frame(root)
tk.Button(select_frame, text="Event Found", command=event_found).grid(row=0, column=0, padx=5, pady=3)
tk.Button(select_frame, text="Not Found", command=event_not_found).grid(row=0, column=1, padx=5, pady=3)
select_frame.grid(row=3, column=0)

root.mainloop()
