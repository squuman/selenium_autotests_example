# Usbc Autotesting

При первой установке должны быть установлены:
1. python3.8
2. jdk
3. pip
4. pyvenv

При первом запуске:
./init.sh

Обязательно скачать драйвера браузера в папку drivers.

Для запуска тестов (при необходимости в файлах можно поправить адреса и порты):
1. ./server/run_hub.sh
2. ./server/run_*_node.sh
3. ./runs/run_*_tests.sh

Для визуализации отчета:
./runs/serve_allure.sh