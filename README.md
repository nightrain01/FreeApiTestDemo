# FreeApiTestDemo
## 项目说明
本项目使用 Pytest + Requests + Allure + YAML 实现了数据驱动的接口自动化测试

挑选了网上一些免费的接口以及Ruoyi-Vue演示版的部分接口进行测试

## 使用
### 依赖安装
由于Ruoyi的登录过程需要填写验证码，这里使用[CalculateCaptcha_Recognition](https://github.com/fupinglee/CalculateCaptcha_Recognition)项目对验证码进行识别，因此需要安装pytorch相关依赖  

python依赖安装：
```shell
pip install torch==1.10.1+cpu torchvision==0.11.2+cpu torchaudio==0.10.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install -r requirements.txt
```
allure安装：  
可以参考[官方文档](https://allurereport.org/docs/gettingstarted-installation/)进行安装  
也可以直接从[Releases](https://github.com/allure-framework/allure2/releases)下载，手动配置path

### 执行测试
使用`pytest`命令执行测试：
```shell
pytest
```

### 查看报告
`pytest`执行完毕后，会在项目根目录`./reports`路径下生成报告  
使用allure命令，生成并查看html报告:
```shell
allure serve ./reports
```
