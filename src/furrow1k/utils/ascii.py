from utils.filesystem import load_text_lines


def concat_art(fname_1: str, fname_2: str, buffer: str = None) -> str:
    if buffer is None:
        buffer = "top"

    buffer_options = ["top", "bottom"]
    if buffer not in buffer_options:
        raise ValueError(f"Buffer must be one of {buffer_options=}")
    art_1 = load_text_lines(fname_1)
    art_2 = load_text_lines(fname_2)

    n_chars_1 = len(max(art_1, key=len))
    height_diff = len(art_1) - len(art_2)
    # art_1 has more rows
    padding = [" " * n_chars_1]
    # print(repr(padding))
    row_padding = abs(height_diff) - 1
    if height_diff < 0:
        if buffer == "top":
            art_1 = row_padding * padding + art_1
        else:
            art_1 += row_padding * padding
    elif height_diff > 0:
        if buffer == "top":
            art_2 = row_padding * padding + art_2
        else:
            art_2 += row_padding * padding

    result = ""
    for left, right in zip(art_1, art_2):
        result += left.strip("\n") + right.strip("\n") + "\n"

    return result




    print(art_1)