#!/usr/bin/env python3
"""Render Pandoc AST with ReportLab and native vector MathText glyphs.
No browser/network/TeX installation is needed. The Markdown manuscript is the editable source.
"""
from pathlib import Path
import subprocess,json,re,hashlib,html,os,tempfile
from PIL import Image as PILImage
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['mathtext.fontset']='stix'
from matplotlib.mathtext import MathTextParser
from matplotlib.font_manager import FontProperties
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Flowable,Table,TableStyle,Image,KeepTogether,Preformatted
root=Path(__file__).resolve().parent.parent
stem='Affine_Maps_Modular_Rounding'
ast=json.loads(subprocess.check_output(['pandoc',str(root/(stem+'.md')),'-t','json']))
fontroot=Path('/usr/share/fonts/truetype/dejavu')
for n,f in [('Body','DejaVuSerif.ttf'),('BodyB','DejaVuSerif-Bold.ttf'),('BodyI','DejaVuSerif-Italic.ttf'),('BodyBI','DejaVuSerif-BoldItalic.ttf'),('Mono','DejaVuSansMono.ttf')]:
 pdfmetrics.registerFont(TTFont(n,str(fontroot/f)))
pdfmetrics.registerFontFamily('Body',normal='Body',bold='BodyB',italic='BodyI',boldItalic='BodyBI')
styles={
 'body':ParagraphStyle('body',fontName='Body',fontSize=10.3,leading=14,spaceAfter=6,allowWidows=0,allowOrphans=0),
 'h2':ParagraphStyle('h2',fontName='BodyB',fontSize=14,leading=18,spaceBefore=14,spaceAfter=8,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='BodyB',fontSize=11,leading=15,spaceBefore=10,spaceAfter=6,keepWithNext=True),
 'title':ParagraphStyle('title',fontName='Body',fontSize=24,leading=29,spaceAfter=15),
 'sub':ParagraphStyle('sub',fontName='Body',fontSize=13,leading=18,spaceAfter=13),
 'ref':ParagraphStyle('ref',fontName='Body',fontSize=9,leading=12.3,spaceAfter=6),
 'small':ParagraphStyle('small',fontName='Body',fontSize=8.8,leading=12,spaceAfter=6),
 'table':ParagraphStyle('table',fontName='Body',fontSize=8.8,leading=12,spaceAfter=0),
 'code':ParagraphStyle('code',fontName='Mono',fontSize=7.8,leading=11,backColor=colors.HexColor('#f2f2f2'),borderPadding=7,spaceBefore=5,spaceAfter=9),
}
math_tmp=tempfile.TemporaryDirectory(prefix='rounded_math_')
math_dir=Path(math_tmp.name)
parser=MathTextParser('path');cache={};fontcache={};math_count=0

def clean(s):
 s=re.sub(r'\\tag\{[^}]*\}','',s)
 s=s.replace(r'\boxed{','{').replace(r'\tfrac',r'\frac')
 s=re.sub(r'\\(?:bigl|bigr|big|Bigl|Bigr)','',s)
 s=re.sub(r'\\(mathcal|mathbf|mathbb|mathrm)\s*([A-Za-z0-9])',r'\\\1{\2}',s)
 s=re.sub(r'\\frac\s*([A-Za-z0-9])\s*([A-Za-z0-9])',r'\\frac{\1}{\2}',s)
 s=re.sub(r'\\frac\s*([A-Za-z0-9])(?=\{)',r'\\frac{\1}',s)
 s=re.sub(r'\\le(?![A-Za-z])',r'\\leq',s)
 s=re.sub(r'\\ge(?![A-Za-z])',r'\\geq',s)
 s=s.replace(r'\square','□')
 s=s.replace(r'\bmod',r'\;\mathrm{mod}\;')
 s=re.sub(r'\\pmod\s*([A-Za-z0-9])',r'\; (\\mathrm{mod}\;\1)',s)
 return re.sub(r'\s+',' ',s).strip()

