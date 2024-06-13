Система управления манипулятором

[Презентация](https://drive.google.com/file/d/1cKRX976KBxD_HUd96p9TGSsha-fylCqs/view?usp=sharing)

## Демонстрация на выставке «Территория NDT»
![](https://github.com/CepbluKot/roboticArm/blob/main/video.gif)

## Диплом с выставки «Территория NDT»
![](https://github.com/CepbluKot/roboticArm/blob/main/diploma_NDT.jpg)

## Конструкция
![](https://github.com/CepbluKot/roboticArm/blob/main/photo1687856753.jpeg)

## Пример работы в ROS
![](https://github.com/CepbluKot/roboticArm/blob/main/ROS-demo.gif)

Робот-манипулятор состоит из нескольких сервомоторов, управляемых через usb-can преобразователь, данные передаются по CAN-шине, применяется протокол CanOpen301

Сервомоторы могут принимать команды и отсылать на них ответы, по которым можно понять дошла ли команда до сервомотора, какие параметры на нем выставлены, его текущее состояние (нарпяжение, температура, коды ошибок и тп)

Как это работает:


1) Уровень железа - есть объект девайса, который напрямую отдает команды в CAN-шину, он умеет отправлять команды, принимать ответы, а так же (!) в него встроен буффер отправляемых команд. В случае, если будет получен ответ, подтверждающий прием команды двигателем, соответсвующая команда будет удалена из буффера, иначе: произойдет повторная отправка, если ответ на команду не приходит после n попыток отправки, она удаляется из буффера. На вход объект железа принимает коллбек для отдачи принятых данных в объект протокола;
2) Уровень протокола - объект, в котором описаны команды протокола и обработчики вхоядщих команд. Он принимает объект уровня железа и через него отсылает команды протокола. В объекте протокола описана коллбек-функция для объекта железа для получения полученных ответов и описаны обработчики самих ответов;
3) Абстракция - уровень робота - объект, в котором описаны базовые команды управления роботом, общается с уровнем протокола. На вход принимает объект уровня протокола. Через него можно выставлять и получать данные робота. Применяется для управления роботом через данный класс другими сущностями, описывающими сложные алгоритмы управения (например, баллистический вычислитель);


Также реализован простой GUI, демонстрирующий возможности интерфейса управления

Для работы с usb-can преобразователем необхоимо получить права на взаимодействие с ним:

```
lsusb
# ищем преобразователь в списке девайсов
sudo chown <ИМЯ ПОЛЬЗОВАТЕЛЯ> /deb/bus/usb/<Номер usb порта, к которому подключен преобразователь usb-can>/<id девайса>
```

Подробнее: https://linuxhint.com/list-usb-devices-linux/


Запуск:
```
pip3 install -r requirements.txt
python3 main.py
```

Для доступа к can-шине через usb используется такое устройство: https://aliexpress.ru/item/4000472388410.html?sku_id=10000001901640368 <br />
![](https://ae04.alicdn.com/kf/H6d02e323135b46718cabcc51bcb68b0fr.jpg)



## Команда
[Игорь Малыш - разработка ПО](http://t.me/igmalysh) </br>
[Виталий Минасян - разработка конструкции](http://t.me/schwarzeseite) </br>


