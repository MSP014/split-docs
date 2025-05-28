#!/usr/bin/env python3
import os
import re
from datetime import datetime

# Будем брать рабочую директорию (где вы запускаете скрипт),
# а не __file__:
ADR_DIR = os.getcwd()  
OUT_FILE = os.path.join(ADR_DIR, "README.md")

lines = [
    "# Architectural Decision Records",
    "",    
    "This folder contains all key architectural decisions made in the SPLiT project.",
    "Each ADR file describes one specific decision and follows a consistent structure.",
    "",
    "---",
    "",
    "## 📄 ADR Index",
    "",
    "| Date       | Title |",
    "|------------|-------|",
]

for fname in sorted(os.listdir(ADR_DIR)):
    if re.match(r"^\d{8}-.*\.md$", fname):
        # Дата
        date = datetime.strptime(fname[:8], "%Y%m%d").strftime("%Y-%m-%d")
        # Заголовок из первой строки
        with open(os.path.join(ADR_DIR, fname), encoding="utf-8") as f:
            first = f.readline().strip()
        title = first.lstrip("# ").strip() or fname
        lines.append(f"| {date} | [{title}]({fname}) |")
        
# Пустая строка перед разделом Development
lines.append("")
# Раздел Development и More information
lines.extend([
    "---",
    "",
    "## Development",
    "",
    "To preview the knowledge base locally, run:",
    "",
    "```bash",
    "log4brains preview",
    "```",
    "",
    "To create a new ADR interactively, run:",
    "",
    "```bash",
    "log4brains adr new",
    "```",
    "",
    "## More information",
    "",
    "- [Log4brains documentation](https://github.com/thomvaill/log4brains/tree/develop#readme)",
    "- [What is an ADR and why should you use them](https://github.com/thomvaill/log4brains/tree/develop#-what-is-an-adr-and-why-should-you-use-them)",
    "- [ADR GitHub organization](https://adr.github.io/)",
    ""
])

# Записываем в README.md
with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"✅ Generated {OUT_FILE}")