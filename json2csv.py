import pandas as pd
import json

# Читаем JSON lines файл
data = []
with open(r'Data\collection_events-000000000000.json', 'r') as f:
    for line in f:
        line = line.strip()
        if line:
            data.append(json.loads(line))

# Создаем DataFrame
df = pd.DataFrame(data)

# Заполняем NaN пустыми строками (опционально)
df = df.fillna('')

# Сохраняем в CSV
df.to_csv(r'Data\Dataset.csv', index=False, encoding='utf-8')

print(f"Сохранено {len(df)} записей")
print(f"Колонки: {list(df.columns)}")