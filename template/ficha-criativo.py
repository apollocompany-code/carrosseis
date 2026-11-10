import os,re
from playwright.sync_api import sync_playwright
from icons import I
exec(open('capas-criativo2.py').read().split("sq=''.join")[0])
N=7
def sqs(i): return ''.join(f"<span style='display:inline-flex;width:32px;height:32px;border:2.5px solid #1b1a17;border-radius:6px;align-items:center;justify-content:center;font-family:JB;font-size:16px;{'background:#2f6fed;color:#fff;' if k==i else ''}'>{k}</span>" for k in range(1,N+1))
def head(i,tema): return f"<div style='position:absolute;top:44px;left:60px;right:60px;display:flex;align-items:center;justify-content:space-between'><div class='mono' style='font-size:22px'><span style='display:inline-block;width:16px;height:16px;background:#2f6fed;margin-right:10px'></span>Nº 0{i} — {tema}</div><div style='display:flex;gap:6px'>{sqs(i)}</div></div>"
def title(a,b,sub,ital,size=104): return f"<div style='position:absolute;top:110px;left:60px;right:60px'><div class='g' style='font-size:{size}px'>{a}</div><div class='g' style='font-size:{size}px;color:#2f6fed'>{b}</div><div style='font-family:TS;font-weight:800;font-size:40px;line-height:1.05;margin-top:16px'>{sub}</div><div class='ser' style='font-size:36px'>{ital}</div></div>"
def card(ic,n,t,d,bg='#fff'): return f"<div class='box' style='padding:12px 14px;background:{bg};display:flex;gap:12px;align-items:flex-start'><div style='width:58px;height:58px;flex:none'>{I[ic]}</div><div><div class='mono' style='font-size:14px;color:#2f6fed'>{n}</div><div style='font-family:TS;font-weight:800;font-size:30px;line-height:1.05'>{t}</div><div style='font-size:28px;line-height:1.05;margin-top:4px'>{d}</div></div></div>"
def term(a,b): return f"<div style='background:#1b1a17;border-radius:12px;padding:14px 22px;font-family:JB;font-size:24px;color:#fff;display:inline-block'><span style='color:#ffd43b'>$</span> {a}<br><span style='color:#2b9a5a'>✓ {b}</span></div>"
def tag(t,bg,fg='#fff'): return f"<span class='tag' style='background:{bg};color:{fg};font-size:18px;padding:4px 10px'>{t}</span>"
def pose(n,h=250,r=40,b=100): return f"<img style='position:absolute;right:{r}px;bottom:{b}px;height:{h}px' src='{P(n)}'>"
def stamp(t,c): return f"<div style='position:absolute;top:150px;right:70px;transform:rotate(-10deg);border:5px solid {c};color:{c};font-family:TP;font-weight:900;font-size:40px;padding:2px 16px;border-radius:10px;background:#fffdf6'>{t}</div>"
S=[]
# 2 erro
arrow="<div style='font-family:TP;font-weight:900;font-size:40px;color:#2f6fed'>→</div>"
flow=arrow.join(f"<div class='box' style='padding:10px 14px;text-align:center;width:210px;{bg}'><div style='width:60px;height:60px;margin:0 auto'>{I[ic]}</div><div style='font-family:TS;font-weight:800;font-size:24px;line-height:1.05;margin-top:6px'>{t}</div></div>" for ic,t,bg in [('chartdown','Criativo cansa',''),('warning','Troca dor, hook e CTA',''),('arrowcurl','Volta pra estaca zero',''),('ban','Culpa o gerenciador','background:#fde3df')])
S.append(head(2,'O erro')+stamp('ERRO','#d6402b')+title('O erro','mais caro.','Trocar tudo quando o criativo cansa','(e jogar fora o que vendia.)')+
 f"<div style='position:absolute;top:560px;left:50px;right:50px;display:flex;align-items:center;gap:6px'>{flow}</div>"+
 f"<div class='box' style='position:absolute;top:800px;left:60px;width:620px;padding:16px 20px'><div class='mono' style='font-size:14px;color:#8b8577'>Você → criativo cansou</div><div style='font-family:TS;font-weight:800;font-size:30px'>“Morreu. Vou fazer outro do zero.”</div><div style='margin-top:10px'>{tag('ERRADO','#d6402b')}</div><div style='font-size:30px;margin-top:6px'>Você nem sabe qual parte cansou.</div></div>"+
 f"<div style='position:absolute;top:1030px;left:60px'>{term('troca tudo = perde o motivo da venda','próximo slide: o que não mexer')}</div>"+pose('frustrado',270))
# 3 fixo
S.append(head(3,'O fixo')+stamp('NÃO MEXE','#1b1a17')+title('A parte','fixa.','O que aparece em todos os seus vencedores','(se repete em 3 de 3, é fixo.)')+
 f"<div style='position:absolute;top:560px;left:60px;width:640px;display:flex;flex-direction:column;gap:14px'>{card('target','01','A dor','A mesma dor em todos os vencedores','#fff3bf')}{card('hook','02','O tipo de hook','Pergunta, choque, número… o mesmo jeito de abrir','#fff3bf')}{card('megaphone','03','O CTA','O mesmo pedido no final, levando pro X1','#fff3bf')}</div>"+
 f"<div style='position:absolute;top:620px;right:70px;width:220px;height:220px;transform:rotate(8deg)'>{I['lock']}</div>"+
 f"<div style='position:absolute;top:1030px;left:60px'>{term('fixo = o que vendeu em todos','é ele que faz o criativo escalar')}</div>"+pose('confiante-oculos',260))
