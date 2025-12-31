import json
from datetime import datetime, timezone
from pathlib import Path
from jinja2 import Environment, FileSystemLoader



with Path('data/portfolio.json').open(encoding='utf-8') as f:
    data = json.load(f)


data['current_year'] = datetime.now(tz=timezone.utc).year


if 'social_links' in data:
    for link in data['social_links']:
        if link.get('img_path'):
            with Path(link['img_path']).open(encoding='utf-8') as img_file:
                link['img_data'] = img_file.read()


env = Environment(loader=FileSystemLoader("templates/"), autoescape=True)
index_template = env.get_template('portfolio.html')

html_output = index_template.render(**data)


with Path('index.html').open('w', encoding='utf-8') as f:
    f.write(html_output)


print('HTML file generated successfully')