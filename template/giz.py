import os
from playwright.sync_api import sync_playwright
from icons import I
D=os.getcwd()
CSS=open('style7.css').read().replace('DIR',D)
def P(n): return f"file://{D}/desenhado/{n}.png"
X=f"""
@font-face{{font-family:TT;src:url(file://{D}/titan-one-latin-400-normal.woff2)}}
.slide.paper{{background:#fbfaf6;background-image:radial-gradient(rgba(0,0,0,.025) 1px,transparent 1.2px);background-size:6px 6px}}
.g{{font-family:TT;text-transform:uppercase;line-height:.98;letter-spacing:1px;filter:url(#giz);text-align:center}}
.ac{{color:var(--ac)}}
.burst{{position:absolute;width:90px;height:110px}}
"""
FILT="""<svg width=0 height=0 style='position:absolute'>
<filter id='giz' x='-5%' y='-5%' width='110%' height='110%'>
<feTurbulence type='fractalNoise' baseFrequency='1.4 .35' numOctaves='2' seed='7' result='n'/>
<feColorMatrix in='n' type='matrix' values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.3 1.55' result='m'/>
<feComposite in='SourceGraphic' in2='m' operator='in' result='t'/>
<feTurbulence type='fractalNoise' baseFrequency='.04' numOctaves='2' seed='3' result='d'/><feDisplacementMap in='t' in2='d' scale='5'/></filter>
<filter id='rough'><feTurbulence type='fractalNoise' baseFrequency='.04' numOctaves='2' seed='2'/><feDisplacementMap in='SourceGraphic' scale='4'/></filter></svg>"""
def burst(side,ac):
    if side=='l': p="M80 20 L30 0 M86 55 L10 55 M80 90 L30 110"
    else: p="M10 20 L60 0 M4 55 L80 55 M10 90 L60 110"
    return f"<svg viewBox='0 0 90 110'><path d='{p}' stroke='{ac}' stroke-width='9' stroke-linecap='round' fill='none' filter='url(#giz)'/></svg>"
def page(l1,l2,l3,ac,pose,obj,bar=True):
    under=f"<svg style='display:block;margin:6px auto 0;width:520px;height:40px' viewBox='0 0 500 40'><path d='M8 22 Q250 2 492 18 M30 30 Q260 14 470 28' stroke='{ac}' stroke-width='9' fill='none' stroke-linecap='round' filter='url(#giz)'/></svg>"
    b="<div class='bar'><span class='pill'>@gabrielalmeidamx</span><span class='pill save'>Salva pra depois</span><span class='pill'>Arrasta →</span></div>" if bar else ''
    return f"""<html><head><style>{CSS}{X}.g{{color:#151515}}.g.ac{{color:var(--ac)}}</style></head><body>{FILT}<div class='slide paper' style='--ac:{ac}'>
<div style='position:absolute;top:56px;left:20px;right:20px'>
<div class='g' style='font-size:128px'>{l1}</div>
<div style='position:relative'><div class='burst' style='left:-6px;top:14px'>{burst('l',ac)}</div><div class='g ac' style='font-size:136px;margin:0 70px'>{l2}</div><div class='burst' style='right:-6px;top:14px'>{burst('r',ac)}</div></div>
<div class='g' style='font-size:128px'>{l3}</div>{under}</div>
<img style='position:absolute;left:130px;bottom:118px;height:600px' src='{P(pose)}'>
<div style='position:absolute;right:80px;bottom:230px;width:400px'>{obj}</div>{b}</div></body></html>"""
ban=lambda: f"<img style='width:100%' src='file://{D}/giz-proibido.png'>"
S=[('giz-vermelho',page('Palavras','Que matam','Seu criativo','#e0301e','pare',ban())),
   ('giz-azul',page('Palavras','Que matam','Seu criativo','#2f6fed','pare',ban())),
   ('giz-verde',page('O pedido','Entregue','É o que conta','#2b9a5a','joinha',f"<div style='width:330px;margin-left:50px'>{I['truck']}</div>"))]
os.makedirs('out/modelo-giz',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350})
    for slug,h in S:
        open('/tmp/g.html','w').write(h); pg.goto('file:///tmp/g.html'); pg.wait_for_timeout(400); pg.screenshot(path=f'out/modelo-giz/{slug}.png')
    b.close()
