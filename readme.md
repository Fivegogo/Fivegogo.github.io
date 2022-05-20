## 添加相册
1. 将图片添加到`static/img/photos`下(例如`WechatIMG241.jpeg`)  
2. 在`content/gallery/_index.md`中添加一个`[[item]]`, 格式如下:
```
[[item]]
    title = "图片的标题, 如果留空, 那么将不显示标题"
    content = "一句话简介图片, 如果留空, 那么将不显示内容"
    font_color = "#f8f8f2"  title和content的字体颜色
    align = "center"  # 标题和内容的对齐方式, 可用选项: ["center", "left", "right"].
    overlay_color = "#555"  # 图片不可用时, 会显示该颜色
    overlay_img = "photos/bWechatIMG241.jpeg"  # 图片的url(如果按照1去配置的话, 这里必须添加photos/的前缀, 如果放在了static/img/dir下的话, 可以添加dir/的前缀), "photos/WechatIMG241.jpeg"
    overlay_filter = 0.5  # rgba的alpha通道, 取值范围为[0, 1], 0表示不模糊, 1表示完全模糊(即全黑)
```

## 添加News
1. 在`content/home/news.md`中添加一个`[[item]]`, 格式如下:
```
[[item]]
    title = "新闻的主标题(例如: 发表论文: xxx同学论文被xxx会议录用)"
    subtitle = "新闻的副标题(例如: 论文题目)"
    subtitle_color = "#808080"  # 副标题的颜色(如果没用特殊需求, 不需要该这个)
    link = "http://aibox.ruc.edu.cn/paper.html"  # 主标题的链接
```

## 添加图标到主页:
1. 在`content/home/hero.md`中添加一个`[[cta]]`, 格式如下:
```
[[cta]]
  url = "http://www.baidu.com"  # 链接
  icon_pack = "fab"  # 图标库
  icon = "zhihu"  # 图标名称
```
这里的icon_pack和icon的使用方法详见`https://wowchemy.com/docs/getting-started/page-builder/` 中的icons一节, 下面是从中摘抄出来的一部分
> Icon pack “fab” includes the following brand icons:
> - twitter, weixin, weibo, linkedin, github, facebook, pinterest, twitch, youtube, instagram, soundcloud
> - [See all icons](https://fontawesome.com/icons?d=gallery&s=brands)  
> 
> Icon packs “fas” and “far” include the following general icons:
> - fax, envelope (for email), comments (for discussion forum)
> - [See all icons](https://fontawesome.com/icons?d=gallery&s=regular,solid)  
>   
> Icon pack “ai” includes the following academic icons:
> - cv, google-scholar, arxiv, orcid, researchgate, mendeley
> - [See all icons](https://jpswalsh.github.io/academicons/)
> - To enable the academic icon pack in v5+, set `ai = true` under `[icon.pack]` in `params.yaml`  
> 
> Icon pack “emoji” gives you the ability to use emojis as icons  
> - [See all icons](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md)  
> - Enter the emoji shortcode, such as `:heart:`, in Wowchemy’s `icon` field
> - Wowchemy v4.9+ is required to utilise the emoji icon pack and can currently only be used in the Featurette (skills) widget.
>  
> Icon pack “custom” gives you the ability to use custom SVG icons
> - Create an SVG icon in your favorite image editor or download one from a site such as [Flat Icon](https://www.flaticon.com/)
> - Place the custom SVG icon in `assets/media/icons/`, creating the folders if necessary
> - Reference the SVG icon name (without `.svg` extension) in the `icon` field
> - Wowchemy v4.9+ is required to utilise the custom icon pack and can currently only be used in the Featurette (skills) widget.