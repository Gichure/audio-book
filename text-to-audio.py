import PyPDF4
import pyttsx3
import pdfplumber


file_path = 'book/CV.pdf'

book = open(file_path, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)


pages = pdfReader.numPages

contentText = ""
 
with pdfplumber.open(file_path) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        contentText += text
        
engine = pyttsx3.init()
engine.save_to_file(contentText, 'book/audio_cv.mp3')
engine.runAndWait()

