## Get Start

```sh
pip install -r requirement.txt

```

## Other

在Pycharm中Matplotlib Backend绘图会存在问题，解决方案为使用`TkAgg`后端进行绘图。

安装tk依赖：

```shell
brew install python-tk
```

python代码

```python
import matplotlib
matplotlib.use('TkAgg')
```

全局设置对虚拟环境Pycharm不生效，但还是告诉大家如何全局设置：在`~/.matplotlib/matplotlibrc`文件新增一行`backend: TkAgg`。

同时配置运行选项（或运行模版配置），将Run with Python Console取消勾选。