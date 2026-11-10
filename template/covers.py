import os
from playwright.sync_api import sync_playwright
from icons import I
D=os.getcwd(); CSS=open('style7.css').read().replace('DIR',D)+(open(os.environ['TITLECSS']).read().replace('DIR',D) if os.environ.get('TITLECSS') else '')
def P(n): return f"file://{D}/desenhado/{n}.png"
X="""
.cv{position:absolute;z-index:1;top:150px;bottom:120px;left:64px;right:64px;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;text-align:center}
.kick{font-family:NU;font-weight:900;font-size:26px;letter-spacing:3px;text-transform:uppercase;border:3px solid #1b1a17;border-radius:40px;padding:6px 18px;background:#fff}
.huge{font-family:NU;font-weight:900;color:#1b1a17;line-height:.95;letter-spacing:-3px}
.hl{background:linear-gradient(transparent 50%,#ffd43b 50%,#ffd43b 88%,transparent 88%);padding:0 10px}
.sub{font-family:PHS;font-size:44px;margin-top:24px;max-width:860px;line-height:1.1}
.st{position:absolute}
.circ{position:relative;display:inline-block}
.circ svg{position:absolute;left:-40px;top:-30px;width:calc(100% + 80px);height:calc(100% + 60px);overflow:visible}
.strike{position:relative;display:inline-block;color:#8b8577}
.strike:after{content:'';position:absolute;left:-10px;right:-10px;top:52%;height:12px;background:#1b1a17;transform:rotate(-4deg);border-radius:6px}
.fix{font-family:PHS;color:#2f6fed;font-size:80px;transform:rotate(-4deg);display:block;margin-top:-10px}
.ftape{display:inline-block;background:rgba(255,212,59,.92);padding:8px 34px;font-family:NU;font-weight:900;font-size:86px;box-shadow:3px 4px 0 rgba(0,0,0,.15);margin:8px 0}
.ftape.b{background:rgba(47,111,237,.95);color:#fff}
.bigpost{background:#ffe680;width:820px;padding:50px 50px 40px;transform:rotate(-2deg);box-shadow:8px 12px 0 rgba(0,0,0,.18);text-align:left;position:relative}
.bigpost:before{content:'';position:absolute;top:-22px;left:50%;margin-left:-80px;width:160px;height:40px;background:rgba(47,111,237,.55);transform:rotate(3deg)}
.bubble2{position:relative;background:#fff;border:5px solid #1b1a17;border-radius:50px;padding:46px 50px;box-shadow:9px 10px 0 #1b1a17;width:880px}
.bubble2:after{content:'';position:absolute;bottom:-46px;left:300px;width:60px;height:60px;background:#fff;border-right:5px solid #1b1a17;border-bottom:5px solid #1b1a17;transform:rotate(45deg) skew(10deg,10deg)}
.numbig{font-family:NU;font-weight:900;font-size:430px;line-height:.8;color:#fff;-webkit-text-stroke:12px #1b1a17;text-shadow:16px 16px 0 #2f6fed}
.split{display:flex;width:100%;gap:24px;margin-top:30px}
.split>div{flex:1;border:4px solid #1b1a17;border-radius:24px;box-shadow:8px 8px 0 #1b1a17;padding:20px;display:flex;flex-direction:column;align-items:center}
.split img{height:330px}
.split b{font-family:NU;font-weight:900;font-size:50px;-webkit-text-stroke:0}
.ic0{top:880px;left:50px}.ic1{top:880px;right:50px}
"""
def page(inner,ics,i):
    ic=''.join(f"<div class='ic ic{k}'>{I[x]}</div>" for k,x in enumerate(ics))
    return f"""<html><head><style>{CSS}{X}</style></head><body><svg width=0 height=0 style='position:absolute'><filter id='rough'><feTurbulence type='fractalNoise' baseFrequency='.04' numOctaves='2' seed='{i}'/><feDisplacementMap in='SourceGraphic' scale='4'/></filter></svg>
<div class='slide'><div class='head'><img src='file://{D}/head-desenhado.png'><span>Gabriel Almeida</span><i>01/07</i></div>{ic}<div class='cv'>{inner}</div>
<div class='bar'><span class='pill'>@gabrielalmeidamx</span><span class='pill save'>Salva pra depois</span><span class='pill'>Arrasta →</span></div></div></body></html>"""
CIRC="<svg viewBox='0 0 100 50' preserveAspectRatio='none'><path d='M8 26 Q6 4 50 4 Q96 4 94 26 Q92 46 50 46 Q8 46 10 22 Q14 10 30 8' fill='none' stroke='#2f6fed' stroke-width='2.2' stroke-linecap='round' filter='url(#rough)'/></svg>"
C=[
("01-blocos","Blocos tracejados",f"<div class='t1'>Por que você não</div><div class='tbox'><span>Escala</span></div><div class='tpost'><span>Mesmo com criativo bom?</span></div><img style='height:520px;margin-top:40px' src='{P('pensando')}'>",["question","chart"]),
("02-marca-texto","Marca-texto",f"<div class='kick'>Laboratório de Criativos</div><div class='huge' style='font-size:118px;margin-top:30px'>O criativo <span class='hl'>não morreu</span>.<br>Você parou de testar.</div><div class='sub'>Volume vence o gerenciador</div><img style='height:460px;margin-top:30px' src='{P('criativos-que-convertem')}'>",["pencil","sparkle"]),
("03-circulado","Palavra circulada",f"<div class='huge' style='font-size:112px;margin-top:20px'>O segredo do<br><span class='circ'>pagamento{CIRC}</span><br>na entrega</div><div class='sub' style='color:#2f6fed'>↳ Não é vender. É <b>receber</b>.</div><img style='height:480px;margin-top:30px' src='{P('pague-na-entrega')}'>",["arrowcurl","truck"]),
("04-riscado","Riscado e corrigido",f"<div class='huge' style='font-size:116px;margin-top:20px'>Pare de culpar o<br><span class='strike'>gerenciador</span></div><span class='fix'>seu criativo ✎</span><img style='height:520px;margin-top:20px' src='{P('meta-ads')}'>",["warning","pencil"]),
("05-fita","Fita adesiva",f"<div class='ftape' style='transform:rotate(-3deg)'>IA na operação</div><div class='ftape b' style='transform:rotate(2deg)'>de nutra:</div><div class='ftape' style='transform:rotate(-1deg);font-size:64px'>o que eu já automatizei</div><img style='height:500px;margin-top:30px' src='{P('ia-notebook')}'>",["bolt","gear"]),
("06-post-it","Post-it gigante",f"<div class='bigpost'><div style='font-family:PHS;font-size:40px;color:#2f6fed'>Lembrete pra quem opera nutra:</div><div class='huge' style='font-size:96px;margin-top:10px'>Acertar é sorte.<br><span class='hl'>Repetir é método.</span></div></div><img style='height:500px;margin-top:40px' src='{P('lupa')}'>",["sparkle","target"]),
("07-numero","Número gigante",f"<div style='display:flex;align-items:center;gap:30px;margin-top:20px'><div class='numbig'>3</div><div class='huge' style='font-size:84px;text-align:left'>erros que<br><span class='hl'>travam</span><br>sua escala</div></div><img style='height:480px;margin-top:50px' src='{P('chocado')}'>",["warning","chart"]),
("08-balao","Balão de fala",f"<div class='bubble2'><div class='huge' style='font-size:92px'>“Meu produto<br>parou de vender.”</div><div class='sub' style='margin:16px auto 0'>Antes de trocar de produto, olha isso</div></div><img style='height:480px;margin-top:70px' src='{P('analise-otimizacao')}'>",["eye","question"]),
("09-antes-depois","Antes × Depois",f"<div class='t1'>Minha operação</div><div class='tbox'><span>Antes × Depois</span></div><div class='split'><div style='background:#fff'><b style='color:#1b1a17'>Antes</b><img src='{P('frustrado')}'><span class='sub' style='margin-top:6px;font-size:36px'>Tudo passava por mim</span></div><div style='background:#d6f0df'><b style='color:#2b9a5a'>Depois</b><img src='{P('comemorando')}'><span class='sub' style='margin-top:6px;font-size:36px'>Cada área com dono</span></div></div>",["arrowcurl","star"]),
("10-figurinhas","Mural de figurinhas",f"<div class='t1'>Tudo que uma operação</div><div class='tbox'><span>Nutra</span></div><div class='tpost'><span>precisa ter (de verdade)</span></div><div style='display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:30px'>"+''.join(f"<img style='height:200px;transform:rotate({r}deg)' src='{P(x)}'>" for x,r in [('pote-proprio',-4),('trafego-meta-ads',3),('atendimento-x1',-2),('logistica-expedicao',2),('after-pay-cobranca',-3),('analise-metricas',4)])+"</div>",["sparkle","box"]),
]
OUT='out/modelos-capa'+os.environ.get('OUTSUF','');os.makedirs(OUT,exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,(slug,name,inner,ics) in enumerate(C):
        f=f'/tmp/cv{i}.html'; open(f,'w').write(page(inner,ics,i)); pg.goto('file://'+f); pg.wait_for_timeout(300); pg.screenshot(path=f'{OUT}/{slug}.png')
    # doodle sheet
    items=''.join(f"<div class='dd'><div class='ds'>{v}</div><span>{k}</span></div>" for k,v in I.items())
    html=f"<html><head><style>{CSS}.grid{{position:absolute;top:200px;left:60px;right:60px;display:grid;grid-template-columns:repeat(6,1fr);gap:20px 10px}}.dd{{display:flex;flex-direction:column;align-items:center}}.ds{{width:120px;height:120px}}.ds svg{{width:100%;height:100%;overflow:visible}}.dd span{{font-family:PHS;font-size:28px;margin-top:6px}}</style></head><body><svg width=0 height=0 style='position:absolute'><filter id='rough'><feTurbulence type='fractalNoise' baseFrequency='.04' numOctaves='2' seed='3'/><feDisplacementMap in='SourceGraphic' scale='4'/></filter></svg><div class='slide'><div class='cv' style='position:absolute;top:60px;left:0;right:0;text-align:center'><div class='tbox' style='display:inline-block'><span style='font-size:70px'>Desenhinhos</span></div></div><div class='grid'>{items}</div></div></body></html>"
    open('/tmp/dd.html','w').write(html); pg.goto('file:///tmp/dd.html'); pg.wait_for_timeout(300); pass
    b.close()