# 4 variavel
S.append(head(4,'O variável')+stamp('TESTA AQUI','#2f6fed')+title('A parte','variável.','Todo o resto do criativo','(é aqui que você testa, não no fixo.)')+
 f"<div style='position:absolute;top:560px;left:60px;right:60px;display:grid;grid-template-columns:1fr 1fr;gap:14px'>{card('pin','01','Cenário','Casa, rua, carro, consultório','#dbe7fd')}{card('people','02','Quem fala','Você, cliente, especialista','#dbe7fd')}{card('quote','03','A frase do hook','Outras palavras, mesmo tipo de hook','#dbe7fd')}{card('headline','04','O body','Como você conta: história, prova, explicação','#dbe7fd')}</div>"+
 f"<div style='position:absolute;top:1000px;left:60px'>{term('variável = 1 troca por teste','você sabe o que funcionou')}</div>"+pose('ideia',240,40,110))
# 5 como testar
st=''.join(f"<div style='flex:1;text-align:center'><div style='width:120px;height:120px;margin:0 auto;border-radius:50%;border:4px solid #1b1a17;box-shadow:6px 6px 0 #1b1a17;background:{c};display:flex;align-items:center;justify-content:center;font-family:TP;font-weight:900;font-size:56px'>{n}</div><div style='font-family:TS;font-weight:800;font-size:30px;margin-top:12px'>{t}</div><div style='font-size:28px;line-height:1.05'>{d}</div></div>" for n,t,d,c in [('1','Separa','Seus 3 últimos vencedores','#7fd3a0'),('2','Marca','O que se repete nos 3','#ffd43b'),('3','Troca','Uma variável por vez','#8db3f5')])
S.append(head(5,'Como testar')+title('Testa sem','perder o vencedor.','3 passos, nessa ordem','(pula um e o teste não vale.)',78)+
 f"<div style='position:absolute;top:560px;left:60px;right:60px;display:flex;gap:10px;position:absolute'>{st}</div>"+
 f"<div class='box' style='position:absolute;top:860px;left:60px;width:640px;padding:16px 20px'><div class='mono' style='font-size:14px;color:#8b8577'>Exemplo de teste</div><div style='font-size:30px;line-height:1.1;margin-top:4px'>Mesma dor, mesmo hook, mesmo CTA.<br>Muda só <b style='background:#ffd43b;padding:0 4px'>quem fala</b>. Ganhou? Esse vira o novo fixo.</div></div>"+
 f"<div style='position:absolute;top:1060px;left:60px'>{term('1 vencedor + 1 variável = 1 teste','sem perder o que já vende')}</div>"+pose('checklist-operacao',260))
# 6 faça hoje
rows=''.join(f"<tr><td>Criativo {k}</td><td></td><td></td><td></td></tr>" for k in ('A','B','C'))
S.append(head(6,'Faça hoje')+stamp('5 MIN','#2b9a5a')+title('Faça','hoje.','Descobre o seu fixo em 5 minutos','(papel e caneta resolvem.)')+
 f"<div class='box' style='position:absolute;top:560px;left:60px;right:60px;padding:16px 22px'><div style='font-size:34px;line-height:1.3'>☐ Abre os 3 últimos criativos que venderam<br>☐ Preenche a tabela abaixo<br>☐ O que repetir nas 3 linhas é o seu fixo</div>"+
 f"<table style='width:100%;border-collapse:collapse;margin-top:14px;font-size:28px'><tr style='font-family:TS;font-weight:800;font-size:24px;background:#fff3bf'><td style='padding:8px;border:2.5px solid #1b1a17'></td><td style='border:2.5px solid #1b1a17;padding:8px'>Dor</td><td style='border:2.5px solid #1b1a17;padding:8px'>Hook</td><td style='border:2.5px solid #1b1a17;padding:8px'>CTA</td></tr>{rows.replace('<td>','<td style=border:2.5px\\ solid\\ #1b1a17;padding:8px;height:48px>')}</table></div>"+pose('notebook-mesa',230,40,100))
# 7 cta
S.append(head(7,'Escala previsível')+title('Um vencedor','vira vinte.','Quando você sabe o que mexer','(e o que nunca mexer.)')+
 f"<div style='position:absolute;top:580px;left:60px;right:60px;text-align:center'><div style='display:inline-block;background:#fff;border:4px dashed #2f6fed;border-radius:60px;padding:22px 40px;font-size:46px'>Comenta <b style='background:#ffd43b;padding:0 8px'>ESCALA</b> que eu te chamo no direct</div>"+
 f"<div style='margin-top:30px;display:flex;justify-content:center;gap:18px'>{tag('SALVA','#1b1a17')}{tag('MANDA PRA UM PRODUTOR','#2f6fed')}{tag('SEGUE','#2b9a5a')}</div>"+
 f"<div style='background:#ffe680;width:520px;margin:40px 0 0 0;padding:20px;transform:rotate(-3deg);font-size:32px;text-align:left;box-shadow:4px 6px 0 rgba(0,0,0,.18)'>Para mais dicas sobre o universo do Nutra, siga <b>@gabrielalmeidamx</b>. Falow!</div></div>"+pose('apontando-voce',330,50,100))
os.makedirs('out/criativo-nao-morreu',exist_ok=True)
import shutil; shutil.copy('out/capas-criativo2/F-ficha.png','out/criativo-nao-morreu/01.png')
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350})
    for i,h in enumerate(S,2):
        html=page(h)
        if i==N: html=html.replace('Arrasta →','Compartilha ↗')
        open('/tmp/f.html','w').write(html); pg.goto('file:///tmp/f.html'); pg.wait_for_timeout(400); pg.screenshot(path=f'out/criativo-nao-morreu/0{i}.png')
    b.close()
