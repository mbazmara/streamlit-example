def categorize(data):
    for f_type in data.columns:
        if isinstance(data[f_type][0], str):
            data[f_type] = data[f_type].astype('category')
            data[f_type] = data[f_type].cat.codes
        else:
            pass
    return data