"""Genera el catálogo estático con unidades directas desde Aprende con Leli."""
from pathlib import Path
import argparse, html, json, re, subprocess, urllib.parse

ROOT=Path(__file__).resolve().parents[1]
PLATAFORMA='https://lelyliliana.github.io/aprende-con-leli/'
AREAS=[('programacion','Programación'),('desarrollo-web','Desarrollo web'),('iot-robotica','Electrónica e IoT'),('datos-ia','Datos e IA'),('herramientas','Herramientas')]

def texto(s):
 return html.unescape(re.sub(r'<[^>]+>','',s)).strip().removesuffix('→').strip()

def extraer(c,fuente):
 pagina=fuente/c['internalPath'].removeprefix('./')/'index.html'
 contenido=pagina.read_text(encoding='utf-8')
 lead=re.search(r'<p class="lead">([\s\S]*?)</p>',contenido)
 if not lead:raise ValueError('Falta descripción: '+c['id'])
 temas=[];seen=set()
 for block in re.finditer(r'<div class="unit-list">([\s\S]*?)</div>',contenido):
  antes=contenido[:block.start()];titulos=re.findall(r'<h3[^>]*>([\s\S]*?)</h3>',antes)
  grupo=texto(titulos[-1]) if titulos else c['title']
  for url,label in re.findall(r'<a[^>]*href="([^"]+)"[^>]*>([\s\S]*?)</a>',block.group(1)):
   url=html.unescape(url);label=texto(label)
   if 'SOLUCIONES.md' in url or label.startswith('Soluciones'):continue
   if not url.startswith('https://github.com/lelyliliana/'):raise ValueError('Destino no esperado: '+url)
   if re.search('Curso-(Lenguaje-de-Programacion|Desarrollo-de-Software)-',url):raise ValueError('Recurso universitario: '+url)
   if url in seen:continue
   seen.add(url)
   if label in ('Estudiar y practicar','Ver el módulo completo'):label=grupo
   temas.append({'titulo':label,'url':url})
 if not temas:raise ValueError('Faltan unidades: '+c['id'])
 return {'id':c['id'],'titulo':c['title'],'area':c['area'],'nivel':c['level'],'descripcion':texto(lead.group(1)),'tecnologias':c['technologies'],'baseRecomendada':c.get('prerequisites',[]),'url':PLATAFORMA+c['internalPath'].removeprefix('./'),'temas':temas}

def render(c,titulos):
 esc=html.escape
 recomendado=', '.join(titulos[x] for x in c['baseRecomendada'] if x in titulos)
 salida=f'<article class="project-card course-card" id="curso-{esc(c["id"])}" data-course-id="{esc(c["id"])}">\n<span class="tag">{esc(c["nivel"])}</span><h4>{esc(c["titulo"])}</h4><p>{esc(c["descripcion"])}</p>\n<p class="course-meta"><strong>Temas:</strong> {esc(" · ".join(c["tecnologias"]))}</p>\n'
 if recomendado:salida+=f'<p class="course-meta"><strong>Base recomendada:</strong> {esc(recomendado)}</p>\n'
 salida+=f'<div class="course-actions"><a class="button button-secondary" href="{esc(c["url"],quote=True)}">Ver información del curso</a><a class="resource-link-button" href="{esc(c["temas"][0]["url"],quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="Comenzar {esc(c["titulo"],quote=True)}">Comenzar →</a></div>\n'
 mensaje=f'Hola, Leli. Estoy revisando el curso de {c["titulo"]} ({c["url"]}) y me interesa una asesoría personalizada. Necesito apoyo con…'
 whatsapp='https://wa.me/573103618296?text='+urllib.parse.quote(mensaje,safe='')
 salida+=f'<div class="course-advice"><p>¿Necesitas apoyo para resolver errores o aplicarlo a tu proyecto?</p><a class="button button-primary" href="{esc(whatsapp,quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="Solicitar asesoría para {esc(c["titulo"],quote=True)}">Solicitar asesoría por WhatsApp →</a></div>\n'
 salida+=f'<details class="course-topics"><summary>Unidades y temas ({len(c["temas"])} accesos)</summary><ul>\n'
 for t in c['temas']:salida+=f'<li><a href="{esc(t["url"],quote=True)}" target="_blank" rel="noopener noreferrer">{esc(t["titulo"])}</a></li>\n'
 return salida+'</ul></details></article>\n'

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--fuente',type=Path,required=True,help='Checkout de aprende-con-leli');args=parser.parse_args();fuente=args.fuente.resolve()
 cursos=json.loads((fuente/'src/data/courses.json').read_text(encoding='utf-8'));catalogo=[extraer(c,fuente) for c in cursos if c['status']=='available']
 if len({c['id'] for c in catalogo})!=len(catalogo):raise ValueError('IDs repetidos')
 titulos={c['id']:c['titulo'] for c in catalogo}
 nav='<nav class="hero-actions" aria-label="Cursos por área">'+''.join(f'<a class="button button-secondary" href="#{area}">{nombre}</a>' for area,nombre in AREAS)+'<a class="button button-secondary" href="#investigacion">Investigación</a></nav>\n'
 sections=nav+f'<section class="interests" aria-labelledby="courses-title"><h2 id="courses-title">Cursos abiertos</h2><p>{len(catalogo)} cursos con información y accesos directos. Despliega las unidades de cada curso para entrar al tema que necesitas. Los enlaces a GitHub se abren en una pestaña nueva.</p>\n'
 for area,nombre in AREAS:
  sections+=f'<section id="{area}" class="interests" aria-labelledby="area-{area}"><h3 id="area-{area}">{nombre}</h3><div class="project-grid">\n'
  sections+=''.join(render(c,titulos) for c in catalogo if c['area']==area)
  sections+='</div></section>\n'
 sections+='</section>\n'
 p=ROOT/'recursos/index.html';s=p.read_text(encoding='utf-8');start=s.index('<nav class="hero-actions"');end=s.index('    <section id="investigacion"',start)
 extras=re.search(r'<section class="interests" aria-labelledby="examples-title">[\s\S]*?</section>',s[start:end])
 s=s[:start]+sections+(extras.group(0)+'\n' if extras else '')+s[end:]
 # Se conserva investigación y los accesos complementarios, evitando repetir el curso IA.
 start=s.find('    <section id="tecnologias-emergentes"')
 if start>=0:
  end=s.index('\n  </main>',start)
  s=s[:start]+s[end:]
 s=s.replace('Mis cursos, guías y ejemplos ahora están organizados como rutas de aprendizaje para que puedas comenzar desde cero, elegir un objetivo o entrar directamente al tema que necesitas.','Elige un curso, consulta qué aprenderás y entra directamente a sus unidades o temas. Puedes seguir el recorrido completo o repasar lo que necesites.')
 s=s.replace('La plataforma conecta los contenidos con sus repositorios fuente sin duplicar el material.','Los contenidos se organizan en cursos públicos con explicaciones, prácticas y proyectos.')
 s=s.replace('Explorar Aprende con Leli','Abrir la plataforma de aprendizaje')
 p.write_text(s,encoding='utf-8')
 revision=subprocess.check_output(['git','-C',str(fuente),'rev-parse','HEAD'],text=True).strip()
 (ROOT/'recursos/catalogo.json').write_text(json.dumps({'revisionFuente':revision,'cursos':catalogo},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(f'Catálogo: {len(catalogo)} cursos y {sum(len(c["temas"]) for c in catalogo)} accesos independientes.')

if __name__=='__main__':main()
