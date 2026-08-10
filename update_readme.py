import feedparser
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from datetime import datetime

# Configuração de sessão com retries
session = requests.Session()
retry = Retry(connect=5, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# URL do feed RSS
blog_rss_url = "https://pedrobiqua.github.io/feed.xml"
response = session.get(blog_rss_url, verify=True)
rss_feed = feedparser.parse(response.content)

# Limite máximo de posts exibidos
MAX_POST_NUM = 5

# Início da lista de posts no formato Markdown
latest_blog_post_list = "## 📄 Blog Posts <br>\n"

# Iterar pelos posts no feed
for idx, entry in enumerate(rss_feed.entries):
    # Filtrar pela categoria "Blog"
    if not any(category['term'] == "Blog" for category in entry.get('tags', [])):
        continue

    if idx >= MAX_POST_NUM:
        break

    # Formatar a data de publicação
    published_date = datetime.strptime(entry.published, "%Y-%m-%dT%H:%M:%S%z")
    formatted_date = published_date.strftime("%Y/%m/%d")

    # Adicionar o post à lista
    latest_blog_post_list += f"- [{formatted_date} - {entry.title.strip()}]({entry.link}) <br>\n"

# Texto inicial do README
markdown_text = """
### Hi guys, welcome to my GitHub👋

- 🧑‍💻 I'm currently work with this languages C++, Python and Java
- 📫 How to reach me: pedrobiqua@outlook.com
- 👨‍💻 My blog:  <a href="https://pedrobiqua.dev.br/" target="_blank">pedrobiqua.dev</a>
- 🧑‍🏫 Languages: Portuguese 🇧🇷, English 🇺🇸, Japanese 🇯🇵

<br>

<p align="center">
    <a href="https://github.com/pedrobiqua" target="_blank"><img alt="GitHub" src="https://img.shields.io/badge/-@pedrobiqua-181717?style=flat-square&logo=GitHub&logoColor=white"></a>
    <a href="https://www.linkedin.com/in/pedrobiqua" target="_blank"><img alt="LinkedIn" src="https://img.shields.io/badge/-LinkedIn-0077B5?style=flat-square&logo=Linkedin&logoColor=white"></a>
</p>

<p align="center">
    <a href="https://github.com/pedrobiqua?tab=repositories" target="_blank"><img alt="Code" src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white"></a>
    <a href="https://github.com/pedrobiqua?tab=repositories&language=python" target="_blank"><img alt="python" src="https://img.shields.io/badge/-python-3776AB?style=flat-square&logo=Python&logoColor=white"></a>
    <a href="https://github.com/pedrobiqua?tab=repositories&language=c%2B%2B" target="_blank"><img alt="C++" src="https://img.shields.io/badge/-C%2B%2B-00599C?style=flat-square&logo=C%2B%2B&logoColor=white"></a>
    <a href="https://github.com/pedrobiqua?tab=repositories&language=typescript" target="_blank"><img alt="C++" src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"></a>
    <a href="#" target="_blank"><img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?style=flat-square&logo=ubuntu&logoColor=white"></a>
</p>

<p align="center">
    <a href="#"><img alt="Visual Studio Code" src="https://custom-icon-badges.demolab.com/badge/Visual%20Studio%20Code-0078d7.svg?style=flat-square&logo=vsc&logoColor=white"></a>
    <a href="#"><img alt="NeoVim" src="https://img.shields.io/badge/Neovim-57A143?style=flat-square&logo=neovim&logoColor=fff"></a>
</p>

<p align="center">
    <a href="https://github.com/pedrobiqua?tab=followers" target="_blank"><img alt="Updates" src="https://img.shields.io/badge/--000000?style=flat-square&logo=RSS&logoColor=white"></a>
    <a href="https://github.com/pedrobiqua/pedrobiqua" target="_blank"><img alt="GitHub hits" src="https://img.shields.io/github/last-commit/pedrobiqua/pedrobiqua?label=profile%20updated&style=flat-square"></a>
</p>

## 👥 Contribution
### o2
- [songkg/o2#410](https://github.com/songkg7/o2/pull/410) 🚀
- [songkg/o2#417](https://github.com/songkg7/o2/pull/417) 🚀

"""

# View count placeholder
view_count = """
<!-- View count placeholder -->
<p align="right">
<a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fpedrobiqua&count_bg=%23673DC8&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=hits&edge_flat=false"/></a>
</p>
"""

# Combinar todos os textos
readme_text = f"{markdown_text}{latest_blog_post_list}{view_count}"

# Exibir o texto completo do README
print(readme_text)

# Opcional: Escrever o conteúdo no arquivo README.md
with open("README.md", 'w') as f:
    f.write(readme_text)
