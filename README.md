# RussianFIO2AD

Программа для генерации логинов и паролей из списка фамилий, имен и отчеств (ФИО) сотрудников.

![main](https://user-images.githubusercontent.com/132103/84661717-6adff600-af23-11ea-89b4-050b92f032ad.png)

Демонстрация работы: [youtube](https://www.youtube.com/watch?v=qBOdzqp3qxk).


Поддерживает вставку ФИО, скопированных из таблиц или текстового файла.

Логины и пароли генерируются на основании заданных шаблонов (шаблоны автоматически сохраняются в настройках). Возможно указание префикса для логина. Логин автоматически усекается до 20 символов (ограничение AD).

Поддерживает создание учетных записей в текущем домене Active Directory (требуется запуск на компьютере-члене домена под учетной записью, имеющей соответствующие права)

Возможно указание общих аттрибутов Active Directory, таких как описание, компания, департамент. Список общих атрибутов может быть дополнен вручную через файл конфигурации "data\settings.ini", список атрибутов можно найти здесь: [kouti.com](http://www.kouti.com/tables/userattributes.htm) ([копия](https://web.archive.org/web/20190412095601/http://www.kouti.com/tables/userattributes.htm))

Поддерживается добавление учетных записей в группы Active Directory (имеются ограничения, связанные с использованием экранируемых символов в именах групп).

Программа написана на Python 3 с использованием Qt5.

**[СКАЧАТЬ](https://github.com/qiwichupa/RussianFIO2AD/releases)**