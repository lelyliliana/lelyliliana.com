"""Genera el catálogo estático con unidades directas desde Aprende con Leli."""
from pathlib import Path
import argparse, html, json, re, subprocess, urllib.parse
from datetime import date

ROOT=Path(__file__).resolve().parents[1]
PLATAFORMA='https://lelyliliana.github.io/aprende-con-leli/'
AREAS=[('programacion','Programación'),('desarrollo-web','Desarrollo web'),('iot-robotica','Electrónica e IoT'),('datos-ia','Datos e IA'),('herramientas','Herramientas')]
# Organización editorial del sitio, independiente del orden de la plataforma.
ORDEN=['algoritmos','c','cpp','python','java','estructuras-datos','html-css','javascript','react','frontend','php','spring-boot','backend-java','fullstack','arduino','esp32','bases-datos-sql','r','inteligencia-artificial','git-github']
AREA_CURSO={'bases-datos-sql':'datos-ia','php':'desarrollo-web'}
ENFOQUES={
 'html-css':'Fundamentos de estructura y diseño para comenzar la ruta web.',
 'javascript':'Estudia el lenguaje y el navegador antes de pasar a React.',
 'react':'Profundiza en React; después puedes integrarlo en la ruta Frontend.',
 'frontend':'Ruta integradora: aplica HTML, CSS, JavaScript y React en un proyecto progresivo.',
 'php':'Alternativa para crear aplicaciones web con lógica en el servidor y SQLite.',
 'spring-boot':'Curso de tecnología: estudia Spring Boot y sus herramientas para construir APIs.',
 'backend-java':'Ruta aplicada: integra y experimenta con los proyectos de Spring Boot, desde sus contratos hasta su operación.',
 'fullstack':'Ruta integradora final: conecta una interfaz React con una API Spring Boot y una base de datos.',
}

def enlace_curso(id,titulos):
 return f'<a href="#curso-{html.escape(id,quote=True)}">{html.escape(titulos[id])}</a>'

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
   if label in ('Estudiar y practicar','Estudiar y ejecutar','Ver el módulo completo','Estudiar la lección'):label=grupo
   elif label in ('Práctica paso a paso','Resolver la práctica'):label=grupo+' · Práctica'
   elif label=='Desarrollo del caso':label=grupo+' · Desarrollo del caso'
   temas.append({'titulo':label,'url':url})
 if not temas:raise ValueError('Faltan unidades: '+c['id'])
 return {'id':c['id'],'titulo':c['title'],'area':AREA_CURSO.get(c['id'],c['area']),'nivel':c['level'],'descripcion':texto(lead.group(1)),'tecnologias':c['technologies'],'baseRecomendada':c.get('prerequisites',[]),'unidades':c.get('modules',len(temas)),'url':PLATAFORMA+c['internalPath'].removeprefix('./'),'temas':temas}

