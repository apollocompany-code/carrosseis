import os
from playwright.sync_api import sync_playwright
from icons import I
D=os.getcwd(); CSS=open('style7.css').read().replace('DIR',D)
def P(n): return f"file://{D}/desenhado/{n}.png"
X=f"""
@font-face{{font-family:AN;src:url(file://{D}/anton-latin-400-normal.woff2)}}
@font-face{{font-family:IS;font-style:italic;src:url(file://{D}/instrument-serif-latin-400-italic.woff2)}}
@font-face{{font-family:JB;font-weight:700;src:url(file://{D}/jetbrains-mono-latin-700-normal.woff2)}}
.cray{{font-family:AN;text-transform:uppercase;line-height:.95;filter:url(#crayon);letter-spacing:1px}}
.blue{{color:#2f6fed}}.grn{{color:#2b9a5a}}
.mono{{font-family:JB;font-weight:700;letter-spacing:3px;text-transform:uppercase}}
.ser{{font-family:IS;font-style:italic;color:#2f6fed}}
.box{{background:#fff;border:3px solid #1b1a17;border-radius:12px;box-shadow:5px 5px 0 #1b1a17}}
"""
FILT="""<svg width=0 height=0 style='position:absolute'>
<filter id='rough'><feTurbulence type='fractalNoise' baseFrequency='.04' numOctaves='2' seed='2'/><feDisplacementMap in='SourceGraphic' scale='4'/></filter>
<filter id='crayon' x='-5%' y='-5%' width='110%' height='110%'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' seed='4' result='n'/>
<feColorMatrix in='n' type='matrix' values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -1.4 1.75' result='m'/>
<feComposite in='SourceGraphic' in2='m' operator='in' result='t'/><feTurbulence type='fractalNoise' baseFrequency='.05' numOctaves='2' seed='9' result='d'/><feDisplacementMap in='t' in2='d' scale='6'/></filter></svg>"""
def page(inner,head=True,bar=True,extra=''):
    h="<div class='head'><img src='file://"+D+"/head-desenhado.png'><span>Gabriel Almeida</span><i></i></div>" if head else ''
    b="<div class='bar'><span class='pill'>@gabrielalmeidamx</span><span class='pill save'>Salva pra depois</span><span class='pill'>Arrasta →</span></div>" if bar else ''
    return f"<html><head><style>{CSS}{X}{extra}</style></head><body>{FILT}<div class='slide'>{h}{inner}{b}</div></body></html>"
