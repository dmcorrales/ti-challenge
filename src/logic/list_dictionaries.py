def get_element_by_condition(expected_value=5):
    dict_elements = [
        {"x":1},
        {"x": 2},
        {"x": 5},
        {"x": 6}
    ]
    return next((item for item in dict_elements if item["x"] == expected_value), {})


if __name__ == '__main__':
    print(get_element_by_condition(5))