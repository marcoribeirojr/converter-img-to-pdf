from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
import os

local = os.getcwd()
addr = os.path.join(local, 'img')
content = os.listdir(addr)
file_list = [arq for arq in content if os.path.isfile(os.path.join(addr,arq))]

canvas = Canvas('output.pdf', pagesize=A4)
for f in file_list:
  canvas.drawImage(os.path.join(addr, f), 10, 10, mask='auto')
  canvas.showPage()
if len(file_list) > 0:
  canvas.save()


