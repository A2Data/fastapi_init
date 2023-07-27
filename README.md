# fastapi_init
NewFastApi 初始化，SQLite 数据库 CRUD + logger 标准化输出

## 安装
```bash
pip install cookiecutter
```


## 使用

Github
```angular2html
cookiecutter https://github.com/A2Data/fastapi_init.git


```

Gitee:
```angular2html
cookiecutter https://gitee.com/DataITems_admin/fastapi_init.git
```

## 结构


```
./
├── README.md  项目说明文件
├── alembic  数据库迁移配置目录 
├── apps     项目的存放目录 
│  ├── Application.py  主要应用程序
│  ├── __init__.py
│  ├── api    主项目配置目录，也存放了主路由文件
│  │  ├── ApiRouter.py  路由文件
│  │  ├── controller    视图文件入口
│  │  ├── models        模型文件
│  │  ├── schemas       schema文件
│  │  └── service       CRUD 服务
│  ├── core    核心文件目录
│  │  ├── base        核心配置例如 setting
│  │  ├── config      配置文件目录
│  │  ├── db          ORM模型基类目录
│  │  └── middleware  中间件配置目录
│  ├── resource     资源文件目录
│  │  ├── data     数据存放
│  │  ├── static   静态资源存放目录
│  │  └── temp     临时文件目录
│  ├── tests        测试接口文件目录
│  │  ├── __init__.py 
│  └── utils        封装的一些工具类目录  
│      ├── http_status.py  常用 http 响应类
│      ├── logger.py  日志处理核心配置
│      └── response.py  响应处理文件
├── logs   日志目录 
│  └── log_20230722_18.log
├── main.py      主程序入口文件  
├── pyproject.toml   pdm 版本依赖文件
└── scripts      脚本文件目录
    └── __init__.py
```
## 启动

![image.png](https://cdn.jsdelivr.net/gh/itdocs-icu/img/img/20230726181604.png)



## API 接口文档

![image.png](https://cdn.jsdelivr.net/gh/itdocs-icu/img/img/20230726182007.png)



## Tests
![image.png](https://cdn.jsdelivr.net/gh/itdocs-icu/img/img/20230727122139.png)