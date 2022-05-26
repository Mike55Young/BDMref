# BDMref
Reformat the output of Australian Births Deaths and Marriages websites as references for Genealogy websites like WikiTree.
At present it supports NSW, Queensland and Victoria. It is designed to be expanded to cover other states.
For South Australia it will need to use the Genealogy SA webite data, if possible.

To be able to run this you need to have Python 3 installed. It was developed on Python version 3.8

You will also need to have the pywin32 package installed to enable the clipboard handling functionality.
It can be installed by running the following command in a Windows Command prompt:
	pip install pywin32
	
More detailed installation instructions can be found at:
	https://www.geeksforgeeks.org/how-to-install-pywin32-on-windows/

You can either run the program from IDLE or by double-clicking on BDMref.pyw (as long as .pyw is associated with Python - install of Python should do that).
When you run BDMref.pyw it should open a small window showing buttons to select a state.

When one of the state buttons is clicked further buttons are added.
Once you have copied a single record line from the BDM website,
click on one of the added buttons to generate the formatted reference and copy it to the clipboard.
The generated text is also shown at the bottom of the window.

Victoria has a field in the BDM output for the type of record, so only one button is required.
For NSW you need to tell the program what type of record you are viewing, so there are three buttons, one for each type.
