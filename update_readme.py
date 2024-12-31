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
<h3>みなさん、こんにちは。私のgithubへようこそ</h3>

- 🧑‍💻 I'm currently work with this languages C++, Python, PHP, C# and JAVA
- 👯 I’m looking to collaborate . . . (Open to oportunities)
- 📫 How to reach me: pedrobiqua@outlook.com
- 👨‍💻 My blog:  <a href="https://pedrobiqua.github.io/pedrobiqua.dev/" target="_blank">Coding with Pedro</a>
- 🧑‍🏫 Languages: Portuguese 🇧🇷, English 🇺🇸, Japanese 🇯🇵

<div style="display: flex; justify-content: space-between;">
  <img src="https://github-readme-stats.vercel.app/api?username=pedrobiqua&theme=default&show_icons=true&hide_border=false&count_private=false" alt="pedrobiqua's Stats" width="49%" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=pedrobiqua&theme=default&show_icons=true&hide_border=false&layout=compact&hide=html,css,javascript,jupyter%20notebook,java,hack,processing,hack,scss" alt="pedrobiqua's Top Languages" width="37%" />
</div>

<br>

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## Contribution
### o2
- [songkg/o2#410](https://github.com/songkg7/o2/pull/410) 🚀

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
