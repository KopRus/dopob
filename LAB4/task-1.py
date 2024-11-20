# TODO решите задачу
import json

def task(file_path: str) -> float:
    with open(file_path, 'r') as file:
        data = json.load(file)
        result = sum(item['score'] * item['weight'] for item in data)
        return round(result, 3)

print(task('input.json'))
