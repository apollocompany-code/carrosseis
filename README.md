# Carrosséis — @gabrielalmeidamx

Sistema de carrosséis do Instagram do Gabriel Almeida (Apollo Company): nutra, tráfego pago, IA e gestão.

## Estrutura

| Pasta | O que tem |
| --- | --- |
| `template/` | Motor de geração: scripts, estilos, fontes, avatares e desenhinhos |
| `template/poses/` | Avatar em pixel art (padrão) |
| `template/desenhado/` | Avatar "Desenhado" (lápis de cor) e figurinhas temáticas — usar quando o Gabriel disser **"Desenhado"** |
| `modelos/` | Catálogo visual: capas, modelos de slide, estilos de título, modelo giz de cera |
| `publicados/AAAA-MM-DD-tema/` | Slides finais de cada carrossel (01.png, 02.png…) usados na publicação |

## Identidade visual

- Fundo de caderno (grade pequena, pontilhado, pautado ou milimetrado), papel creme `#FFFDF6`
- Cores: preto `#1B1A17`, branco, azul `#2F6FED`, verde `#2B9A5A`, amarelo `#FFD43B` (vermelho só em alertas / modelo giz)
- Títulos: **Poppins** nas capas e headlines, **Sora** nos slides de conteúdo (Nunito como alternativa)
- Texto de conteúdo: **Patrick Hand SC** (letra de mão do Mapa Rabisco); maiúscula no início de tudo; negrito em títulos e destaques
- Desenhos com borda de figurinha; 66+ desenhinhos em `template/icons.py`
- Rodapé: `@gabrielalmeidamx` · `Salva pra depois` · `Arrasta →`

## Como gerar

```bash
cd template
pip install playwright && playwright install chromium
python3 render7.py slides7.json                                  # títulos em Nunito
TITLECSS=title-sora.css OUTSUF=-sora python3 render7.py slides7.json  # títulos em Sora
```

O arquivo `.json` define cada slide (`layout`: diagram, compare, list, steps, tip, cta). As imagens saem em `template/out/<slug>/`.

## Publicação

Cada slide em `publicados/` tem um link direto, usado para publicar no Instagram pelo Zernio:

`https://raw.githubusercontent.com/apollocompany-code/carrosseis/main/publicados/<pasta>/01.png`
