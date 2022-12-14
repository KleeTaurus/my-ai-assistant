# My-AI-Assistant

## 介绍

[官网文档](beta.openai.com)

OpenAI 的使用场景：

* 内容生成
* 归纳总结
* 分类、归类和情感分析
* 数据提取
* 翻译

[API 列表](https://beta.openai.com/docs/api-reference/introduction)

[官方及三方开发库](https://beta.openai.com/docs/libraries)

## Python 示例

### Python 环境搭建

[Python Env](https://docs.python.org/3/library/venv.html)

创建 virtualenv 环境

```shell
$ python3 -m venv .env
$ source .env/bin/activate
```

安装 OpenAI 包

```
pip install openai
```

获取 Model 列表

```python
import os
import openai
openai.organization = "org-eXcqm3mDqaR6m7xWX4Z4I9gu"
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())
```
