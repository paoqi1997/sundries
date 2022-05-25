# The manual of Mermaid

面向 [Mermaid](https://mermaid-js.github.io/mermaid/#/) 的基本教程。

## 说明

GitHub 现已支持在 Markdown 文件中渲染 Mermaid 内容，详情请参考[该文](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/)。

如果要在 vscode 下工作，请安装该 [Mermaid](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) 扩展。

## 练习

下面是一个非常简单的流程图。

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```
