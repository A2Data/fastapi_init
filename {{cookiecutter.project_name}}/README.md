# FastAPI-INIT

{{cookiecutter.project_name}}

## PDM
推荐使用 PDM 初始化

https://pdm.fming.dev/latest/

### Linux/Mac
```bash
curl -sSL https://pdm.fming.dev/dev/install-pdm.py | python3 -
```

### Windows

```angular2html
(Invoke-WebRequest -Uri https://pdm.fming.dev/dev/install-pdm.py -UseBasicParsing).Content | python -
```

也可以使用 pip 安装

```angular2html
pip install  --user pdm
```


### 初始化

```angular2html
pdm init
```

### 安装依赖项
运行以下命令来安装项目的依赖项。
```angular2html

pdm install

```

或者使用常规安装

```angular2html
pip install -r requirements.txt
```


### 运行

```angular2html
pdm run main.py

或者
python run main.py
```



![image.png](https://cdn.jsdelivr.net/gh/itdocs-icu/img/img/20230727121404.png)


### API接口
http://127.0.0.1:8000/docs





![image.png](https://cdn.jsdelivr.net/gh/itdocs-icu/img/img/20230727121501.png)



### Test


![image.png](https://cdn.jsdelivr.net/gh/itdocs-icu/img/img/20230727122139.png)
