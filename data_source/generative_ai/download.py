import os
import wget
import re

# Đường dẫn thư mục đích
download_dir = os.path.join(os.path.dirname(__file__))

file_links = [
    {
        "title": "Attention Is All You Need",
        "url": "https://arxiv.org/pdf/1706.03762"
    },
    {
        "title": "BERT - Pre-training of Deep Bidirectional Transformers for Language Understanding",
        "url": "https://arxiv.org/pdf/1810.04805"
    },
    {
        "title": "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models",
        "url": "https://arxiv.org/pdf/2201.11903"
    },
    {
        "title": "Denoising Diffusion Probabilistic Models",
        "url": "https://arxiv.org/pdf/2006.11239"
    },
    {
        "title": "Instruction Tuning for Large Language Models - A Survey",
        "url": "https://arxiv.org/pdf/2308.10792"
    },
    {
        "title": "Llama 2 - Open Foundation and Fine-Tuned Chat Models",
        "url": "https://arxiv.org/pdf/2307.09288"
    }
]

# Làm sạch tên file nếu cần
def clean_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

def is_exist(file_link):
    filename = clean_filename(f"{file_link['title']}.pdf")
    return os.path.exists(os.path.join(download_dir, filename))

for file_link in file_links:
    filename = clean_filename(f"{file_link['title']}.pdf")
    out_path = os.path.join(download_dir, filename)
    if not os.path.exists(out_path):
        print(f"Downloading: {file_link['title']}")
        wget.download(file_link["url"], out=out_path)
