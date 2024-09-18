import pandas as pd

info_df = pd.read_excel('information_list.xlsx')
output_df = pd.read_excel('output_list.xlsx')

for index, output_row in output_df.iterrows():
    description = output_row['Description']
    
    for _, info_row in info_df.iterrows():
        full_name = f"{info_row['First Name']} {info_row['Surname']}"
        
        if full_name in description:
            output_df.at[index, 'First Name And Surname'] = full_name
            output_df.at[index, 'Personal ID'] = info_row['Personal ID']
            output_df.at[index, 'Company'] = info_row['Company']

output_df.to_excel('updated_output_list.xlsx', index=False)
