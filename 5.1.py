
def find_key(struct, key, max_depth=None, depth=1):
    result = None 

    if max_depth and max_depth < depth:
        return result

    if key in struct:
        return struct[key]

    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, max_depth,
depth=depth + 1)
            if result:
                break
    return result

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}
while True:
    key = input('Введите искомый ключ: ') 