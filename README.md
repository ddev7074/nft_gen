# NFT generator

## Начало работы

Переименовать файл `.env.example` в `.env`, указать `<TOKEN>` из Pinata
## Конфигурация
отредактировать файл conf в формате json

"PROCESSES":4 - количество процессов

"SRC_PATH":"./layers" - источник картинок

"TOTAL_IMAGES":5 - количество картинок

"IMAGES_BASE_URL":"ipfs://<TOKEN>/"

"SIZE_W":1140 - размер картинок

"SIZE_H":1140 - размер картинок
```
pip install poetry
make install
```
## Источник для генерации картинок
./layers
## Сгененрировать картинки

```
make images
```

## Перегенерировать метаданные

```
make metadata
```
