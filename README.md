# Python学习程序测试管理工具

这是一个便于python学习者管理及运行学习过程中产生的.py脚本程序的小工具，可以自动生成执行时间、执行耗时、作者等信息，同时生成包含这些信息以及输入的数据和程序执行结果的图片，然后将这个图片复制到剪贴板。本工具还支持自动对程序输入参数（向你的.py脚本中的input()函数输入），以便更好地测试程序执行耗时。

（当然，这个工具主要服务于西南科技大学python选修课实验）

## 内容列表

- [使用说明](#使用说明)
- [下载](#下载)
- [如何贡献](#如何贡献)
- [维护者](#维护者)
- [使用许可](#使用许可)

## 使用说明

*已知问题：生成图片时不能正确处理 \t 这个符号 *

你可以选择将我的整个项目结构全部复制下来，也可以根据我的结构自行修改，总之，你需要在 TestAdminTool.py 同级文件夹下创建一个名为 config 的配置文件，里面填入以下内容
```
name=
path=.\\test
package=com.shirakawatyu.test
args=null
```
等于号后填写自己相应的信息，

name对应你的名字，

path对应你学习过程中编写的文件的文件夹（这个由包决定），

package对应软件包，

如果你不知道如何path和package这两个参数请直接复制上述，并保持你的项目结构与我的完全一致（包括名字），当然，test文件夹中的东西你都可以删掉，那些是我写的实验的作业（

args对应自动输入的参数，如果你用不到请保持 null

## 下载

请直接clone，然后使用下面的指令安装pygame,pillow,pywin32
```
pip install pygame
pip install pillow
pip install pywin32
```

## 维护者

[@flben233](https://github.com/flben233)。

## 如何贡献

非常欢迎你的加入！[提一个 Issue](https://github.com/flben233/pythonExperiment/issues/new) 或者提交一个 Pull Request。

## 使用许可

[MIT](LICENSE) © flben233