def render(c,titulos):
 esc=html.escape
 recomendado=', '.join(enlace_curso(x,titulos) for x in c['baseRecomendada'] if x in titulos)
 salida=f'<article class="project-card course-card" id="curso-{esc(c["id"])}" data-course-id="{esc(c["id"])}">\n<span class="tag">{esc(c["nivel"])}</span><h4>{esc(c["titulo"])}</h4><p>{esc(c["descripcion"])}</p>\n<p class="course-meta"><strong>Temas:</strong> {esc(" · ".join(c["tecnologias"]))}</p>\n'
 if c['id'] in ENFOQUES:salida+=f'<p class="course-meta"><strong>Enfoque:</strong> {esc(ENFOQUES[c["id"]])}</p>\n'
 if recomendado:salida+=f'<p class="course-meta"><strong>Base recomendada:</strong> {recomendado}</p>\n'
 salida+=f'<div class="course-actions"><a class="button button-secondary" href="{esc(c["url"],quote=True)}">Ver información del curso</a><a class="resource-link-button" href="{esc(c["temas"][0]["url"],quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="Comenzar {esc(c["titulo"],quote=True)}">Comenzar →</a></div>\n'
 mensaje=f'Hola, Leli. Estoy revisando el curso de {c["titulo"]} ({c["url"]}) y me interesa una asesoría personalizada. Necesito apoyo con…'
 whatsapp='https://wa.me/573103618296?text='+urllib.parse.quote(mensaje,safe='')
 salida+=f'<div class="course-advice"><p>¿Necesitas apoyo para resolver errores o aplicarlo a tu proyecto?</p><a class="button button-primary consultation-link" href="{esc(whatsapp,quote=True)}" target="_blank" rel="noopener noreferrer" aria-label="Consultar asesoría para {esc(c["titulo"],quote=True)} por WhatsApp"><svg class="whatsapp-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M21 11.5a9 9 0 0 1-13.4 7.8L3 21l1.7-4.6A9 9 0 1 1 21 11.5Z"/><path d="M8.3 7.2c-.6 0-1.3.8-1.3 1.8 0 2.8 4.2 7 7 7 1 0 1.8-.7 1.8-1.3l-2.3-1.3-.9.9a7.1 7.1 0 0 1-3.4-3.4l.9-.9-1.3-2.8Z"/></svg><span>Consultar asesoría</span></a></div>\n'
 tipo_unidad='módulos' if c['id']=='estructuras-datos' else 'unidades'
 salida+=f'<details class="course-topics"><summary>{c["unidades"]} {tipo_unidad} · {len(c["temas"])} accesos a temas y prácticas</summary><ul>\n'
 for t in c['temas']:salida+=f'<li><a href="{esc(t["url"],quote=True)}" target="_blank" rel="noopener noreferrer">{esc(t["titulo"])}</a></li>\n'
 return salida+'</ul></details></article>\n'

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--fuente',type=Path,required=True,help='Checkout de aprende-con-leli');parser.add_argument('--fecha-revision',type=date.fromisoformat,help='Fecha real de revisión de enlaces y organización (AAAA-MM-DD)');args=parser.parse_args();fuente=args.fuente.resolve()
 cursos=json.loads((fuente/'src/data/courses.json').read_text(encoding='utf-8'));catalogo=[extraer(c,fuente) for c in cursos if c['status']=='available']
 if len({c['id'] for c in catalogo})!=len(catalogo):raise ValueError('IDs repetidos')
 catalogo.sort(key=lambda c: ORDEN.index(c['id']) if c['id'] in ORDEN else len(ORDEN))
 archivo_catalogo=ROOT/'recursos/catalogo.json'
 fecha_revision=args.fecha_revision.isoformat() if args.fecha_revision else json.loads(archivo_catalogo.read_text(encoding='utf-8')).get('fechaRevisionEnlaces')
 titulos={c['id']:c['titulo'] for c in catalogo}
 nav='<nav class="hero-actions" aria-label="Cursos por área">'+''.join(f'<a class="button button-secondary" href="#{area}">{nombre}</a>' for area,nombre in AREAS)+'<a class="button button-secondary" href="#investigacion">Investigación</a></nav>\n'
 sections=nav+f'<section class="interests" aria-labelledby="courses-title"><h2 id="courses-title">Cursos abiertos</h2><p>{len(catalogo)} cursos con información y accesos directos. Despliega cada curso para entrar al tema que necesitas. El número de unidades indica el recorrido; los accesos incluyen temas, casos y prácticas de esas unidades. Los enlaces a GitHub se abren en una pestaña nueva.</p>\n'
 if fecha_revision:sections+=f'<p class="course-meta">Enlaces y organización revisados el <time datetime="{fecha_revision}">{date.fromisoformat(fecha_revision).strftime("%d/%m/%Y")}</time>.</p>\n'
 for area,nombre in AREAS:
  sections+=f'<section id="{area}" class="interests" aria-labelledby="area-{area}"><h3 id="area-{area}">{nombre}</h3>\n'
  if area=='datos-ia':
   sections+='<p>Comienza con SQL para consultar y organizar datos. Sigue la ruta de R para análisis e investigación, o la de Python para avanzar hacia inteligencia artificial.</p>\n'
   sections+=f'<p class="course-meta"><strong>Base para IA:</strong> {enlace_curso("python",titulos)}. Para comenzar con R no necesitas Python.</p>\n'
  elif area=='desarrollo-web':
   sections+=f'<p><strong>Ruta de interfaz:</strong> {enlace_curso("html-css",titulos)} → {enlace_curso("javascript",titulos)} → {enlace_curso("react",titulos)} → {enlace_curso("frontend",titulos)}.</p>\n'
   sections+=f'<p><strong>Ruta de servidor con Java:</strong> {enlace_curso("java",titulos)} y {enlace_curso("bases-datos-sql",titulos)} → {enlace_curso("spring-boot",titulos)} → {enlace_curso("backend-java",titulos)}. Integra interfaz y servidor en {enlace_curso("fullstack",titulos)}.</p>\n'
  sections+='<div class="project-grid">\n'
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
 # El resumen de portada debe contar el mismo catálogo que la página de recursos.
 portada=ROOT/'index.html';inicio=portada.read_text(encoding='utf-8')
 inicio=re.sub(r'\b\d+ cursos abiertos en cinco áreas',f'{len(catalogo)} cursos abiertos en cinco áreas',inicio)
 portada.write_text(inicio,encoding='utf-8')
 revision=subprocess.check_output(['git','-C',str(fuente),'rev-parse','HEAD'],text=True).strip()
 (ROOT/'recursos/catalogo.json').write_text(json.dumps({'revisionFuente':revision,'fechaRevisionEnlaces':fecha_revision,'cursos':catalogo},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(f'Catálogo: {len(catalogo)} cursos y {sum(len(c["temas"]) for c in catalogo)} accesos independientes.')

if __name__=='__main__':main()

