Система управления роботом-манипулятором

[Презентация](https://docs.google.com/presentation/d/15_yC8rDs_KMLsT8r7TEIxtrsaSBIVCJt/edit?usp=sharing&ouid=100188907486347298259&rtpof=true&sd=true)

## Демонстрация на выставке «Территория NDT»
![](https://github.com/CepbluKot/roboticArm/blob/main/video.gif)

## Диплом с конференции «ННТК»
![](https://github.com/CepbluKot/roboticArm/blob/main/%D0%94%D0%B8%D0%BF%D0%BB%D0%BE%D0%BC%20%D0%9D%D0%9D%D0%A2%D0%9A_page-0001.jpg)

## Диплом с выставки «Территория NDT»
![](https://github.com/CepbluKot/roboticArm/blob/main/diploma_NDT.jpg)

## Конструкция
![](https://github.com/CepbluKot/roboticArm/blob/main/photo1687856753.jpeg)

## Пример работы в ROS
![](https://github.com/CepbluKot/roboticArm/blob/main/ROS-demo.gif)


## Графический интерфейс

Вкладка управления <br />
![](https://github.com/CepbluKot/roboticArm/blob/main/interface1.jpeg)

Вкладки с информацией о электродвигателях <br />
![](https://github.com/CepbluKot/roboticArm/blob/main/interface2.jpeg)
![](https://github.com/CepbluKot/roboticArm/blob/main/interface3.jpeg)
![](https://github.com/CepbluKot/roboticArm/blob/main/interface4.jpeg)
![](https://github.com/CepbluKot/roboticArm/blob/main/interface5.jpeg)
![](https://github.com/CepbluKot/roboticArm/blob/main/interface6.jpeg)

Вкладка программы последовательности движений <br />
![](https://github.com/CepbluKot/roboticArm/blob/main/interface7.jpeg)

Вкладка настроек электродвигателей <br />
![](https://github.com/CepbluKot/roboticArm/blob/main/interface8.jpeg)


## Демонстрация обмена данными 

![](https://github.com/CepbluKot/roboticArm/blob/main/data_example.png) </br>

## UML диаграмма классов 

![](https://github.com/CepbluKot/roboticArm/blob/main/class_diagram.png) </br>

## UML диаграмма прецедентов

![](https://github.com/CepbluKot/roboticArm/blob/main/precedent_diagram.png) </br>


## Описание архитектуры

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

Для корректной работы требуется подключение к сревомотороам через адаптер usb-can <br />

Для доступа к can-шине через usb используется такое устройство: https://aliexpress.ru/item/4000472388410.html?sku_id=10000001901640368 <br />
![](https://ae04.alicdn.com/kf/H6d02e323135b46718cabcc51bcb68b0fr.jpg)



## Команда
[Игорь Малыш - разработка ПО](http://t.me/igmalysh) </br>
[Виталий Минасян - разработка конструкции](http://t.me/schwarzeseite) </br>


## Дополнительные материалы

[Документация к электромоторам](https://github.com/CepbluKot/roboticArm/blob/main/electrical_motor_documentation.pdf)
