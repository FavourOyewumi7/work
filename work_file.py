

# import http.client
import requests as re


def get_conn_and_docs(id):
    base_url = "https://api.bitbucket.org"
    headers = { 'Authorization': 'input here'}
    response = re.get(base_url+'/2.0/repositories/enersoftinc/geoaiprocessing/pullrequests/'+id, headers=headers)
    return response.json()

data = get_conn_and_docs('715')


def seperate_data(data_sample):
    final_data = {}
    actual_data = data_sample['description']
    seperated_lines = actual_data.strip('\n').split('##')
    seperated_lines = seperated_lines[1:]
    #getting the Overview
    overview_line = seperated_lines[0]
    sep_overview_line = overview_line.split('\n>')
    cleaned_sep_line = []
    for line in sep_overview_line:
        line = line.strip(' \n![]()')
        cleaned_sep_line.append(line)
    final_data['1.1 Overview'] = []
    for line in cleaned_sep_line[1:]:
        if len(line) > 0:
            final_data['1.1 Overview'].append(line)

    #affected scripts and arguments
    affected_line = seperated_lines[1]
    sep_affected_line = affected_line.split('\n>')
    cleaned_aff_line = []
    for line in sep_affected_line:
        line = line.strip(' \n ')
        cleaned_aff_line.append(line)
    print(cleaned_aff_line)
    final_data['2.2 Affected Scripts and Arguments'] = {}
    count = 1
    current_line = None
    for line in cleaned_aff_line[1:]:
        if len(line) > 0:
            if line.startswith(f'{str(count)}. **'):
                keep = line.split(' ')
                current_line = f'2.2.{count} {keep[1]}'
                final_data['2.2 Affected Scripts and Arguments'][current_line]= []
                count += 1
            elif line.startswith(f'{str(count)}.') and current_line == None:
                keep = line.split('.')
                current_line =  f'2.2.{count} {keep[1]}'
                final_data['2.2 Affected Scripts and Arguments'][current_line]= []
                count += 1
            elif current_line:
                final_data['2.2 Affected Scripts and Arguments'][current_line].append(line)


    print(final_data)


seperate_data(data)





