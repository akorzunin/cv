## Мои пэт проекты

## [duckdns-ui](https://github.com/akorzunin/duckdns-ui)

Self-hosted веб приложение для обновления динамических ip адресов в сервисе duckdns.org. Бэкенд разработан на Go, фронтенд на React. Поддерживает просмотр логов и ошибок, автоматическую перезагрузку и автоматическое обновление ip адресов.

Стек проекта:

- Backend: {{< icon "go.svg" >}} Go, BoltDB,  gocron
- Frontend: {{< icon "typescript.svg" >}} TypeScript {{< icon "react.svg" >}}React {{< icon "tailwind.svg" >}} Tailwind, Shadcn-ui


## [SuperIcosahedron](https://github.com/akorzunin/SuperIcosahedron)

Аркадня игра написанная на движке Godot. Пока находится в стадии разработки. Тестовые сборки для Windows, Linux(x11), Android и веб версия доступны по адресу [supericosahedron.akorz.duckdns.org](https://supericosahedron.akorz.duckdns.org)

Стек проекта:

- Лендинг: Astro, {{< icon "react.svg" >}}React {{< icon "tailwind.svg" >}} Tailwind
- Приложение: Godot


## [id3v2-tui](https://github.com/akorzunin/id3v2-tui)

Терминальный пользовательский интерфейс для редактирования метаданных ID3v2 в MP3-файлах. Поддерживает редактирование тегов в том числе изменение картинок обложек.

Стек проекта:

- {{< icon "go.svg" >}}Go, tview


## [DWMan](https://github.com/akorzunin/dwman)

Web приложение для автоматического сохранения плейлистов через АПИ Spotify. Поддерживает OAuth 2.0 авторизацию, периодические задачи для уведомлений и интерфейс для сборки плейлистов из плейбека.

Стек проекта:

- Backend: {{< icon "python.svg" >}} Python {{< icon "fastapi.svg" >}} Fastapi TinyDB
- Frontend: {{< icon "typescript.svg" >}} TypeScript {{< icon "react.svg" >}}React {{< icon "tailwind.svg" >}} Tailwind
- Тесты: pytest vitest playwright
