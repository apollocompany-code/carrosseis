import json,sys,os,re
from playwright.sync_api import sync_playwright
from icons import I
D=os.getcwd()
def cap(t):
    if not isinstance(t,str): return t
    if re.fullmatch(r'[a-z0-9-]+',t) and (os.path.exists(f'desenhado/{t}.png') or os.path.exists(f'poses/{t}.png')): return t
    return re.sub(r'^((?:<[^>]+>|[^\wÀ-ÿ<])*)([a-zà-ÿ])',lambda m:m.group(1)+m.group(2).upper(),t,count=1)
def capall(o,skip=('pose','c','layout','icons','center','avatar')):
    if isinstance(o,str): return cap(o)
    if isinstance(o,list): return [capall(x) for x in o]
    if isinstance(o,dict): return {k:(v if k in skip else capall(v)) for k,v in o.items()}
    return o
d=json.load(open(sys.argv[1])); n=len(d['slides']); out=f"out/{d['slug']}"+os.environ.get('OUTSUF',''); os.makedirs(out,exist_ok=True)
AV=d.get('avatar','desenhado'); ADIR='desenhado' if AV=='desenhado' else 'poses'
def P(name): return f"file://{D}/{ADIR}/{name}.png"
CSS=open('style7.css').read().replace('DIR',D)+(open(os.environ['TITLECSS']).read().replace('DIR',D) if os.environ.get('TITLECSS') else '')
def title(T):
    return f"<div class='t1'>{T['pre']}</div><div class='tbox'><span>{T['box']}</span></div><div class='tpost'><span>{T['post']}</span></div>"
def body(s):
    L=s['layout']; h=''
    if L=='diagram':
        nodes=''.join(f"<div class='node n{k}'><img src='{P(img)}'><b>{t}</b></div>" for k,(t,img) in enumerate(s['nodes']))
        h=f"<div class='diagram'><svg class='lines' viewBox='0 0 940 560'><g stroke='#1b1a17' stroke-width='4' stroke-dasharray='10 10' fill='none' filter='url(#rough)'><path d='M470 280 L130 110'/><path d='M470 280 L810 110'/><path d='M470 280 L130 430'/><path d='M470 280 L810 430'/><path d='M470 280 L470 520'/></g></svg><div class='center'><img src='{P(s['center'])}'></div>{nodes}</div>"
    if L=='compare':
        b=''.join(f"<li><i class='x'>✕</i>{x}</li>" for x in s['bad']['items']); g=''.join(f"<li><i class='v'>✓</i>{x}</li>" for x in s['good']['items'])
        h=f"<div class='compare'><div class='col bad'><h3>{s['bad']['t']}</h3><ul>{b}</ul></div><div class='col good'><h3>{s['good']['t']}</h3><ul>{g}</ul></div></div>"
    if L=='list':
        h="<div class='rows'>"+''.join(f"<div class='row'><span class='rn'>0{k+1}</span><img src='{P(img)}'><div><b>{nm}</b><em>{tag}</em><p>{txt}</p></div></div>" for k,(img,nm,txt,tag) in enumerate(s['rows']))+"</div>"
    if L=='steps':
        h="<div class='steps'>"+''.join(f"<div><span class='{c}'>{k}</span><b>{l}</b><em>{dsc}</em></div>" for k,l,dsc,c in s['steps'])+"</div>"
        h+="<div class='cards'>"+''.join(f"<div class='card {c['c']}'><b class='tape'></b><small>{c['label']}</small><p>{c['text']}</p></div>" for c in s['cards'])+"</div>"
    if L=='tip':
        h="<div class='tipbox'><b class='tape'></b><small>⏱ Leva 5 minutos</small><ul>"+''.join(f"<li><span>☐</span>{x}</li>" for x in s['check'])+"</ul></div>"
    if L=='cta': h=f"<div class='big'>{s['big']}</div>"
    return h
def html(s,i):
    num=f"<div class='num'>{s['num']}</div>" if 'num' in s else ''
    bottom=''
    if 'pose' in s:
        st=f"<div class='sticky'>{s['sticky']}</div>" if 'sticky' in s else '<div></div>'
        bottom=f"<div class='bottom'>{st}<img class='pose' src='{P(s['pose'])}'><div class='spacer'></div></div>"
    ics=''.join(f"<div class='ic ic{k}'>{I[x]}</div>" for k,x in enumerate(s.get('icons',[])))
    last=i==n
    return f"""<html><head><style>{CSS}</style></head><body>
<svg width=0 height=0 style='position:absolute'><filter id='rough'><feTurbulence type='fractalNoise' baseFrequency='.04' numOctaves='2' seed='{i}'/><feDisplacementMap in='SourceGraphic' scale='4'/></filter></svg>
<div class='slide L{s['layout']}'>
<div class='head'><img src='file://{D}/head-desenhado.png'><span>{d['name']}</span><i>{i:02d}/{n:02d}</i></div>
{ics}
<div class='main'>{num}{title(s['title'])}{body(s)}{bottom}</div>
<div class='bar'><span class='pill'>{d['handle']}</span><span class='pill save'>Salva pra depois</span><span class='pill'>{'Compartilha ↗' if last else 'Arrasta →'}</span></div>
</div></body></html>"""
d['slides']=[capall(s) for s in d['slides']]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,s in enumerate(d['slides'],1):
        f=f'/tmp/v7s{i}.html'; open(f,'w').write(html(s,i)); pg.goto('file://'+f); pg.wait_for_timeout(300); pg.screenshot(path=f'{out}/{i:02d}.png')
    b.close()
print(out)
