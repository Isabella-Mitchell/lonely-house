def dates_string_to_list(str):
    selected_dates_list = str.split(',')
    # remove check out date from list so not included in price
    del selected_dates_list[-1]
    return selected_dates_list
