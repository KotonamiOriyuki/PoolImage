可以自动通过 osu! 导出bid所对应bg并生成难度名，谱面信息的工具，可用于大部分 osu! 比赛的 showcase 。

在开始前，请使用 PyCharm 编辑 main.py 中的 key 和 path 方可正常运作。\
Key - osu!API key，您可以通过 https://osu.ppy.sh/p/api 申请一个。\
其次，您需要下载 ImageMagick，安装时**请勾选 Install development headers and libraries for C and C++。**

如果程序缺少库，请依次检查下列库:
`requests
json
Wand`\
安装方法:\n
打开 Terminal (或cmd),定位到本文件夹,例:\
`cd C:\Users\Administrator\PoolImage`\
后，键入
`pip install 上方对应缺少库的名称`即可。


同时您需要编辑 list.txt 键入 bid 和 图池类型。格式：bid,type\
例子:\
2570910,NM\
1000684,TB\
不同的图用换行区分，如上。

您也可以通过更换 font.ttf 改变生成图片所用的字体。

生成的图片将会保存至 /image/

编译环境:Windows 10 , anaconda3 , PyCharm 社区版\
鸣谢:Zh_Jk 对本代码的部分援助。\
Last Update : 2021/6/13 16:11