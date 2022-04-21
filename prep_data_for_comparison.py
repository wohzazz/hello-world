
# Last updated: Thursday 21st April 2022

# NOTE the read_data function is an example only. Replace with the data read function for the specific task at hand
def read_data(Category):
    import pandas as pd
    url = 'https://github.com/wohzazz/Datasets/blob/main/Orders_Trended.csv?raw=true' # link need to be 'raw'. Refer to https://stackoverflow.com/questions/55240330/how-to-read-csv-file-from-github-using-pandas for more info
    df = pd.read_csv(url, parse_dates = ['Date', 'LY_Date', 'LW_Date'], dayfirst=True)    
    df = df[df['Category'] == Category]
    
    return df

# df = read_data(Category = 'Phones')
# df


# parameters
# data = read_data(Category = 'Phones')
# metric = 'NbrOrders'
# period = 'Date'
# comparison = 'LY'
# frequency = 'Daily'

def prep_data_for_comparison(data, metric, period, comparison, frequency=None, metric_type = None):
    """
    Prepare data for period on period 
    
    Inputs:
    data: DataFrame with required data
    metric: metric being analysed
    period: date column in df
    comparison: specify the comparison period. should correspond with the column name in df
    frequency: e.g. Daily. this will be hardcoded into the final table. Defaults to None
    metric_type: e.g. percentage, integer, dollar. This will help with building scalable visuals


    ################################################################################################################################################
    An example of the required data format:

            def read_data(Category):
                import pandas as pd
                url = 'https://github.com/wohzazz/Datasets/blob/main/Orders_Trended.csv?raw=true' # link need to be 'raw'. Refer to https://stackoverflow.com/questions/55240330/how-to-read-csv-file-from-github-using-pandas for more info
                df = pd.read_csv(url, parse_dates = ['Date', 'LY_Date', 'LW_Date'], dayfirst=True)    
                df = df[df['Category'] == Category]
                
                return df
                
            df = read_data(Category = 'Phones')
            # df

            df = prep_data(
            data = read_data(Category = 'Computers')
            ,metric = 'NbrOrders'
            ,period = 'Date'
            ,comparison = 'LY'
            #     ,frequency = 'Daily'
            )
            df.loc[:, 'Category'] = 'Computers'
            display(df)

    ################################################################################################################################################
    """
    # libraries 
    import pandas as pd
    # calculated variables based on input parameters
    agg_dict = {metric: 'sum'}
    left_on = [comparison+'_'+period]
    right_on = [period]
    dims = right_on+left_on
    # 1. read in data
    df = data
    
    # 2. aggregate to required level
    df = df.groupby(dims).agg(agg_dict).reset_index()
#     df
    
    # 3. add period comparisons 
    df = df.merge(df[[period,metric]],how = 'left', left_on = left_on, right_on = right_on, suffixes = ['', '_'+comparison]).drop([period+'_'+comparison], axis=1)
    df.loc[:, 'Variance'] = df[metric] - df[metric+'_'+comparison]
    df.loc[:, '% Variance'] = (df[metric] - df[metric+'_'+comparison])/df[metric+'_'+comparison]
    
    # 4. Add 'legend' for plotting purposes
    df1 = df
    df1.loc[:, 'Legend'] = metric
#     print(df1)
    
    df2 = df[[period, comparison+'_'+period, metric+'_'+comparison]].rename({metric+'_'+comparison: metric}, axis=1)
    df2.loc[:, 'Legend'] = metric+' '+comparison
#     print(df2)
    df = pd.concat([df1, df2])
   
    # 4. final renames for scalability
    df = df.rename({period: 'Period', comparison+'_'+period: 'Comp Period', metric: 'Metric Value', metric+'_'+comparison: 'Metric Value Comp Period'}, axis=1)
    df.loc[:, 'Frequency'] = frequency
    df.loc[:, 'Metric'] = metric
    df.loc[:, 'Metric Type'] = metric_type
     
    return df

df = prep_data_for_comparison(
    data = read_data(Category = 'Phones')
    ,metric = 'NbrOrders'
    ,period = 'Date'
    ,comparison = 'LY'
    ,frequency = 'Daily'
)
df.loc[:, 'Category'] = 'Phones'
display(df)

df = prep_data(
    data = read_data(Category = 'Computers')
    ,metric = 'NbrOrders'
    ,period = 'Date'
    ,comparison = 'LY'
#     ,frequency = 'Daily'
)
df.loc[:, 'Category'] = 'Computers'
display(df)
