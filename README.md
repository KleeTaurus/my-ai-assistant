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
$ python3 -m venv venv
$ source venv/bin/activate
```

安装 OpenAI 包

```
$ pip install openai
```

获取 Model 列表

```python
import os
import openai
openai.organization = "org-eXcqm3mDqaR6m7xWX4Z4I9gu"
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())
```

```shell
model, openai            , 2022-04-07 19:07:29, babbage
model, openai            , 2022-04-07 18:51:31, ada
model, openai            , 2022-04-07 19:31:14, davinci
model, openai-dev        , 2022-04-28 19:01:49, babbage-code-search-code
model, openai-dev        , 2022-04-28 19:01:45, text-similarity-babbage-001
model, openai            , 2022-04-07 20:40:42, text-davinci-001
model, openai            , 2022-04-07 20:40:42, curie-instruct-beta
model, openai-dev        , 2022-04-28 19:01:49, babbage-code-search-text
model, openai-dev        , 2022-04-28 19:01:45, babbage-similarity
model, openai-dev        , 2022-04-28 19:01:49, curie-search-query
model, openai-dev        , 2022-04-28 19:01:47, code-search-babbage-text-001
model, openai-internal   , 2022-11-28 01:40:35, text-davinci-003
model, openai            , 2022-06-24 14:43:57, code-cushman-001
model, openai-dev        , 2022-04-28 19:01:47, code-search-babbage-code-001
model, openai            , 2022-04-07 20:40:42, text-ada-001
model, openai-dev        , 2022-04-28 19:01:45, text-similarity-ada-001
model, openai            , 2022-04-13 20:08:04, text-davinci-insert-002
model, openai-dev        , 2022-04-28 19:01:45, ada-code-search-code
model, openai-dev        , 2022-04-28 19:01:47, ada-similarity
model, openai-dev        , 2022-04-28 19:01:47, code-search-ada-text-001
model, openai-dev        , 2022-04-28 19:01:45, text-search-ada-query-001
model, openai            , 2022-04-07 20:40:43, text-curie-001
model, openai            , 2022-04-13 00:19:39, text-davinci-edit-001
model, openai-dev        , 2022-04-28 19:01:49, davinci-search-document
model, openai            , 2022-04-13 20:08:04, text-davinci-002
model, openai-dev        , 2022-04-28 19:01:50, ada-code-search-text
model, openai-dev        , 2022-04-28 19:01:47, text-search-ada-doc-001
model, openai            , 2022-04-13 20:08:04, code-davinci-edit-001
model, openai            , 2022-04-07 20:40:42, davinci-instruct-beta
model, openai            , 2022-04-07 20:40:43, text-babbage-001
model, openai-dev        , 2022-04-28 19:01:47, text-similarity-curie-001
model, openai-dev        , 2022-04-28 19:01:47, code-search-ada-code-001
model, openai-dev        , 2022-04-28 19:01:45, ada-search-query
model, openai-dev        , 2022-04-28 19:01:45, text-search-davinci-query-001
model, openai            , 2022-04-13 20:08:05, code-davinci-002
model, openai-dev        , 2022-04-28 19:01:50, curie-similarity
model, openai-dev        , 2022-04-28 19:01:45, davinci-search-query
model, openai            , 2022-04-13 20:08:04, text-davinci-insert-001
model, openai-dev        , 2022-04-28 19:01:50, babbage-search-document
model, openai-dev        , 2022-04-28 19:01:47, ada-search-document
model, openai            , 2022-04-07 19:31:14, curie
model, openai-dev        , 2022-04-28 19:01:49, text-search-babbage-doc-001
model, openai-dev        , 2022-04-28 19:01:49, text-search-curie-doc-001
model, openai-dev        , 2022-04-28 19:01:49, text-search-curie-query-001
model, openai-dev        , 2022-04-28 19:01:49, babbage-search-query
model, openai-dev        , 2022-04-28 19:01:45, text-search-davinci-doc-001
model, openai-dev        , 2022-04-28 19:01:49, text-search-babbage-query-001
model, openai-dev        , 2022-04-28 19:01:48, curie-search-document
model, openai-dev        , 2022-04-28 19:01:45, text-similarity-davinci-001
model, openai            , 2022-06-28 20:17:29, audio-transcribe-001
model, openai-dev        , 2022-04-28 19:01:49, davinci-similarity
model, system            , 2020-05-28 00:18:30, cushman:2020-05-03
model, system            , 2020-12-10 20:20:25, ada:2020-05-03
model, system            , 2020-12-10 20:36:51, babbage:2020-05-03
model, system            , 2020-12-10 20:38:45, curie:2020-05-03
model, system            , 2020-12-10 22:42:43, davinci:2020-05-03
model, openai            , 2021-01-15 21:26:30, if-davinci-v2
model, openai            , 2021-01-15 21:26:08, if-curie-v2
model, openai            , 2021-08-20 00:52:35, if-davinci:3.0.0
model, openai            , 2021-08-20 22:21:10, davinci-if:3.0.0
model, openai            , 2021-08-20 23:25:14, davinci-instruct-beta:2.0.0
model, system            , 2022-01-12 01:06:48, text-ada:001
model, system            , 2022-01-11 23:32:46, text-davinci:001
model, system            , 2022-01-12 02:37:27, text-curie:001
model, openai            , 2022-01-12 20:12:50, text-babbage:001
```
