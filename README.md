# BDMref

This program reformats the output of Australian Births Deaths and Marriages websites as references for Genealogy websites like WikiTree.
At present it supports NSW, Queensland, Victoria, South Australia and Western Australia.
It is designed to be expanded to cover other states as they become available.
For South Australia it uses the Genealogy SA webite data, either from the list or the details page.

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

All sites other than NSW have a field in the BDM output that can be used to determine the type of record, so only one button is required.
For NSW you need to tell the program what type of record you are viewing, so there are three buttons, one for each type.

When selecting the text to be copied you need to highlight all the data fields in the row, then right click and select copy.
The field indicating document availability or linking to details is not required, and for NSW at least you will have trouble highlighting it anyway.

## Configuration

Config.ini contains the initialisation data such as the names of the BDM websites, their URLs, the date format, and the name of the output format file.
The format file is used to define the layout of the generated citation. Details can be found in the file itself.

## Sample Output

### Format.ini

Data from the website (apart from surnames) is converted to mixed case.

**New South Wales**  
New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search : 15 Jul 2022) Birth registration # 29358/1900<br/>
SMITH James B F, Father: David L, Mother: Caroline M, District: Balmain North

New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search : 15 Jul 2022) Marriage registration # 1024/1900<br/>
Groom: SMITH James R, Bride: HEALEY Jane, District: Carcoar

New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search : 15 Jul 2022) Death registration # 8983/1900<br/>
SMITH James, Father: John, Mother: Nancy, District: Granville

**Queensland**  
Queensland family history research service (https://www.familyhistory.bdm.qld.gov.au/details/dd3c37c9f82a2e88a9db6ca7337570659f9724d159245325868da853f6bad64f : 15 Jul 2022) Birth registration # 1900/C/8586<br/>
James Smith, Date: 15/07/1900, Mother: Ada Emma Rensley  Jewell, Father/parent: Thomas

Queensland family history research service (https://www.familyhistory.bdm.qld.gov.au/details/b239ed528422d397ba0124c632918aa8df1601c16651f26269d9dd8012937bca : 15 Jul 2022) Marriage registration # 1900/C/2601<br/>
James Smith, Spouse: Caroline Kahl, Date: 13/12/1900

Queensland family history research service (https://www.familyhistory.bdm.qld.gov.au/details/09b75c11c900df9106046ed5b8c5135366a4fb99cc9b952927a71303f453a3a6 : 15 Jul 2022) Death registration # 1900/C/4145<br/>
James Smith, Date: 30/08/1900, Mother: Lucy Fleming, Father/parent: Thomas Smith

### Format_asis.ini

Data from the website is output as it appears on the website.

**New South Wales**  
New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search : 15 Jul 2022) Birth registration # 29358/1900<br/>
SMITH JAMES B F, Father: DAVID L, Mother: CAROLINE M, District: BALMAIN NORTH

New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search : 15 Jul 2022) Marriage registration # 1024/1900<br/>
Groom: JAMES R SMITH, Bride: JANE HEALEY, District: CARCOAR

New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search : 15 Jul 2022) Death registration # 8983/1900<br/>
SMITH JAMES, Father: JOHN, Mother: NANCY, District: GRANVILLE

**Queensland**  
Queensland family history research service (https://www.familyhistory.bdm.qld.gov.au/details/dd3c37c9f82a2e88a9db6ca7337570659f9724d159245325868da853f6bad64f : 15 Jul 2022) Birth registration # 1900/C/8586<br/>
James Smith, Date: 15/07/1900, Mother: Ada Emma Rensley  Jewell, Father/parent: Thomas

Queensland family history research service (https://www.familyhistory.bdm.qld.gov.au/details/b239ed528422d397ba0124c632918aa8df1601c16651f26269d9dd8012937bca : 15 Jul 2022) Marriage registration # 1900/C/2601<br/>
James Smith, Spouse: Caroline Kahl, Date: 13/12/1900

Queensland family history research service (https://www.familyhistory.bdm.qld.gov.au/details/09b75c11c900df9106046ed5b8c5135366a4fb99cc9b952927a71303f453a3a6 : 15 Jul 2022) Death registration # 1900/C/4145<br/>
James Smith, Date: 30/08/1900, Mother: Lucy Fleming, Father/parent: Thomas Smith

### Format_RG.ini

Data from the website is output as it appears on the website. Fields are individually labelled and delimited by parentheses.  
This format is included as an example of what can be done with output formatting.

**New South Wales**  
New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search : 15 Jul 2022)<br/>(Surname: SMITH); (Given Names: JAMES B F); (Father: DAVID L); (Mother: CAROLINE M); (District: BALMAIN NORTH); (Reg no: 29358/1900)

New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search : 15 Jul 2022)<br/>(Groom Surname: SMITH); (Groom Given Names: JAMES R)

New South Wales Family History - Births, Deaths and Marriages Search (https://familyhistory.bdm.nsw.gov.au/lifelink/familyhistory/search : 15 Jul 2022)<br/>(Surname: SMITH); (Given Names: JAMES); (Father: JOHN); (Mother: NANCY); (District: GRANVILLE); (Reg no: 8983/1900)

**Queensland**  
Queensland family history research service (https://www.familyhistory.bdm.qld.gov.au/details/dd3c37c9f82a2e88a9db6ca7337570659f9724d159245325868da853f6bad64f : 15 Jul 2022)<br/>(Name: James Smith); (Mother: Ada Emma Rensley  Jewell); (Father/parent: Thomas); (Reg no: 1900/C/8586); (Birth year: 15/07/1900)

Queensland family history research service (https://www.familyhistory.bdm.qld.gov.au/details/b239ed528422d397ba0124c632918aa8df1601c16651f26269d9dd8012937bca : 15 Jul 2022)<br/>(Name: James Smith); (Spouse: Caroline Kahl)

Queensland family history research service (https://www.familyhistory.bdm.qld.gov.au/details/09b75c11c900df9106046ed5b8c5135366a4fb99cc9b952927a71303f453a3a6 : 15 Jul 2022)<br/>(Name: James Smith); (Mother: Lucy Fleming); (Father/parent: Thomas Smith); (Reg no: 1900/C/4145); (Death year: 30/08/1900)


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
* Bugfix. Remove stray "\\" from before apostrophes on the NSW website (e.g. O\\'Keefe)
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