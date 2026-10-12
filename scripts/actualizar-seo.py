"""Actualiza metadatos sociales y sitemap con las páginas públicas del sitio."""
from pathlib import Path
from html.parser import HTMLParser
from html import escape
from urllib.parse import urljoin, urlparse
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://lelyliliana.com/'

class Page(HTMLParser):
 def __init__(self):
  super().__init__(); self.meta={}; self.title=''; self.in_title=False; self.redirect=False; self.images=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='title': self.in_title=True
  if tag=='meta':
   self.meta[a.get('property',a.get('name','')).lower()]=a.get('content','')
   if a.get('http-equiv','').lower()=='refresh': self.redirect=True
  if tag=='img':self.images.append(a)
 def handle_endtag(self,tag):
  if tag=='title': self.in_title=False
 def handle_data(self,data):
  if self.in_title:self.title+=data

def main():
 urls=[];total=0
 for p in sorted(ROOT.rglob('*.html')):
  rel=p.relative_to(ROOT).as_posix()
  if any(part.startswith('.') for part in p.relative_to(ROOT).parts):continue
  s=p.read_text(encoding='utf-8');page=Page();page.feed(s)
  if page.redirect:continue
  path=rel.removesuffix('index.html') if p.name=='index.html' else rel
  url=urljoin(BASE,path)
  if 'noindex' not in page.meta.get('robots','').lower() and rel!='mesa-steam-feedback/index.html':urls.append(url)
  title=page.meta.get('og:title') or page.title.strip()
  desc=page.meta.get('og:description') or page.meta.get('description','')
  if not title or not desc:raise ValueError(f'Falta título o descripción: {rel}')
  images=[a for a in page.images if urlparse(a.get('src','')).path.lower().endswith(('.jpg','.jpeg','.png','.webp'))]
  image=next((a for a in images if any(c in a.get('class','') for c in ['book-cover','portrait-photo'])),images[0] if images else None)
  imageurl=urljoin(url,image['src']) if image else BASE+'assets/img/perfil.jpg'
  alt=image.get('alt','') if image else 'Leli Liliana Díaz Izquierdo, ingeniera de sistemas y docente investigadora'
  if urlparse(imageurl).netloc!='lelyliliana.com' or not (ROOT/urlparse(imageurl).path.lstrip('/')).is_file():raise ValueError(f'Imagen no disponible: {imageurl}')
  kind=page.meta.get('og:type') or ('article' if '/articulos/' in rel else 'website')
  s=re.sub(r'^[ \t]*<meta\b[^>]*(?:property=["\']og:|name=["\']twitter:)[^>]*>\s*\n?', '',s,flags=re.M|re.I)
  s=re.sub(r'^[ \t]*<link\b[^>]*rel=["\']canonical["\'][^>]*>\s*\n?', '',s,flags=re.M|re.I)
  e=lambda x:escape(x,quote=True)
  tags=f'  <link rel="canonical" href="{e(url)}">\n'
  for key,value in [('og:title',title),('og:description',desc),('og:type',kind),('og:url',url),('og:site_name','Leli Liliana Díaz Izquierdo'),('og:locale','es_CO'),('og:image',imageurl),('og:image:alt',alt)]:tags+=f'  <meta property="{key}" content="{e(value)}">\n'
  for key,value in [('twitter:card','summary_large_image'),('twitter:title',title),('twitter:description',desc),('twitter:image',imageurl),('twitter:image:alt',alt)]:tags+=f'  <meta name="{key}" content="{e(value)}">\n'
  s=s.replace('</head>',tags+'</head>');p.write_text(s,encoding='utf-8');total+=1
 ET.register_namespace('', 'http://www.sitemaps.org/schemas/sitemap/0.9')
 root=ET.Element('{http://www.sitemaps.org/schemas/sitemap/0.9}urlset')
 for url in sorted(set(urls)):
  entry=ET.SubElement(root,'url');ET.SubElement(entry,'loc').text=url
 ET.indent(root,space='  ')
 ET.ElementTree(root).write(ROOT/'sitemap.xml',encoding='utf-8',xml_declaration=True)
 (ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+BASE+'sitemap.xml\n',encoding='utf-8')
 print(f'{total} páginas con metadatos; {len(set(urls))} URLs en sitemap.')

if __name__=='__main__':main()
