# BDMref

This program reformats the output of Australian Births Deaths and Marriages websites as references for Genealogy websites like WikiTree.
At present it supports NSW, Queensland, Victoria, and Western Australia. It is designed to be expanded to cover other states.
For South Australia it will need to use the Genealogy SA webite data, if possible.

## Prerequisites

To be able to run this you need to have Python 3, and the pywin32 package for Python installed.  
It was developed on Python version 3.8

### Installing Python on Windows

You can obtain the latest version of Python from the Microsoft store. It is a free app.

The latest version at the time of writing is Python 3.10
Simply click on the latest version (highest number) and then click the Get button.

Version 3.11 is there in Beta form but I would recommend that you stick to the non-beta releases unless you are feeling adventurous!

### pywin32 package

You will also need to have the pywin32 package installed to enable the clipboard handling functionality.
It can be installed by running the following command in a Windows Command prompt:
	pip install pywin32
	
A batch file (install_pywin32.bat) is provided to run this command but it may run foul of some anti-virus software.
	
More detailed installation instructions can be found at:  
https://www.geeksforgeeks.org/how-to-install-pywin32-on-windows/

## Running BDMref

You can either run the program from IDLE or by double-clicking on BDMref.pyw (as long as .pyw is associated with Python - install of Python should do that).
When you run BDMref.pyw it should open a small window showing buttons to select a state.

When one of the state buttons is clicked further buttons are added.
Once you have copied a single record line from the BDM website,
click on one of the added buttons to generate the formatted reference and copy it to the clipboard.
The generated text is also shown at the bottom of the window.

Victoria and Queensland have a field in the BDM output for the type of record, so only one button is required.
For NSW you need to tell the program what type of record you are viewing, so there are three buttons, one for each type.

When selecting the text to be copied you need to highlight all the data fields in the row, then right click and select copy.
The field indicating document availability or linking to details is not required, and for NSW at least you will have trouble highlighting it anyway.

## Configuration

Config.ini contains the initialisation data such as the names of the BDM websites, their URLs, the date format, and the name of the output format file.
The format file is used to define the layout of the generated citation. Details can be found in the file itself.

## Version History

### Version 2.7
* Update SA processing to allow for differences when logged in as member
* Bugfix - remove checking for incomplete detail clip as that only works in Firefox (you now just get however much you copy)

### Version 2.6
* Increase the size of the output box from 5 rows to 7 rows and enlarge the font to 12pt
* Improve handling of errors like not copying enough of the row or selecting the wrong state
* Bugfix. If there was only one row in the second column of the Queensland website it was not collected for output
* Colour messages red (error) or green (copied to clipboard) to make them more noticeable
* Update output format files to show gender and marriage location if available. Have not included all the SA (members only) detail fields.
* Known issue: the correct parsing of the SA website list relies on copying the whole table row (including the View Details link), otherwise a birth might be incorrectly output as a death.

### Version 2.5
* Bugfix. Rework the handling of names on the Victorian website to correctly remove <Unknown Family Name> if present.

### Version 2.4
* Bugfix. Program would crash if father's given name was missing on the Victorian website
* Bugfix. Remove stray "\\" from before apostrophes on the NSW website (e.g. O\Keefe)
* Updates to output format files:
*   Make gender field in output format more obvious by prefixing with "Gender: "
*   Output mother's birth surname (Vic only) in parentheses after her name at the birth/death e.g. O'Keefe, Mary (FARRELL)

### Version 2.3
* Bugfix. Support change to Qld website where first entry in column 2 is no longer the ordering information

### Version 2.2
* Support SA website change and tolerate future changes better
* Support SA detail page (primarily useful for SA Genealogy members)
* SA now outputs the event year in a new variable "year" instead of "date". Default format file puts this after the reference number.

### Version 2.1
* Add a button to open the BDM website for the selected state in your default browser

### Version 2.0
* Support a website change
* Add config file and user defined formatting
* Provide for the current date to be inserted as an access date
* Treat lines starting with # in Config.ini as comments to be skipped

### Version 1.9
* Add support for South Australia (Genealogy SA)

### Version 1.8
* Add support for Western Australia

### Version 1.7
* Fixed missing field in Victorian output
* Converted Queensland to use HTML data, including url pointing to detail record (website says you can bookmark it)

### Version 1.6
* Some bugfixes
* Changed Victoria to use HTML clipboard
* Separate clip scanning and output processing. This prepares the way for output templates to allow customisation
* Added sample template files (not yet used). Will provide documentation on them when they get used.

### Version 1.5
* Fixed a nasty bug in v1.4

### Version 1.4
* Read the clipboard directly so you don't have to paste into BDMref
* NSW website is handled as an HTML clip to avoid issues with the text clip not having field separators in some browsers
* Version displayed at the top of the window
* State selection buttons recessed when pressed to show which state is selected
* HTML clipboard functionality requires the pywin32 package

### Version 1.3
* Fix issue with browser differences in the text clip for Queensland
* Known issue: NSW BDM website only works with the Firefox browser

### Version 1.2
* Make the program work with different browsers on the Victorian website
* Known issue: NSW BDM website only works with the Firefox browser

### Version 1.1
* Add support for the Queensland registry

### Version 1.0
* Basic program. Works with NSW and Victoria when using Firefox browser