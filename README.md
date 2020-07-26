## 环境配置

本程序需要在 Python3 环境下运行
安装插件:

```shell
pip3 install tushare -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip3 install flask -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip3 install flask-restful

# 假如提示缺少 bs4, 需要手动安装
pip3 install bs4

```

## 使用方式

* 启动

```shell
python3 serverjsonp.py

```

``` shell
GET 127.0.0.1:5000/max?s=002396&d=2019-03-02

RESPONSE
{
    "stock": "002396",
    "price": "25.100",
    "name": "星网锐捷",
    "time": "15:00:03",
    "hight": 26.13
}

```

``` javascript
        function getCurrentStock(code, date, op, id) {
            console.log('------get stock------')
            console.log(code)
            console.log(date)
            console.log(id)
            console.log(op)

            $.ajax({
                url: "http://xxx.xxx.xx.xxx:5000/max?s=" + code + "&d=" + date,
                dataType: "jsonp",
                jsonp: "callback",
                success: function (data) {
                    console.log(data);
                    $('#' + id + "cur").html(data.price)
                    $('#' + id + "gain").html(Percentage(data.hight - op, op))
                }
            })

        }

        function Percentage(num, total) {
            return (Math.round(num / total * 10000) / 100.00 + "%");
        }

```

## 服务

建议通过 gunicorn 来启动服务
``` shell

pip install gunicorn

gunicorn -w 4 serverjsonp:app

```
