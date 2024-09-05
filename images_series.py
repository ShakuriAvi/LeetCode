from typing import Dict, Tuple
import uuid

series_by_slice = dict()


def insert_new_img(img_obj: Dict[str, str]) -> Dict[str, str]:
    key = img_obj["series_id"]
    val = img_obj["slice"]
    if key not in series_by_slice:
        series_by_slice[key] = set()
    series_by_slice[key].add(val)
    items = get_longest_items(series_by_slice[key])
    return {"series_id": key, "start": items[0], "end": items[1]}


def get_longest_items(items: set) -> Tuple[int, int]:
    start, end = items, 0
    count = 0

    idx_by_counter = dict()
    for i in items:
        if count == 0:
            start = i
            end = i

        if i + 1 in items:
            end = i + 1
            count += 1
        else:
            idx_by_counter[count] = (start, end)
            count = 0

    return idx_by_counter[max(idx_by_counter.keys())]

if __name__ == '__main__':
    series_id_1 = uuid.uuid1()
    series_id_2 = uuid.uuid1()
    series_id_3 = uuid.uuid1()
    img1 = {"series_id": series_id_1, "slice": 4}
    img2 = {"series_id": series_id_1, "slice": 2}

    img3 = {"series_id": series_id_1, "slice": 1}
    img4 = {"series_id": series_id_2, "slice": 5}
    img5 = {"series_id": series_id_3, "slice": 2}
    img6 = {"series_id": series_id_2, "slice": 3}
    img7 = {"series_id": series_id_1, "slice": 3}
    print(insert_new_img(img1))
    print(insert_new_img(img2))
    print(insert_new_img(img3))
    print(insert_new_img(img4))
    print(insert_new_img(img5))
    print(insert_new_img(img6))
    print(insert_new_img(img7))



