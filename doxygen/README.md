# The manual of Doxygen

面向Doxygen的基本教程。

## 配置

如果是C/C++工程，你需要在默认生成的 Doxyfile 的基础上添加以下配置：

```
# 工程名称
PROJECT_NAME           = "PQLIB"

# 版本号
PROJECT_NUMBER         = "0.1.0"

# 文档输出目录
OUTPUT_DIRECTORY       = .

# 文档语言环境
OUTPUT_LANGUAGE        = Chinese

# 提取所有文档信息，类的私有成员及文件的静态成员除外
EXTRACT_ALL            = YES

# 提取类的私有成员的信息
EXTRACT_PRIVATE        = YES

# 提取文件的静态成员的信息
EXTRACT_STATIC         = YES

# 文档输入目录
INPUT                  = .

# 添加树形结构的侧边栏
GENERATE_TREEVIEW      = YES

# 不生成latex格式的文档
GENERATE_LATEX         = NO
```

## 生成文档

相关命令如下所示：

```
$ doxygen Doxyfile
```
