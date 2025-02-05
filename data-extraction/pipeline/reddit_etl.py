from etls.reddit_etl import extract_data, load_data
def reddit_data_pipeline():
    data = extract_data()
    load_data(data)