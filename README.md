使用方式

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
                url: "http://47.95.197.116:5000/max?s=" + code + "&d=" + date,
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
