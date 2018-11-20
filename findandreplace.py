# ------- Importing required libraries ------- #
import zipfile
import os
import shutil
'''
a)zipfile is the library we require to change the contents of word files. All it does is allow us to assess the various associated files with a regular .docx file (this is explained later on).
b)os is for deleting the temporary files that get created (at the end)
c)shutil is for deleting the temporary folders that get created (at the end)
'''


def createResume(input):

    # NOTE: Replace the path to your files here
    address_of_sample_resume = "/Users/naveen/Desktop/Naveen/PES University/Semester 1/Introduction to Computing Using Python/ICUP-Project/SampleResume.docx"
    address_of_new_resume = "/Users/naveen/Desktop/Naveen/PES University/Semester 1/Introduction to Computing Using Python/ICUP-Project/OutputDocument.docx"
    address_of_temp_xml = "/Users/naveen/Desktop/Naveen/PES University/Semester 1/Introduction to Computing Using Python/ICUP-Project/temp.xml"

    '''
	address_of_sample_resume : where the sample resume / template is stored on your computer (needs a .docx extension)
	address_of_new_resume : where you want the output file to get stored - recommended to be in the same folder but name has to be different (needs a .docx extension)
	address_of_temp_xml : recommended to be in the same folder as before (needs a .xml extention)
	'''

    # ------- Defining replacement text ------- #
    replaceText = {"XXXNAMEXXX": "Joe",
                   "XXXEMAILXXX": "sample@gmail.com",
                   }
    replaceText.update(input)
    # I've only replaced 3 fields so far but feel free to change as many as you'd like
    '''
	replaceText : A dictionary containing all the replacements we have to make to the sample format where the keys are placeholders in the sample resume and the values are the user's inputs (Right now, it is hard-coded)
	'''

    # ------- Assigning variables to zipfile objects ------- #
    templateDocx = zipfile.ZipFile(address_of_sample_resume)
    # 'a' stands for 'append' access mode
    newDocx = zipfile.ZipFile(address_of_new_resume, "a")
    '''
	templateDocx : zipfile object of our sample resume
	newDocx : zipfile object of output (customized) resume
	'''

    # ------- Opening required files as zipfile objects ------- #
    with open(templateDocx.extract("word/document.xml")) as tempXmlFile:
        tempXmlStr = tempXmlFile.read()
    '''
	NOTE: Each word document consists of a number of .xml files which contain the actual content for each header, footer, paragraph, styles, etc. We are interested only in the document.xml file which is what contains all the text in our .docx file.
	The extract function is used to get that file and we henceforth name it as 'tempXmlFile'.
	The contents of this file (i.e contents of our sample resume) are read as a string into a variable 'tempXmlStr'
	'''

    # ------- Text Replacement  ------- #
    for key in replaceText.keys():
        tempXmlStr = tempXmlStr.replace(str(key), str(replaceText.get(key)))
    '''
	This is where the actual content replacement takes place. It is a simple string.replace() method.
	'''

    # ------- Creating temporary file  ------- #
    with open(address_of_temp_xml, "w+") as tempXmlFile:  # 'w+' allows us to write into the file
        tempXmlFile.write(tempXmlStr)
    '''
	This is just a temporary text file where we store the contents we want to write to the .docx later
	'''

    # ------- Rejoining temp file with original docx files  ------- #
    for file in templateDocx.filelist:
        if not file.filename == "word/document.xml":
            newDocx.writestr(file.filename, templateDocx.read(file))
    '''
	Using a for loop and the zipfile module to copy all of the files in the template docx archive to a new docx archive EXCEPT the word/document.xml file.
	'''

    # ------- Rezipping the .xml files to a .docx output file  ------- #
    newDocx.write(address_of_temp_xml, "word/document.xml")
    '''
	We are writing the temporary xml file with the replaced text to the new docx archive as a new word/document.xml file.
	The old document.xml gets over-written by our edited file
	'''

    # ------- Closing both our sample file and output file  ------- #
    templateDocx.close()
    newDocx.close()

    # ------- Deleting unnecessary files/folders  ------- #
    os.remove(address_of_temp_xml)
    shutil.rmtree("word")
    '''
	Removes the temp.xml file as well as the word/document.xml folder with its contents
	'''