def getmath(s,size=10.3):
 global math_count
 key=hashlib.sha256((s+'|'+str(size)).encode()).hexdigest()[:16]
 if key not in cache:
  parsed=parser.parse('$'+clean(s)+'$',dpi=72,prop=FontProperties(size=size))
  for font,fs,cp,x,y in parsed.glyphs:
   path=font.fname
   if path not in fontcache:
    name='Math'+str(len(fontcache));pdfmetrics.registerFont(TTFont(name,path));fontcache[path]=name
  cache[key]=parsed
  PILImage.new('RGBA',(1,1),(255,255,255,0)).save(math_dir/(key+'.png'))
 math_count+=1
 return key,cache[key]

def paint(canv,key,x,y):
 r=cache[key];canv.saveState();canv.setFillColor(colors.HexColor('#171717'))
 for font,fs,cp,gx,gy in r.glyphs:
  canv.setFont(fontcache[font.fname],fs);canv.drawString(x+float(gx),y+float(gy),chr(cp))
 for rx,ry,w,h in r.rects:canv.rect(x+rx,y+ry,w,h,fill=1,stroke=0)
 canv.restoreState()

class MathCanvas(Canvas):
 def __init__(self,*args,**kwargs):
  kwargs["invariant"]=1
  super().__init__(*args,**kwargs)
 def drawImage(self,image,x,y,width=None,height=None,**kwargs):
  name=getattr(image,'fileName',image)
  key=Path(name).stem if isinstance(name,(str,Path)) else ''
  if key in cache:
   paint(self,key,x,y+float(cache[key].depth))
   return width,height
  return super().drawImage(image,x,y,width=width,height=height,**kwargs)

class MathBlock(Flowable):
 def __init__(self,s):
  Flowable.__init__(self);self.key,self.r=getmath(s,11.5);self.box=r'\boxed' in s
  self.tag=(re.search(r'\\tag\{([^}]*)\}',s) or [None,None])[1]
  self.spaceBefore=5;self.spaceAfter=8
 def wrap(self,w,h):
  self.aw=w;self.scale=min(1,(w-32)/(self.r.width+12));self.height=float(self.r.height)*self.scale+10
  return w,self.height
 def draw(self):
  c=self.canv;c.saveState();c.translate((self.aw-self.r.width*self.scale)/2,5+self.r.depth*self.scale);c.scale(self.scale,self.scale)
  paint(c,self.key,0,0)
  if self.box:c.rect(-5,-self.r.depth-4,self.r.width+10,self.r.height+8,stroke=1,fill=0)
  c.restoreState()
  if self.tag:c.setFont('Body',9);c.drawRightString(self.aw,self.height/2-3,'('+self.tag+')')

def inlines(items,size=10.3):
 out=[]
 for o in items:
  t=o['t'];v=o.get('c')
  if t=='Str':out.append(html.escape(v))
  elif t in ('Space','SoftBreak'):out.append(' ')
  elif t=='LineBreak':out.append('<br/>')
  elif t in ('Strong','Emph'):
   tag='b' if t=='Strong' else 'i';out.append('<'+tag+'>'+inlines(v,size)+'</'+tag+'>')
  elif t=='Code':out.append('<font name="Mono">'+html.escape(v[1])+'</font>')
  elif t=='Math':
   key,r=getmath(v[1],size)
   out.append(f'<img src="{math_dir/(key+".png")}" width="{float(r.width)+.5}" height="{float(r.height)+1}" valign="{-float(r.depth)}"/>')
  elif t=='Link':out.append('<link href="'+html.escape(v[2][0],quote=True)+'" color="#21516d">'+inlines(v[1],size)+'</link>')
  elif t=='Span':out.append(inlines(v[1],size))
  elif t=='Quoted':out.append('“'+inlines(v[1],size)+'”')
  elif t=='Image':out.append(inlines(v[1],size))
  else:raise ValueError(('unknown inline',t))
 return ''.join(out)

