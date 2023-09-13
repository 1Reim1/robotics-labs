alphabet = "АаБбВвГгҐґДдЕеЄєЖжЗзИиІіЇїЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщьЮюЯя"


def encode(text, key):
    result = ""
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            result += char
            continue
        new_index = index + key
        if new_index > len(alphabet) - 1:
            new_index -= len(alphabet)
        result += alphabet[new_index]
    return result


def decode(text, key):
    result = ""
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            result += char
            continue
        new_index = index - key
        if new_index < 0:
            new_index = len(alphabet) - abs(new_index)
        result += alphabet[new_index]
    return result


if __name__ == "__main__":
    text_to_encode = 'Привіт. Сьогодні чудовий день для нападу на галлів'
    key = 8
    encoded_text = encode(text=text_to_encode, key=key)
    decoded_text = decode(text=encoded_text, key=key)
    assert text_to_encode == decoded_text, "Oooops! Something go wrong"
