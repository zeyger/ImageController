# Refer to: https://github.com/zeyger/NeuralArt

NeuralArt + ImageController есть реализация паттерна Master/Worker (в какой-то степени), где NeuralArt - мастер, Worker - слейв 

Задача этого кода: взятие задание из хранилища в виде JSON, десериализация, запуск заранее спижженого скрипта из https://github.com/jcjohnson/neural-style, соответственно сериализация и запись обратно в хранилище (Redis)

