猜字游戏
==================================

**** 

## 项目介绍
       本项目为个人练习项目，近期学习python ,通过使用pygame、pyttsx3 实现了一个简单的猜字游戏，如有雷同纯属巧合。
       项目实现了简单的猜字游戏功能，点击play 按钮，进入猜字游戏界面，会有朗读声响起，提示当前需要猜的字的读音，如果为听清可以点击top按钮 进行听取读音，下方会给去四个选项按钮，点击正确的汉字，则有提示成功提示音，并继续下一关，点击错误按钮，有错误提示音，保持当前状态。
       项目有简单的倒计时功能（不是很完善），没关有10秒的倒计时，倒计时结束 ，提示 End
        、Reset 按钮， 点击 End 按钮，则结束游戏，点击 Reset 则游戏重新开始。项目有简单的计分功能，每答对一关，则计分。 

## 版本介绍
本版本介绍为开发环境使用版本，具体支持版本作者没有去考究，以下版本仅供参考

python ：3.10.11
pygame ：2.5.2
pyttsx3 :  2.90

## 目录结构

```
--根目录
    --resource 资源目录
        --font  字体资源
        --wav 音频目录（免费网站下载）
    --build 生成exe可执行文件时生成的目录
    --dist  生成exe可执行文件时生成的目录
    start.py 入口文件
    button.py 按钮类
    game_stats.py 统计类
    scoreboard.py 头部得分及涉及属性类
    setting.py 基础设置类

```

## 操作方法
1.点击运行 start.py 文件

2.点击运行 start.exe 文件

## 操作扩展
exe可执行文件生成 扩展
pyinstaller : 6.5.0

生成命令
```
pyinstaller --onefile --windowed --add-data="resource/;resource/" start.py
```
生成后，需要将dist目录中的start.exe copy到 根目录下

## 更新日志

### 1.0.0
    初版更新 

## 已知功能缺陷

1. 倒计时不是很准确
2. 四个选项 ，没有相应点击状态
3. 猜字朗读声音有点小，pyttsx3不支持音量设置
4. 没有实现窗口最大化效果，exe文件点击放大窗口会报错
5. 无任何UI界面
6. 倒计时结束时，无得分提示，不够友好
7. 没有添加等级提示，
8. 关卡难度没有变化，完全随机