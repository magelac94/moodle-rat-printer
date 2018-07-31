#!/usr/bin/env python
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

c = canvas.Canvas('rldemo4.pdf', pagesize=letter)
width, height = letter
c.drawString(inch, height - inch, 'Left')