S=[]
# 1 capa crayon
S.append(('capa-escrita-desenhada',page(f"""
<div style='position:absolute;top:150px;left:0;right:0;text-align:center'>
<div class='cray' style='font-size:200px'>Palavras</div>
<div class='cray blue' style='font-size:200px'>que matam</div>
<div class='cray' style='font-size:170px'>seu criativo</div></div>
<img style='position:absolute;left:150px;bottom:150px;height:470px' src='{P("cetico")}'>
<div style='position:absolute;right:150px;bottom:230px;width:300px;height:300px'>{I['ban']}</div>
<div style='position:absolute;right:120px;bottom:190px;width:120px;height:120px;transform:rotate(12deg)'>{I['headline']}</div>
""")))
# 2 ficha
grid=''.join(f"<div class='box' style='padding:10px 14px'><div class='mono blue' style='font-size:18px'>0{k+1}</div><div style='font-family:NU;font-weight:900;font-size:30px'>{t}</div></div>" for k,t in enumerate(['Pergunta','Dor','Número','Polêmica','Antes/depois','Prova']))
sq=''.join(f"<span style='display:inline-flex;width:36px;height:36px;border:2.5px solid #1b1a17;border-radius:6px;align-items:center;justify-content:center;font-family:JB;font-size:18px;{'background:#2f6fed;color:#fff;' if k==2 else ''}'>{k}</span>" for k in range(1,8))
S.append(('ficha-gancho',page(f"""
<div style='position:absolute;top:60px;left:64px;right:64px;display:flex;justify-content:space-between;align-items:center'>
<div class='mono' style='font-size:24px'><span style='display:inline-block;width:18px;height:18px;background:#2f6fed;margin-right:12px'></span>Nº 02 — Gancho</div><div style='display:flex;gap:6px'>{sq}</div></div>
<div style='position:absolute;top:120px;right:70px;transform:rotate(-6deg);background:#ffd43b;border:3px solid #1b1a17;border-radius:30px;padding:6px 18px' class='mono'>Laboratório de criativos</div>
<div style='position:absolute;top:190px;right:90px;width:190px;height:190px;border-radius:50%;background:#1b1a17;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;transform:rotate(-10deg);border:6px double #ffd43b'><span style='color:#ffd43b;font-size:30px'>★</span><b style='font-family:NU;font-weight:900;font-size:58px;-webkit-text-stroke:0;line-height:1'>3 seg</b><span class='mono' style='font-size:14px'>pra prender</span></div>
<div style='position:absolute;top:170px;left:64px'><div class='cray' style='font-size:210px;text-transform:none'>Gancho<span class='blue'>.</span></div></div>
<div style='position:absolute;top:400px;left:64px;right:64px'>
<div style='font-family:NU;font-weight:900;font-size:50px;line-height:1.05'>O que faz o dedo parar</div>
<div class='ser' style='font-size:44px'>(antes de você gastar com tráfego.)</div>
<div class='box' style='margin-top:22px;padding:14px 20px;display:flex;align-items:center;gap:20px'><div style='flex:1'><div class='mono' style='font-size:16px;color:#8b8577'>Você → criativo novo</div><div style='font-family:NU;font-weight:800;font-size:32px'>Começo falando do produto ou da dor?</div></div><div style='width:60px;height:60px;border-radius:50%;background:#2f6fed;border:3px solid #1b1a17;color:#fff;display:flex;align-items:center;justify-content:center;font-size:34px'>↑</div></div>
<div style='display:flex;gap:22px;margin-top:22px'>
<div style='flex:1.2'><div class='mono' style='font-size:16px;margin-bottom:8px'>Tipos de gancho ↓</div><div style='display:grid;grid-template-columns:1fr 1fr;gap:10px'>{grid}</div>
<div style='margin-top:12px;display:flex;align-items:center;gap:12px'><span style='background:#1b1a17;color:#fff;border-radius:30px;padding:6px 16px;font-family:NU;font-weight:900;font-size:22px'>+ Testa 3 por semana</span><span class='ser' style='font-size:34px'>no mínimo.</span></div></div>
<div class='box' style='flex:1;padding:16px 18px;position:relative'><div class='mono' style='font-size:14px;color:#8b8577'>Relatório do criativo</div><div style='font-family:NU;font-weight:900;font-size:40px'>Veredito</div>
<div style='position:absolute;top:30px;right:14px;transform:rotate(8deg);border:4px solid #2b9a5a;color:#2b9a5a;font-family:NU;font-weight:900;font-size:30px;padding:2px 12px;border-radius:8px'>DOR</div>
<div style='margin-top:12px'><span class='mono' style='font-size:13px;background:#d6402b;color:#fff;padding:2px 8px'>Red flag</span><div style='font-family:NU;font-weight:800;font-size:24px'>Começa com o nome do produto</div></div>
<div style='margin-top:10px'><span class='mono' style='font-size:13px;background:#ffd43b;padding:2px 8px'>Yellow flag</span><div style='font-family:NU;font-weight:800;font-size:24px'>Gancho genérico</div></div>
<div style='margin-top:10px'><span class='mono' style='font-size:13px;background:#2b9a5a;color:#fff;padding:2px 8px'>Green flag</span><div style='font-family:NU;font-weight:800;font-size:24px'>Fala a dor em 1 frase</div></div></div></div>
<div style='margin-top:22px;background:#1b1a17;border-radius:12px;padding:18px 24px;font-family:JB;font-size:26px;color:#fff'><span style='color:#ffd43b'>$</span> gancho bom = dor + 1 frase + 3 segundos<br><span style='color:#2b9a5a'>✓ pronto pra testar</span></div></div>
<img style='position:absolute;right:30px;bottom:96px;height:150px' src='{P("lupa")}'>
""",head=False)))
# 3 lista com cargo
rows=[('eye','CPM','Termômetro do leilão','Quanto custa mil pessoas verem o anúncio'),('cursor','CTR','Medidor de gancho','De cada 100 que viram, quantos clicaram'),('handcoin','CPC','Custo da atenção','Quanto você paga por cada clique'),('cart','Conversão','Teste da oferta','De quem clicou, quantos compraram'),('receipt','CPA','Custo da venda','Quanto custa cada pedido gerado'),('truck','Taxa de entrega','A métrica do after pay','Dos pedidos, quantos foram entregues e pagos')]
R=''.join(f"<div class='box' style='display:flex;align-items:center;gap:18px;padding:10px 16px;box-shadow:none;border-width:2.5px;border-radius:14px'><span style='font-family:NU;font-weight:900;font-size:30px;color:#2f6fed;width:50px'>0{k+1}</span><div style='width:76px;height:76px;flex:none;background:#f4efe1;border:2.5px solid #1b1a17;border-radius:14px;padding:8px'>{I[ic]}</div><div><div><b style='font-family:NU;font-weight:900;font-size:34px;-webkit-text-stroke:0'>{n}</b> <span style='font-family:NU;font-weight:900;font-size:22px;color:#2f6fed;margin-left:8px'>{role}</span></div><div style='font-size:30px'>{dsc}</div></div></div>" for k,(ic,n,role,dsc) in enumerate(rows))
S.append(('lista-com-cargo',page(f"""
<div style='position:absolute;top:150px;left:64px;right:64px'>
<div style='font-family:NU;font-weight:900;font-size:26px;color:#2f6fed;letter-spacing:1px;text-transform:uppercase'>Tráfego 1 de 3 · 6 métricas</div>
<div style='display:flex;align-items:flex-end;justify-content:space-between'><div style='font-family:NU;font-weight:900;font-size:72px;line-height:1;letter-spacing:-2px'>Métricas <span class='blue'>que importam</span></div></div>
<div style='font-size:34px;margin-top:6px'>E o que cada uma te conta sobre a operação.</div>
<div style='display:flex;flex-direction:column;gap:12px;margin-top:22px'>{R}</div></div>
<img style='position:absolute;right:40px;top:40px;height:130px' src='{P("analise-metricas")}'>
""")))
# doodle sheets
def sheet(keys,title):
    items=''.join(f"<div class='dd'><div class='ds'>{I[k]}</div><span>{k}</span></div>" for k in keys)
    return page(f"<div style='position:absolute;top:60px;left:0;right:0;text-align:center'><div class='cray' style='font-size:110px'>{title}</div></div><div style='position:absolute;top:240px;left:60px;right:60px;display:grid;grid-template-columns:repeat(5,1fr);gap:26px 10px'>{items}</div>",head=False,bar=False,extra=".dd{display:flex;flex-direction:column;align-items:center}.ds{width:130px;height:130px}.ds svg{width:100%;height:100%;overflow:visible}.dd span{font-family:PHS;font-size:28px;margin-top:6px}")
S.append(('desenhinhos-trafego-vendas',sheet(['cursor','ads','cart','pricetag','coins','receipt','percent','play','thumbsup','fire','crown','gauge','abtest','gift','chartdown','handcoin','phonecheck','headline','quote','ban','megaphone','funnel','target','money','chart'],'Tráfego <span class=blue>&</span> vendas')))
os.makedirs('out/modelos-v2',exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350})
    for slug,h in S:
        open('/tmp/s.html','w').write(h); pg.goto('file:///tmp/s.html'); pg.wait_for_timeout(350); pg.screenshot(path=f'out/modelos-v2/{slug}.png')
    b.close()
