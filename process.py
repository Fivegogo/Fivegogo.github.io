import os
import shutil
import json
from bs4 import BeautifulSoup

publication_types = ["Uncategorized", "Conference Paper", "Journal Paper", "Preprint", "Report", "Book", "Book section", "Thesis", "Patent", "Workshop Paper"]

bs = BeautifulSoup(open("Publications.html", "r"), features="html.parser")
layout_content = bs.find(id="layout-content")

contents = {}
contents_meta = {}

cur_type = None

for sub in layout_content.children:
    if sub == "\n": continue
    if hasattr(sub,"attrs") and "id" in sub.attrs and (sub.attrs["id"] == "toptitle" or sub.attrs["id"] == "footer"): continue
    if sub.name == "h2":
        if sub.text not in contents.keys(): contents[sub.text] = []
        cur_type = sub.text
    else:
        contents[cur_type].append(sub)

for key in contents.keys():
    contents_meta[key] = []
    for sub in contents[key]:
        metadata = {
            "img": None,
            "pdf": None,
            "demo": None,
            "video": None,
            "code": None,
            "dataset": None,
            "title": None,
            "conf": "",
            "author": ""
        }

        # 获取img_url
        img = sub.find_all("img")
        if img is not None:
            metadata["img"] = img[0].attrs["src"]

        # 填充其他的信息
        p = sub.find_all("p")[0]
        if p is not None:
            for link in p.contents:
                print(link)
                meta = input(f"type(pass, {', '.join(list(metadata.keys()))})>")
                if meta == "" or meta == "pass": continue
                if meta == "conf":
                    if link.name == "b": metadata[meta] += f"<b>{link.text}</b>"
                    else: metadata[meta] += link.text

                if meta == "author":
                    if link.name == "b": metadata[meta] += f"<b>{link.text}</b>"
                    else: metadata[meta] += link.text
                else:
                    metadata[meta] = link.attrs["href"]
                    if meta == "pdf":
                        metadata["title"] = link.text
        contents_meta[key].append(metadata)
        
        pub_types = publication_types.index(key)
        for meta in contents_meta[key]:
            content  = "---" + "  \n"
            content += f"title: " + meta["title"] + "  \n"
            content += f"authors:  [\"" + "\", \"".join(meta["author"].split(", ")) + "\"]  \n"
            content += f"publication_types: [\"" + str(pub_types) + "\"]" + "  \n"
            if meta["pdf"] is not None:
                content += "url_pdf: " + meta["pdf"] + "  \n"
            if meta["demo"] is not None:
                content += "url_demo: " + meta["demo"] + "  \n"
            if meta["video"] is not None:
                content += "url_video: " + meta["video"] + "  \n"
            if meta["code"] is not None:
                content += "url_code: " + meta["code"] + "  \n"
            if meta["dataset"] is not None:
                content += "url_dataset: " + meta["dataset"] + "  \n"
            content  += "---" + "  \n"
        os.makedirs(f"content/publication/{meta['title']}", exist_ok=True)
        
        if meta['img'].endswith("png") or meta["img"].endswith("PNG"): posifix = "png"
        elif meta["img"].endswith("jpg") or meta["img"].endswith("jpeg") or meta["img"].endswith("JPG"): posifix = "jpg"
        shutil.copy(meta['img'], f"content/publication/{meta['title']}/feature.{posifix}")
        with open(f"content/publication/{meta['title']}/index.md", "w") as fo: fo.writelines(content)
        
        print("")
        print("")
        print("current paper results: ")
        print(json.dumps(metadata, indent=4))
        print("")
        print("")


# for key in contents_meta.keys():
#     pub_types = publication_types.index(key)
#     for meta in contents_meta[key]:
#         content  = "---" + "  \n"
#         content += f"title: " + meta["title"] + "  \n"
#         content += f"authors: " + meta["author"] + "  \n"
#         content += f"publication_types: [\"" + pub_types + "\"]" + "  \n"
#         if meta["url"] is not None:
#             content += "url_pdf: " + meta["url"] + "  \n"
#         if meta["demo"] is not None:
#             content += "url_demo: " + meta["demo"] + "  \n"
#         if meta["video"] is not None:
#             content += "url_video: " + meta["video"] + "  \n"
#         if meta["code"] is not None:
#             content += "url_code: " + meta["code"] + "  \n"
#         if meta["dataset"] is not None:
#             content += "url_dataset: " + meta["dataset"] + "  \n"
#         content  += "---" + "  \n"
#     os.makedirs(f"content/publication/{meta['title']}", exist_ok=True)
    
#     if meta['img'].endswith("png") or meta["img"].endswith("PNG"): posifix = "png"
#     elif meta["img"].endswith("jpg") or meta["img"].endswith("jpeg") or meta["img"].endswith("JPG"): posifix = "jpg"
#     os.system(f"copy {meta['img']} content/publication/{meta['title']}/feature.{posifix}")
#     with open(f"content/publication/{meta['title']}/index.md", "w") as fo: fo.writelines(content)
