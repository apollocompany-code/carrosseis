import os
from playwright.sync_api import sync_playwright
from icons import I
D=os.getcwd()
CSS=open('style7.css').read().replace('DIR',D)+open('title-poppins.css').read().replace('DIR',D)
def P(n): return f"file://{D}/desenhado/{n}.png"
X=f"""
@font-face{{font-family:TT;src:url(file://{D}/titan-one-latin-400-normal.woff2)}}
@font-face{{font-family:IS;font-style:italic;src:url(file://{D}/instrument-serif-latin-400-italic.woff2)}}
@font-face{{font-family:JB;font-weight:700;src:url(file://{D}/jetbrains-mono-latin-700-normal.woff2)}}
@font-face{{font-family:TS;font-weight:800;src:url(file://{D}/sora-latin-800-normal.woff2)}}
.slide{{background-color:#fffdf6;background-image:linear-gradient(#ebe4d2 1.5px,transparent 1.5px),linear-gradient(90deg,#ebe4d2 1.5px,transparent 1.5px);background-size:30px 30px}}
.mono{{font-family:JB;font-weight:700;letter-spacing:2px;text-transform:uppercase}}
.ser{{font-family:IS;font-style:italic;color:#2f6fed}}
.g{{font-family:TT;text-transform:uppercase;line-height:.95;filter:url(#giz)}}
.box{{background:#fff;border:3px solid #1b1a17;border-radius:14px;box-shadow:5px 5px 0 #1b1a17}}
.d{{position:absolute;width:86px;height:86px}}.d svg{{width:100%;height:100%;overflow:visible}}
/*g3d*/.g{{filter:none!important;position:relative;line-height:1.08!important}}.g .gf{{position:relative;filter:url(#giz)}}.g .gb,.g .gw{{position:absolute;left:0;top:0;right:0;filter:none}}.g .gb{{color:#1b1a17;-webkit-text-stroke:16px #1b1a17;text-shadow:1px 1px 0 #1b1a17,2px 2px 0 #1b1a17,3px 3px 0 #1b1a17,4px 4px 0 #1b1a17,5px 5px 0 #1b1a17,6px 6px 0 #1b1a17,7px 7px 0 #1b1a17,8px 8px 0 #1b1a17,9px 9px 0 #1b1a17,10px 10px 0 #1b1a17}}.g .gw{{color:#fff;-webkit-text-stroke:9px #fff}}
.tag{{display:inline-block;font-family:JB;font-weight:700;font-size:15px;padding:2px 8px;border-radius:4px}}
"""
FILT="""<svg width=0 height=0 style='position:absolute'><filter id='rough'><feTurbulence type='fractalNoise' baseFrequency='.04' numOctaves='2' seed='2'/><feDisplacementMap in='SourceGraphic' scale='4'/></filter>
<filter id='giz' x='-5%' y='-5%' width='110%' height='110%'><feTurbulence type='fractalNoise' baseFrequency='1.4 .35' numOctaves='2' seed='7' result='n'/><feColorMatrix in='n' type='matrix' values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.3 1.55' result='m'/><feComposite in='SourceGraphic' in2='m' operator='in' result='t'/><feTurbulence type='fractalNoise' baseFrequency='.04' numOctaves='2' seed='3' result='d'/><feDisplacementMap in='t' in2='d' scale='5'/></filter></svg>"""
def dd(k,x,y,r=0,s=86): return f"<div class='d' style='left:{x}px;top:{y}px;width:{s}px;height:{s}px;transform:rotate({r}deg)'>{I[k]}</div>"
bar="<div class='bar'><span class='pill'>@gabrielalmeidamx</span><span class='pill save'>Salva pra depois</span><span class='pill'>Arrasta →</span></div>"
def g3(h):
    import re as _r
    return _r.sub(r"(<div class='g'[^>]*>)([^<]*)</div>",lambda m:m.group(1)+f"<span class='gb'>{m.group(2)}</span><span class='gw'>{m.group(2)}</span><span class='gf'>{m.group(2)}</span></div>",h)
