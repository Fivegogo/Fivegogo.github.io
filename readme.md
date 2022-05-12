## 添加相册
1. 将图片添加到`static/img/photos`下(例如`WechatIMG241.jpeg`)  
2. 在`content/gallery/_index.md`中添加一个`[[item]]`, 格式如下:
```
[[item]]
    title = "图片的标题, 如果留空, 那么将不显示标题"
    content = "一句话简介图片, 如果留空, 那么将不显示内容"
    align = "center"  # 标题和内容的对齐方式, 可用选项: ["center", "left", "right"].
    overlay_color = "#555"  # 图片不可用时, 会显示该颜色
    overlay_img = "photos/bWechatIMG241.jpeg"  # 图片的url(如果按照1去配置的话, 这里必须添加photos/的前缀, 如果放在了static/img/dir下的话, 可以添加dir/的前缀), "photos/WechatIMG241.jpeg"
    overlay_filter = 0.5  # rgba的alpha通道, 取值范围为[0, 1], 0表示不模糊, 1表示完全模糊(即全黑)
```

