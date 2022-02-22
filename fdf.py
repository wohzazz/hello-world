def fdf(data, def_float_format = '{:,.3f}', formats_dict = {}, percentage_list = None, string_list = None):
    """Format and style DataFrame for Jupyter Notebook display 
    Last updated 23.02.2022
    
    What it does:
    
    By default, there will be an attempt to change all object/string columns to 'float'. 
    'int' and 'object' format will remain as is. DataFrame will then be styled and displayed with heatmap 'Blues'
    formatting on integer or float format columns

    parameters:
    
    (required)
    
        data: DataFrame of data
    

        
        
    (with defaults)
    
        formats_dict: dictionary of formats 
        string_list: list of columns to be formatted as string. Defaults to None
        percentage_list: list of columns identified as percentage columns. Defaults to None
        def_float_format: set default format for 'float'. default to '{:,.3f}' (3 decimal places)    
        
        
    """
    import copy
    df = copy.deepcopy(data)
    #
    if percentage_list == None:
        percentage_list = []
    if string_list == None:
        string_list = []
    for col in percentage_list:
        df[col] = df[col]*100
    
    # process df before displaying
    col_list = list(df.select_dtypes(['object']).columns)
#     print(col_list)
    for col in string_list:
        try:
            col_list.remove(col)
        except:
            pass
#     print(col_list)
    for col in col_list:
        
        try:
            df[col] = df[col].astype('float')
        except:
            pass
#     df.info()

#     # style and display df##################################################
    # initialise format dictionary
    format_string = {}      
    # format object type as 'float' unless in string list
    for col in df.select_dtypes('float').columns:
            format_string[col] = def_float_format
#     print(format_string) # before
    format_string.update(formats_dict) # merge with custom defined formats
#     print(format_string)
    return df.style.background_gradient(cmap = 'Blues').format(format_string).format(formats_dict)


##############sample data for illustration################################################################################################################

import pandas as pd

df = pd.DataFrame([['A', 'Z1', '23', 1, 1.21, 0.66]
                   , ['B', 'Z2', '24', 2, 1.32, 0.58]
    
], columns = ['CAT1', 'CAT2', 'CAT3', 'INT1', 'FLOAT1', 'PERC1'])
df.info()
df
##########################################################################################################################################################

# help(fdf)
# fdf(df)
fdf(df, string_list = ['CAT3'], formats_dict = {'PERC1': '{:,.1f}%'})
fdf(df, string_list = ['CAT3'], formats_dict = {'PERC1': '{:,.1f}%'}, percentage_list=['PERC1'])

##########################################################################################################################################################