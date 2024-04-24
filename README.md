# PhoneBookApp
Клиентская часть
Клиентская часть предоставляет следующие возможности:
- добавление в телефонную книгу новой записи. Запись может содержать: имя, фамилию, отчество, номер телефона,
текстовую заметку
- удаление существующей записи
- поиск по любому полю, кроме заметки. Возможность поиска по содержимому заметки будет плюсом
- просмотр записи

Серверная часть
Серверная часть предоставляет следующие возможности:
- Сервер принимает запросы, выполнять их обработку и возвращать ответы клиенту.
- Сервер хранит состояние между перезапусками.
- Сервер может одновременно работать с несколькими клиентами.
- В процессе обработки запроса сервер не блокируется и принимает в обработку другие запросы.

При запуске клиента необходимо в качестве параметров передать IP-адресс и номер порта сервера.

Список команд:
- "-post <"имя фамилия отчество">, <"номер телефона">, <"записка">" : добавление записи в телефонную книгу;
- "-get_by_name <"имя фамилия отчество">" : получение записи по ФИО;
- "-get_by_phonenumber <"номер телефона">" : получение записи по номеру телефона;
- "-delete <"имя фамилия отчество">" : удаление записи с соответсвующим ФИО;
