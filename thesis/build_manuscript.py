from pathlib import Path
import subprocess,sys,json,io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from docx import Document
from docx.shared import Inches,Pt,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT,WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

root=Path(__file__).resolve().parent
stem='THESIS_Rounding_Statistical_Simulation_v0_6'
fig=root/'figures';fig.mkdir(exist_ok=True)
out=root/'deliverables';out.mkdir(exist_ok=True)
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'savefig.dpi':220})
f,ax=plt.subplots(figsize=(8.1,2.5))
colors=['#dbe4ee','#e8e8e8','#dbe4ee','#e8e8e8']
for y in range(4):
 ax.axvspan(4*y-.45,4*y+3.45,facecolor=colors[y],edgecolor='#7d8792',linewidth=.7)
 ax.text(4*y+1.5,.78,f'quotient {y}',ha='center')
 for r in range(4):
  x=4*y+r;ax.plot(x,.43,'o',color='#263d50',markersize=5)
  ax.text(x,.22,str(x),ha='center',fontsize=10)
ax.set(xlim=(-.7,15.7),ylim=(0,1),xticks=[],yticks=[])
ax.set_xlabel('Canonical input residue',labelpad=9)
for spine in ax.spines.values():spine.set_visible(False)
f.tight_layout();f.savefig(fig/'quotient_cells.png',bbox_inches='tight');plt.close(f)
f,ax=plt.subplots(figsize=(4.4,4))
grid=np.array([[(a+b)//4 for b in range(4)] for a in range(4)])
from matplotlib.colors import ListedColormap
ax.imshow(grid,origin='lower',cmap=ListedColormap(['#eff3f7','#94adbf']),vmin=0,vmax=1)
for i in range(4):
 for j in range(4):ax.text(j,i,str(grid[i,j]),ha='center',va='center',fontsize=16,color='#14232f')
ax.set(xticks=range(4),yticks=range(4),xlabel='Second remainder',ylabel='First remainder')
ax.set_xticks(np.arange(-.5,4,1),minor=True);ax.set_yticks(np.arange(-.5,4,1),minor=True)
ax.grid(which='minor',color='white',linewidth=2);ax.tick_params(which='minor',bottom=False,left=False)
f.tight_layout();f.savefig(fig/'carry_grid.png',bbox_inches='tight');plt.close(f)

# A scalar source and its parity target at the singular noise level.
from fractions import Fraction
P,Q=8,2
M=np.zeros((P,P//Q));N=np.zeros_like(M)
for z in range(P):
 for e,prob in [(-1,.25),(0,.5),(1,.25)]:
  x=(z+e)%P;M[z,x//Q]+=prob;N[z,((4*x)%P)//Q]+=prob
f,axes=plt.subplots(1,2,figsize=(8.1,4.5))
for ax,mat,title in zip(axes,[M,N],['Source channel M','Target channel N']):
 ax.imshow(mat,cmap='Blues',vmin=0,vmax=1,aspect='auto')
 for z in range(P):
  for w in range(P//Q):
   value=Fraction(float(mat[z,w]));label=str(value) if value else '0'
   ax.text(w,z,label,ha='center',va='center',fontsize=10,color='white' if value>Fraction(1,2) else '#14232f')
 ax.set(xticks=range(P//Q),yticks=range(P),xlabel='Output label',ylabel='Hidden state z',title=title)
 ax.set_xticks(np.arange(-.5,P//Q,1),minor=True);ax.set_yticks(np.arange(-.5,P,1),minor=True)
 ax.grid(which='minor',color='white',linewidth=1);ax.tick_params(which='minor',bottom=False,left=False)
f.tight_layout();f.savefig(fig/'noisy_channels.png',bbox_inches='tight');plt.close(f)

# The figure uses the exact orbit profile; verification reconstructs that profile.
profiles=json.loads((root/'data'/'part_iii'/'orbits.json').read_text())['domains']
profile=next(x for x in profiles if (x['P'],x['m'],x['n'])==(4,3,2))
masses=[(Fraction(x['orbit_size'],4096),Fraction(x['target_count'],256))
        for x in profile['target_orbit_profile']]
def budget_error(budget):
 return sum((max(Fraction(0),q-budget*p) for p,q in masses),Fraction(0))
rates=[Fraction(i,512) for i in range(1,513)]
budgets=sorted({Fraction(1),Fraction(16)}|{q/p for p,q in masses if 1<=q/p<=16})
f,axes=plt.subplots(1,2,figsize=(8.1,3.6))
axes[0].plot([float(a) for a in rates],[float(budget_error(1/a)) for a in rates],color='#263d50',lw=2)
axes[0].axvline(501/1024,color='#8a5b31',ls='--',lw=1.3,label='Maximum rate with Toeplitz outputs')
axes[0].set(xlabel='Acceptance probability',ylabel='Best conditional total variation',xlim=(0,1),ylim=(-.015,.56),title='One proposal')
axes[0].legend(fontsize=7,loc='upper left',frameon=True,framealpha=1,facecolor='white',edgecolor='none')
axes[1].plot([float(b) for b in budgets],[float(budget_error(b)) for b in budgets],color='#263d50',lw=2)
axes[1].set(xlabel='Expected independent proposals',xlim=(1,16),ylim=(-.015,.56),xticks=[1,4,8,12,16],title='Independent restarts')
for ax in axes:
 ax.grid(alpha=.2);ax.spines[['top','right']].set_visible(False)
f.tight_layout();f.savefig(fig/'orbit_tradeoff.png',bbox_inches='tight');plt.close(f)

# Repeated-observation curves are evaluated from recorded exact fractions.
curves=json.loads((root/'data'/'part_iv'/'exact_results.json').read_text())['curves_Q4']
f,ax=plt.subplots(figsize=(8.1,3.6))
ax.plot([x['k'] for x in curves],[float(Fraction(x['optimum'])) for x in curves],color='#263d50',lw=2,label='Optimal block kernel')
ax.plot([x['k'] for x in curves],[float(Fraction(x['fair'])) for x in curves],color='#8a5b31',lw=2,label='Independent fair bits')
ax.axhline(.5,color='#8a5b31',ls=':',lw=1)
ax.set(xlabel='Number of observations',ylabel='Full-view total variation',xlim=(1,64),ylim=(-.01,.53))
ax.legend(frameon=False,loc='center right');ax.grid(alpha=.2);ax.spines[['top','right']].set_visible(False)
f.tight_layout();f.savefig(fig/'repeated_error.png',bbox_inches='tight');plt.close(f)

f,ax=plt.subplots(figsize=(8.1,4.1))
points={'Fair':(0,7/64),'Sum-optimal':(1/104,5/64),'Posterior':(17/78,0),'Balanced':(5/24,1/32)}
front=[points[x] for x in ['Fair','Sum-optimal','Posterior']]
ax.plot([p[0] for p in front],[p[1] for p in front],color='#263d50',lw=2,label='Optimal public tradeoff')
for name,(x,y) in points.items():
 ax.scatter(x,y,s=36,color='#8a5b31' if name=='Balanced' else '#263d50',zorder=4)
 offset={'Fair':(10,-2),'Sum-optimal':(10,8),'Posterior':(-38,24),'Balanced':(-67,10)}[name]
 ax.annotate(name,(x,y),xytext=offset,textcoords='offset points',fontsize=10)
ax.set(xlabel='Null public error',ylabel='Real public error',xlim=(-.008,.235),ylim=(-.006,.12))
ax.grid(alpha=.2);ax.spines[['top','right']].set_visible(False)
f.tight_layout();f.savefig(fig/'two_world_errors.png',bbox_inches='tight');plt.close(f)

reference=root/'reference.docx' 
d=Document(io.BytesIO(subprocess.run(['pandoc','--print-default-data-file','reference.docx'],capture_output=True,check=True).stdout));sec=d.sections[0]
from docx.styles import BabelFish
for st in d.styles:
 st._element.find(qn('w:name')).set(qn('w:val'),BabelFish.ui2internal(st.name))
sec.page_width=Inches(8.5);sec.page_height=Inches(11)
sec.top_margin=sec.bottom_margin=Inches(.85)
sec.left_margin=sec.right_margin=Inches(.9)
for name in ['Normal','Body Text','First Paragraph','Compact','Title','Subtitle','Author','Date','Heading 1','Heading 2','Heading 3','Caption']:
 if name not in d.styles:continue
 st=d.styles[name];st.font.name='Liberation Serif';st.font.color.rgb=RGBColor(0,0,0)
 st.font.size=Pt(11.5)
 if st._element.rPr is not None:
  rfonts=st._element.rPr.find(qn('w:rFonts'))
  if rfonts is not None:
   for attr in ['asciiTheme','hAnsiTheme','eastAsiaTheme','cstheme']:
    rfonts.attrib.pop(qn('w:'+attr),None)
 st.paragraph_format.space_after=Pt(5)
 st.paragraph_format.line_spacing=1.10
 if st._element.rPr is not None:
  col=st._element.rPr.find(qn('w:color'))
  if col is not None:
   for attr in ['themeColor','themeTint','themeShade']:col.attrib.pop(qn('w:'+attr),None)
for name,size in [('Title',27),('Subtitle',15),('Heading 1',19),('Heading 2',13),('Heading 3',11.5)]:
 if name in d.styles:
  st=d.styles[name];st.font.size=Pt(size);st.font.bold=name.startswith('Heading')
  st.paragraph_format.keep_with_next=True
  st.paragraph_format.space_before=Pt(12 if name!='Title' else 0)
  st.paragraph_format.space_after=Pt(8)
d.styles['Heading 1'].paragraph_format.page_break_before=True
for st in d.styles:
 if st._element.pPr is not None:
  border=st._element.pPr.find(qn('w:pBdr'))
  if border is not None:st._element.pPr.remove(border)
for name in ['Normal','Body Text','First Paragraph']:
 if name in d.styles:d.styles[name].paragraph_format.widow_control=True
d.styles['Caption'].font.size=Pt(10);d.styles['Caption'].font.italic=True
sec.header_distance=Inches(.35);sec.footer_distance=Inches(.35)
sec.different_first_page_header_footer=True
hp=sec.header.paragraphs[0];hp.text='Rounding and Statistical Simulation';hp.alignment=WD_ALIGN_PARAGRAPH.RIGHT
for r in hp.runs:r.font.name='Liberation Serif';r.font.size=Pt(9);r.font.color.rgb=RGBColor(0,0,0)
fp=sec.footer.paragraphs[0];fp.alignment=WD_ALIGN_PARAGRAPH.CENTER
fld=OxmlElement('w:fldSimple');fld.set(qn('w:instr'),'PAGE');fp._p.append(fld)
d.save(reference)
subprocess.run(['pandoc',str(root/(stem+'.md')),'--from','markdown','--to','docx','--reference-doc',str(reference),'--resource-path',str(root),'-o',str(out/(stem+'.docx'))],check=True)
doc=Document(out/(stem+'.docx'))
# An empty OMML separator is unnecessary for one-argument delimiters and
# triggers a malformed-bracket import in LibreOffice. Omit that optional node.
for el in list(doc._element.iter(qn('m:sepChr'))):
 if el.get(qn('m:val'))=='':el.getparent().remove(el)
# Preserve standalone optimum asterisks and the cardinality hash as literal math tokens.
# The reviewer tested this compatibility fix with LibreOffice 25.2.3.2.
for math_run in doc._element.iter(qn('m:r')):
 text_node=math_run.find(qn('m:t'))
 if text_node is not None and text_node.text in ('*', '#'):
  props=math_run.find(qn('m:rPr'))
  if props is None:
   props=OxmlElement('m:rPr');math_run.insert(0,props)
  literal=props.find(qn('m:lit'))
  if literal is None:
   literal=OxmlElement('m:lit');props.insert(0,literal)
  literal.set(qn('m:val'),'1')
# LibreOffice 25.2 treats a standalone plus used as a positive-part subscript
# as an incomplete unary operator. Mark only these subscript runs as literal.
# Do not change ordinary binary addition or the scientific Markdown source.
for subscript in doc._element.iter(qn('m:sub')):
 if ''.join(t.text or '' for t in subscript.iter(qn('m:t'))) == '+':
  for math_run in subscript.iter(qn('m:r')):
   text_node=math_run.find(qn('m:t'))
   if text_node is not None and text_node.text == '+':
    props=math_run.find(qn('m:rPr'))
    if props is None:
     props=OxmlElement('m:rPr');math_run.insert(0,props)
    literal=props.find(qn('m:lit'))
    if literal is None:
     literal=OxmlElement('m:lit');props.insert(0,literal)
    literal.set(qn('m:val'),'1')
# Preserve double-struck set/expectation symbols through LibreOffice 25.2.
# Its OMML importer may drop m:scr=double-struck although the source is correct.
# Use the equivalent Unicode mathematical characters only on those tagged runs.
# Ordinary variables Z, R and E are deliberately not changed.
double_struck_symbols={'Z':'ℤ','R':'ℝ','E':'𝔼'}
for math_run in doc._element.iter(qn('m:r')):
 text_node=math_run.find(qn('m:t'))
 props=math_run.find(qn('m:rPr'))
 script=props.find(qn('m:scr')) if props is not None else None
 if script is not None and script.get(qn('m:val'))=='double-struck' and text_node is not None and text_node.text in double_struck_symbols:
  text_node.text=double_struck_symbols[text_node.text]
  props.remove(script)
  literal=props.find(qn('m:lit'))
  if literal is None:
   literal=OxmlElement('m:lit');props.insert(0,literal)
  literal.set(qn('m:val'),'1')
for p in doc.paragraphs:
 if p.style.name in ('Title','Subtitle','Author','Date'):
  p.alignment=WD_ALIGN_PARAGRAPH.CENTER
 if p.style.name=='Title':p.paragraph_format.space_before=Pt(95);p.paragraph_format.space_after=Pt(24)
 if p.style.name=='Subtitle':
  p.text='Complete manuscript\nRounding, noise, structure\nand repeated observations'
  p.paragraph_format.space_after=Pt(28)
 if p.style.name=='Date':p.paragraph_format.space_after=Pt(18)
 # Display equations stay intact; long inline paragraphs may flow naturally.
 if p._p.find('.//'+qn('m:oMathPara')) is not None:
  p.paragraph_format.keep_together=True
  p.paragraph_format.space_before=Pt(5);p.paragraph_format.space_after=Pt(7)
 if p.style.name=='Heading 1':p.paragraph_format.page_break_before=True
for table in doc.tables:
 table.alignment=WD_TABLE_ALIGNMENT.CENTER;table.autofit=False
 table_width=6.5
 cols=len(table.columns)
 widths=([2.2,2.1,2.2] if cols==3 else [table_width/cols]*cols)
 headers=[cell.text.strip() for cell in table.rows[0].cells]
 notation_table=headers==['Symbol','Meaning','Location']
 if notation_table:widths=[1.5,4.1,.9]
 if headers==['Question','Principal result','What is kept fixed']:widths=[2.3,1.65,2.55]
 if headers==['Resource change','Quantity that remains constrained','Consequence proved in the volume']:widths=[2.05,2.05,2.4]
 for i,col in enumerate(table.columns):col.width=Inches(widths[i])
 pr=table._tbl.tblPr
 borders=OxmlElement('w:tblBorders')
 for edge in ('top','left','bottom','right','insideH','insideV'):
  el=OxmlElement('w:'+edge);el.set(qn('w:val'),'single');el.set(qn('w:sz'),'4');el.set(qn('w:color'),'D9D9D9');borders.append(el)
 pr.append(borders)
 margins=OxmlElement('w:tblCellMar')
 for edge,value in [('top','90'),('bottom','90'),('left','100'),('right','100')]:
  el=OxmlElement('w:'+edge);el.set(qn('w:w'),value);el.set(qn('w:type'),'dxa');margins.append(el)
 pr.append(margins)
 for i,row in enumerate(table.rows):
  trpr=row._tr.get_or_add_trPr();nosplit=OxmlElement('w:cantSplit');trpr.append(nosplit)
  if i==0:trpr.append(OxmlElement('w:tblHeader'))
  for j,cell in enumerate(row.cells):
   cell.width=Inches(widths[j]);cell.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
   if i==0:
    sh=OxmlElement('w:shd');sh.set(qn('w:fill'),'E6E6E6');cell._tc.get_or_add_tcPr().append(sh)
   for p in cell.paragraphs:
    p.paragraph_format.space_after=Pt(1);p.paragraph_format.line_spacing=1.08
    p.paragraph_format.keep_with_next=((i==0) if notation_table else (i<len(table.rows)-1))
    p.paragraph_format.keep_together=True
    if cols>=4:p.alignment=WD_ALIGN_PARAGRAPH.CENTER
    for r in p.runs:r.font.size=Pt(10);r.font.color.rgb=RGBColor(0,0,0);r.font.bold=(i==0)
doc.core_properties.title='Rounding and Statistical Simulation'
doc.core_properties.subject='Affine compatibility, matrix distributions and repeated-observation simulation'
doc.core_properties.author='Samir Bouftass and ChatGPT (OpenAI)'
doc.core_properties.keywords='rounding; statistical simulation; affine maps; total variation; Toeplitz matrices; rejection sampling'
doc.save(out/(stem+'.docx'))
for ext,extra in [('tex',[]),('html',['--mathml'])]:
 subprocess.run(['pandoc',str(root/(stem+'.md')),'--standalone',*extra,'-o',str(out/(stem+'.'+ext))],check=True)
import shutil
shutil.copytree(fig,out/'figures',dirs_exist_ok=True)
print(json.dumps({'docx':str(out/(stem+'.docx')),'native_math_objects':len(doc._element.findall('.//'+qn('m:oMath'))),'figures':6}))
