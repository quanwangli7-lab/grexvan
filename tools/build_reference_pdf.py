"""Generate a factual reference sheet, not a performance or certification claim."""
from pathlib import Path
from io import BytesIO
from PIL import Image as PILImage
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'downloads/GREXVAN-GV-KIT-001-reference.pdf'
OUT.parent.mkdir(exist_ok=True)
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='Brand',fontName='Helvetica-Bold',fontSize=18,leading=22,textColor=HexColor('#202426'),spaceAfter=10))
styles.add(ParagraphStyle(name='TitleGV',fontName='Helvetica-Bold',fontSize=25,leading=29,spaceAfter=14,textColor=HexColor('#202426')))
styles.add(ParagraphStyle(name='SectionGV',fontName='Helvetica-Bold',fontSize=12,leading=16,spaceBefore=16,spaceAfter=8,textColor=HexColor('#b3262d')))
styles.add(ParagraphStyle(name='BodyGV',fontName='Helvetica',fontSize=10,leading=14,spaceAfter=7,textColor=HexColor('#303638')))
styles.add(ParagraphStyle(name='SmallGV',fontName='Helvetica',fontSize=8,leading=11,spaceAfter=6,textColor=HexColor('#626c70')))
P=lambda text:Paragraph(text,styles['BodyGV'])
doc=SimpleDocTemplate(str(OUT),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=34,bottomMargin=34,title='GREXVAN GV-KIT-001 Product Reference',author='GREXVAN',pageCompression=1)
story=[Paragraph('GREXVAN',styles['Brand']),Paragraph('GV-KIT-001<br/>Product Reference',styles['TitleGV'])]
photo = PILImage.open(ROOT/'support/kit001/images/GV-KIT-001_main.jpg')
photo.thumbnail((360,360))
embedded_photo = BytesIO()
photo.convert('RGB').save(embedded_photo, format='JPEG', quality=78)
embedded_photo.seek(0)
intro=Table([[P('Cabin + Engine Air Filter Kit<br/><br/>A two-component kit for the listed Mazda CX-5 applications.<br/><br/><b>Amazon ASIN:</b> B0HGZ3ZXWM'),Image(embedded_photo,width=125,height=125)]],colWidths=[360,145])
intro.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(-1,-1),12)]));story.append(intro)
story.append(Paragraph('KIT CONTENTS AND OE REFERENCES',styles['SectionGV']))
rows=[[P('<b>Component</b>'),P('<b>Reference numbers</b>')],[P('GV-CF-001 - Cabin Air Filter'),P('KD45-61-J6X series')],[P('GV-EF-001 - Engine Air Filter'),P('PE07-13-3A0 / PE07-13-3A0A')]]
t=Table(rows,colWidths=[240,265]);t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#eef1f1')),('GRID',(0,0),(-1,-1),0.5,HexColor('#dde2e3')),('VALIGN',(0,0),(-1,-1),'TOP'),('PADDING',(0,0),(-1,-1),9)]));story.append(t)
story.append(Paragraph('LISTED VEHICLE APPLICATIONS',styles['SectionGV']))
story.append(P('<b>Mazda CX-5 - naturally aspirated gasoline engines only</b><br/>2.0L: 2013-2019<br/>2.5L: 2014-2025'))
story.append(P('<b>Exclusion:</b> Not applicable to turbocharged models. Confirm the vehicle year, engine configuration and applicable OE reference before purchase or installation. OE references do not imply Mazda affiliation or OEM certification.'))
story.append(Paragraph('DOCUMENTATION AND BUSINESS INQUIRIES',styles['SectionGV']))
story.append(P('Fitment and installation: <link href="https://grexvan.com/support/kit001/">grexvan.com/support/kit001/</link><br/>Wholesale and product support: support@grexvan.com<br/>Amazon listing: <link href="https://www.amazon.com/dp/B0HGZ3ZXWM">amazon.com/dp/B0HGZ3ZXWM</link>'))
story.append(Spacer(1,10))
story.append(Paragraph('Reference revision: 2026-11-24. Model, contents, engine/year limits and OE numbers are consistent with the existing GREXVAN fitment pages and the Amazon listing reviewed for this revision; the site owner also confirmed the listing manually. This document is not an engineering drawing, lab test report or certification. No filtration efficiency, dimensions, certification, stock, pricing, delivery or additional warranty is stated.',styles['SmallGV']))
doc.build(story)
print(OUT)
