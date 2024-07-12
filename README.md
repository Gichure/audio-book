### PDF to Speech

#### Install Required Packages
``` 
pip install PyPDF3 pyttsx3 pdfplumber
```
-  PyPDF3 library to read and edit PDF files in Python.
-  pyttsx3 library provides text-to-speech conversion.
-  pdfplumber is a library that lets you extract text and tables from PDF files.

Import the required libraries

```
import PyPDF3
import pyttsx3
import pdfplumber
````

Provide the name and location of the PDF file to convert

```python
file_path = 'Doc.pdf'  

book = open(file_path, 'rb')
````
Get the total number of pages using the numPages property:

```
pages = pdfReader.numPages
````
Extract the text from the PDF file

```python
contentText = ""
 
with pdfplumber.open(file_path) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        contentText += text
````
Convert the text into audio and save it into a new file

```
engine = pyttsx3.init()
engine.save_to_file(finalText, 'audio.mp3')
engine.runAndWait()
```

Alternatively, you can just stream the audio

```
engine = pyttsx3.init()
engine.say(finalText)
engine.runAndWait()
```