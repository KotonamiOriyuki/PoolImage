# 使用拓展
import json
import os
import requests
from wand.drawing import Drawing
from wand.image import Image

# 参数部分
key = ''  # ppy的apikey,若没有请转到 https://osu.ppy.sh/p/api 申请一个。


# ppy request 部分。
def ppyrequest(apikey: str, beatmaps_id: str, pool: str, name: str):
    url = 'https://osu.ppy.sh/api/get_beatmaps?k=' + apikey + '&b=' + beatmaps_id
    r = requests.get(url)
    hjson = json.loads(r.text)
    title = hjson[0]['artist_unicode'] + ' - ' + hjson[0]['title_unicode']
    diffname = hjson[0]['version']
    beatmapset_id = hjson[0]['beatmapset_id']
    loadimage(beatmapset_id, title, diffname, pool, name)


# 从ppy api中下载封面图到本地。
def loadimage(beatmapset_id: str, title: str, diffname: str, pool: str, name: str):
    url = 'https://assets.ppy.sh/beatmaps/' + beatmapset_id + '/covers/cover.jpg'
    img = requests.get(url)
    ex = open('export.jpg', 'ab')
    ex.write(img.content)
    ex.close()
    imageprocess(title, diffname, pool, name)


# magick裁剪图片。
def imageprocess(title: str, diffname: str, pool: str, name: str):
    with Image(filename='export.jpg')as img:
        img.crop(0, 0, 514, 74)
        img.save(filename='export.png')
        os.remove('export.jpg')
        imagecomposite(title, diffname, pool, name)


# magick处理图片内容。
def imagecomposite(title: str, diffname: str, pool: str, name: str):
    out = Image(width=550, height=110)
    bg = Image(filename='export.png')
    r = Image(filename='frame.png')
    icon = Image(filename='image/' + pool + '.png')
    with Drawing() as draw:
        draw.composite(operator='undefined', left=18, top=18, width=bg.width, height=bg.height, image=bg)
        draw.composite(operator='darken', left=0, top=0, width=r.width, height=r.height, image=r)
        draw.font = 'font.ttf'
        draw.font_size = 24
        draw.fill_color = 'white'
        draw.text(34, 52, title)
        draw.font_size = 20
        draw.fill_color = 'white'
        draw.text(34, 76, diffname)
        draw.composite(operator='atop', left=436, top=59, width=92, height=28, image=icon)
        draw(out)
        out.save(filename='export/' + name + '.png')
        os.remove('export.png')


# 文本读入。
def contenttolist():
    f = open('list.txt')
    g = f.read()
    check = g.split('\n')
    for i in range(0, len(check), 1):
        content = check[i]
        sep = content.split(',')
        bid = sep[0]
        pool = sep[1]
        ppyrequest(key, bid, pool, name=str(i))


# 从此处开始执行，顺序由上往下。
contenttolist()
