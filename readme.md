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