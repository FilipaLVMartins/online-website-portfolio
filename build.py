import json
from jinja2 import Environment, FileSystemLoader

def build_website():
    # 1. Load data from JSON file
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 2. Configure Jinja2 template engine
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # 3. Render final HTML (o ** passa as chaves do JSON como variáveis diretas)
    output_html = template.render(**data)

    # 4. Save to index.html
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(output_html)

    print("🚀 Success! 'index.html' generated successfully by Python.")

if __name__ == '__main__':
    build_website()