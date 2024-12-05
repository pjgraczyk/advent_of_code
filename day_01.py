import pandas as pd

def extract():
    data = pd.read_csv('data.csv', sep='\s\s\s', names=['left', 'right'])
    data.reset_index(inplace=True, drop=True)
    return data

def diff_score(data):
    transformed_data = data.copy()
    transformed_data = pd.DataFrame(
        {"left" : sorted(transformed_data['left']),
         "right" : sorted(transformed_data['right'])
        })
    transformed_data['diff'] = abs(transformed_data['left'] - transformed_data['right'])
    return transformed_data["diff"].sum()

def similarity_score(data):
    transformed_data = data.copy()
    transformed_data['similarity'] = (transformed_data['left']
                        .apply(lambda x: x * transformed_data['right']
                               .value_counts().get(x, 0)))
    return transformed_data['similarity'].sum()

if __name__ == '__main__':
    data = extract()
    diff_score = diff_score(data)
    similarity_score = similarity_score(data)
    print(diff_score, similarity_score)
    