def page(inner): inner=g3(inner); return f"<html><head><style>{CSS}{X}</style></head><body>{FILT}<div class='slide'>{inner}{bar}</div></body></html>"
sq=''.join(f"<span style='display:inline-flex;width:32px;height:32px;border:2.5px solid #1b1a17;border-radius:6px;align-items:center;justify-content:center;font-family:JB;font-size:16px;{'background:#2f6fed;color:#fff;' if k==1 else ''}'>{k}</span>" for k in range(1,8))
# E: diagrama
idx=''.join(f"<div style='display:flex;gap:10px;align-items:center;font-size:30px'><span class='mono' style='color:#2f6fed;font-size:20px'>0{k+1}</span>{t}</div>" for k,t in enumerate(['O erro mais caro','A parte fixa','A parte variável','Como testar','Faça hoje']))
E=f"""
<div style='position:absolute;top:44px;left:60px;right:60px;display:flex;align-items:center;justify-content:space-between'><div class='mono' style='font-size:22px'><span style='display:inline-block;width:16px;height:16px;background:#2f6fed;margin-right:10px'></span>Laboratório de criativos</div><div style='display:flex;gap:6px'>{sq}</div></div>
<div style='position:absolute;top:110px;left:0;right:0;text-align:center'>
<div class='t1' style='font-size:48px'>Seu criativo</div><div class='tbox' style='display:inline-block'><span style='font-size:96px'>Não morreu</span></div>
<div class='ser' style='font-size:44px;margin-top:8px'>(você mexeu na parte errada dele.)</div></div>
<svg style='position:absolute;inset:0' viewBox='0 0 1080 1350'><g stroke='#1b1a17' stroke-width='4' stroke-dasharray='10 9' fill='none' filter='url(#rough)'><path d='M540 640 Q380 600 300 520'/><path d='M540 640 Q700 600 780 520'/></g></svg>
<div class='box' style='position:absolute;left:60px;top:370px;width:400px;padding:16px 18px;background:#fff3bf;transform:rotate(-1.5deg)'><div style='display:flex;align-items:center;gap:10px'><div style='width:60px;height:60px'>{I['lock']}</div><b style='font-family:TP;font-weight:900;-webkit-text-stroke:0;font-size:46px'>Fixo</b></div><div style='font-size:30px;margin-top:6px'>✓ Mesma dor<br>✓ Mesmo gancho<br>✓ Mesmo kit</div><span class='tag' style='background:#1b1a17;color:#fff;margin-top:8px'>NÃO MEXE</span></div>
<div class='box' style='position:absolute;right:60px;top:370px;width:400px;padding:16px 18px;background:#dbe7fd;transform:rotate(1.5deg)'><div style='display:flex;align-items:center;gap:10px'><div style='width:60px;height:60px'>{I['flask']}</div><b style='font-family:TP;font-weight:900;-webkit-text-stroke:0;font-size:46px'>Variável</b></div><div style='font-size:30px;margin-top:6px'>○ Cenário<br>○ Quem fala<br>○ Formato</div><span class='tag' style='background:#2f6fed;color:#fff;margin-top:8px'>TESTA 1 POR VEZ</span></div>
<img style='position:absolute;left:50%;margin-left:-135px;top:650px;height:320px' src='{P('criativos-que-convertem')}'>
<div class='box' style='position:absolute;left:60px;right:60px;top:995px;padding:14px 22px;display:flex;justify-content:space-between;align-items:center'><div><div class='mono' style='font-size:16px;color:#8b8577'>Neste post</div><div style='display:grid;grid-template-columns:auto auto;gap:2px 34px;margin-top:4px'>{idx}</div></div><div style='width:110px;height:110px'>{I['chart']}</div></div>
{dd('bulb',40,110,-12)}{dd('fire',955,110,10)}{dd('sparkle',470,900,0,60)}{dd('arrowcurl',360,860,20,70)}
"""
# F: ficha
grid=''.join(f"<div class='box' style='padding:8px 12px;display:flex;gap:10px;align-items:center;box-shadow:3px 3px 0 #1b1a17'><div style='width:44px;height:44px;flex:none'>{I[ic]}</div><div><div class='mono' style='font-size:13px;color:#2f6fed'>0{k+1}</div><div style='font-family:TS;font-weight:800;font-size:24px;line-height:1'>{t}</div></div></div>" for k,(ic,t) in enumerate([('hook','Hook'),('headline','Body'),('megaphone','CTA'),('target','Dor'),('pin','Cenário'),('people','Quem fala')]))
F=f"""
<div style='position:absolute;top:44px;left:60px;right:60px;display:flex;align-items:center;justify-content:space-between'><div class='mono' style='font-size:22px'><span style='display:inline-block;width:16px;height:16px;background:#2f6fed;margin-right:10px'></span>Nº 01 — Criativo</div><div style='display:flex;gap:6px'>{sq}</div></div>
<div style='position:absolute;top:100px;right:60px;transform:rotate(-6deg);background:#ffd43b;border:3px solid #1b1a17;border-radius:30px;padding:5px 16px' class='mono'>Laboratório</div>
<div style='position:absolute;top:175px;right:60px;width:160px;height:160px;border-radius:50%;background:#1b1a17;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg);border:6px double #ffd43b'><span style='color:#ffd43b;font-size:26px'>★</span><b style='font-family:TP;font-weight:900;font-size:40px;-webkit-text-stroke:0;line-height:1;white-space:nowrap'>1 → 20</b><span class='mono' style='font-size:12px;white-space:nowrap'>vencedores</span></div>
<div style='position:absolute;top:130px;left:60px'><div class='g' style='font-size:100px'>Seu criativo</div><div class='g' style='font-size:100px;color:#2f6fed'>não morreu.</div></div>
<div style='position:absolute;top:385px;left:60px;right:60px'>
<div style='font-family:TS;font-weight:800;font-size:44px;line-height:1.05'>Você mexeu na parte errada dele</div>
<div class='ser' style='font-size:38px'>(e jogou fora um vencedor.)</div>
<div class='box' style='margin-top:18px;padding:12px 18px;display:flex;align-items:center;gap:16px'><div style='flex:1'><div class='mono' style='font-size:14px;color:#8b8577'>Você → criativo cansou</div><div style='font-family:TS;font-weight:800;font-size:28px'>Troco a dor, o hook e o CTA de uma vez?</div></div><div style='width:54px;height:54px;border-radius:50%;background:#2f6fed;border:3px solid #1b1a17;color:#fff;display:flex;align-items:center;justify-content:center;font-size:30px'>↑</div></div>
<div style='display:flex;gap:20px;margin-top:18px'>
<div style='flex:1.15'><div class='mono' style='font-size:15px;margin-bottom:8px'>O que tem num criativo ↓</div><div style='display:grid;grid-template-columns:1fr 1fr;gap:9px'>{grid}</div></div>
<div class='box' style='flex:1;padding:14px 16px;position:relative'><div class='mono' style='font-size:13px;color:#8b8577'>Relatório do teste</div><div style='font-family:TP;font-weight:900;font-size:38px'>Veredito</div>
<div style='position:absolute;top:22px;right:12px;transform:rotate(8deg);border:4px solid #2b9a5a;color:#2b9a5a;font-family:TP;font-weight:900;font-size:24px;padding:0 10px;border-radius:8px'>1 POR VEZ</div>
<div style='margin-top:8px'><span class='tag' style='background:#d6402b;color:#fff'>TROCA TUDO</span><div style='font-family:TS;font-weight:800;font-size:22px'>Perde o que vendia</div></div>
<div style='margin-top:8px'><span class='tag' style='background:#ffd43b'>TROCA 2+</span><div style='font-family:TS;font-weight:800;font-size:22px'>Não sabe o que funcionou</div></div>
<div style='margin-top:8px'><span class='tag' style='background:#2b9a5a;color:#fff'>TROCA 1</span><div style='font-family:TS;font-weight:800;font-size:22px'>Sabe por que deu certo</div></div></div></div>
<div style='margin-top:18px;background:#1b1a17;border-radius:12px;padding:14px 22px;font-family:JB;font-size:24px;color:#fff;width:640px'><span style='color:#ffd43b'>$</span> segura o fixo + testa 1 variável<br><span style='color:#2b9a5a'>✓ 1 vencedor vira 20</span></div></div>
<img style='position:absolute;right:40px;bottom:100px;height:250px' src='{P('lupa')}'>
{dd('sparkle',720,1010,0,50)}
"""
os.makedirs('out/capas-criativo2',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350})
    for s,h in [('E-diagrama',E),('F-ficha',F)]:
        open('/tmp/c.html','w').write(page(h)); pg.goto('file:///tmp/c.html'); pg.wait_for_timeout(400); pg.screenshot(path=f'out/capas-criativo2/{s}.png')
    b.close()
