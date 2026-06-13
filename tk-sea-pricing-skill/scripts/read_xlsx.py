"""无依赖 xlsx 读取器（zip+XML），用法：
python3 read_xlsx.py <文件.xlsx>                 # 列出 sheet
python3 read_xlsx.py <文件.xlsx> <sheet名> [行数] # dump 内容（行号 列号:值）
"""
import zipfile, re, sys
from xml.etree import ElementTree as ET
NS={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def load(path):
    z=zipfile.ZipFile(path); ss=[]
    if 'xl/sharedStrings.xml' in z.namelist():
        root=ET.fromstring(z.read('xl/sharedStrings.xml'))
        for si in root.findall('m:si',NS):
            ss.append(''.join(t.text or '' for t in si.iter('{%s}t'%NS['m'])))
    wb=ET.fromstring(z.read('xl/workbook.xml'))
    rels=ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))
    rmap={r.get('Id'):r.get('Target') for r in rels}
    sheets=[(s.get('name'),'xl/'+rmap[s.get('{%s}id'%NS['r'])].lstrip('/').removeprefix('xl/')) for s in wb.find('m:sheets',NS)]
    sheets=[(n,t if t.startswith('xl/') else 'xl/'+t) for n,t in sheets]
    return z,ss,sheets
def colnum(ref):
    n=0
    for ch in re.match(r'([A-Z]+)',ref).group(1): n=n*26+ord(ch)-64
    return n
def readsheet(z,ss,target,maxrow=300):
    root=ET.fromstring(z.read(target)); rows={}
    for row in root.iter('{%s}row'%NS['m']):
        ri=int(row.get('r'))
        if ri>maxrow: break
        cells={}
        for c in row.findall('m:c',NS):
            v=c.find('m:v',NS)
            if v is None: continue
            val=v.text
            if c.get('t')=='s': val=ss[int(val)]
            cells[colnum(c.get('r'))]=val
        if cells: rows[ri]=cells
    return rows
if __name__=='__main__':
    z,ss,sheets=load(sys.argv[1])
    if len(sys.argv)==2:
        print([s[0] for s in sheets])
    else:
        t=[s for s in sheets if s[0]==sys.argv[2]][0][1]
        for ri,cs in sorted(readsheet(z,ss,t,int(sys.argv[3]) if len(sys.argv)>3 else 100).items()):
            print(ri,' | '.join(f"{ci}:{str(cs[ci])[:40]}" for ci in sorted(cs)))