def blocks(bs,sty='body'):
 out=[]
 for bi,b in enumerate(bs):
  t=b['t'];v=b.get('c')
  if t in ('Para','Plain'):
   if len(v)==1 and v[0]['t']=='Math' and v[0]['c'][0]['t']=='DisplayMath':out.append(MathBlock(v[0]['c'][1]))
   else:
    para=Paragraph(inlines(v,styles[sty].fontSize),styles[sty])
    if bi+1<len(bs) and bs[bi+1]['t']=='Table':para.keepWithNext=True
    out.append(para)
  elif t=='Header':
   out.append(Paragraph(inlines(v[2],14 if v[0]==2 else 11),styles['h2' if v[0]<=2 else 'h3']))
   if any(o.get('c')=='References' for o in v[2]):sty='ref'
   if any(o.get('c')=='Authorship' for o in v[2]):sty='body'
  elif t=='Table':
   rows=v[3][1][:]
   for body in v[4]:rows+=body[2]+body[3]
   data=[[blocks(cell[4],'table') for cell in row[1]] for row in rows]
   n=len(data[0]);widths=([128,WIDTH-128] if n==2 else ([142,(WIDTH-142)/2,(WIDTH-142)/2] if n==3 else [WIDTH/n]*n))
   tb=Table(data,colWidths=widths,repeatRows=len(v[3][1]),hAlign='LEFT')
   tb.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#eeeeee')),('LINEABOVE',(0,0),(-1,0),.6,colors.grey),('LINEBELOW',(0,0),(-1,-1),.25,colors.lightgrey),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
   out.extend([Spacer(1,5),KeepTogether([tb]) if len(data)<=8 else tb,Spacer(1,10)])
  elif t=='CodeBlock':out.append(Preformatted(v[1],styles['code'],maxLineLength=94))
  elif t in ('OrderedList','BulletList'):
   items=v[1] if t=='OrderedList' else v
   for i,item in enumerate(items):
    fs=blocks(item,sty)
    if fs and isinstance(fs[0],Paragraph):
     fs[0]=Paragraph((str(i+1)+'. ' if t=='OrderedList' else '• ')+fs[0].text,styles[sty])
    out+=fs
  elif t=='Figure':
   im=Image(str(root/'figures'/'block_simulation.png'),width=WIDTH,height=WIDTH*3.65/8.2)
   cap=blocks(v[1][1],'small')
   out.append(KeepTogether([Spacer(1,7),im]+cap+[Spacer(1,8)]))
  elif t=='HorizontalRule':out.append(Spacer(1,10))
  else:raise ValueError(('unknown block',t))
 return out
WIDTH=A4[0]-2*60

def meta(name):return inlines(ast['meta'][name]['c'])
story=[Paragraph(meta('title'),styles['title']),Paragraph(meta('subtitle'),styles['sub']),
 Paragraph(meta('author'),styles['body']),Paragraph(meta('date'),styles['small']),Spacer(1,15)]+blocks(ast['blocks'])

def page(canv,doc):
 canv.saveState();canv.setFont('Body',8);canv.setFillColor(colors.grey)
 canv.drawString(60,A4[1]-34,'Affine Maps and Modular Rounding')
 canv.drawRightString(A4[0]-60,A4[1]-34,'English edition 1.1')
 canv.drawCentredString(A4[0]/2,30,str(doc.page));canv.restoreState()

doc=SimpleDocTemplate(str(root/(stem+'.pdf')),pagesize=A4,rightMargin=60,leftMargin=60,topMargin=57,bottomMargin=55,
 title=meta('title'),author='Samir Bouftass',
 subject=meta('subtitle'))
doc.build(story,onFirstPage=page,onLaterPages=page,canvasmaker=MathCanvas)
math_tmp.cleanup()
print(json.dumps(dict(math_occurrences=math_count,math_unique=len(cache),pdf=str(root/(stem+'.pdf')),pages=doc.page)))
