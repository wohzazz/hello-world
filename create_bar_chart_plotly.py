
def create_bar_chart_plotly(data, x, y, color
                            , pattern_shape= None
                            , text=None 
                            , showlegend = True, showxaxis= True, showyaxis = True
                            , output_file = None
                           ):
    """Bar chart using plotly
    
    last updated: 14th Feb 2022
    
    prerequisites: DataFrame of all required data
    
    parameters 
    (required)
    data: DataFrame of data
    x: column of x values to plot
    y: column/s of y values to plot
    color: column to vary colours in bar chart
    
    (with defaults)  
    pattern_shape: column to vary patterns in bar chart by
    text: columns of annotations to show on bar chart
    showlegend: specify whether the have the legend visible or not
    showxaxis: specify whether the have the x axis visible or not
    showyaxis: specify whether the have the y axis visible or not
    
    output_file:
        1. 'png' static supposedly better quality
        2. 'jpeg' static
        3. 'html' interactive but large file size
        4. None. Default no output

    """
    import plotly.express as px


    fig = px.bar(df, x=x, y=y, color=color
                 ,pattern_shape=pattern_shape
#                  , pattern_shape_sequence=[".", "x", "+"]
                ,text = text
    #              ,text = 'Fruit'
                )


    # turn of axis (x, y, legend)##################
    #legend
    fig.update_layout(showlegend=showlegend)
    #x axis
    fig.update_xaxes(visible=showxaxis)
    #y axis    
    fig.update_yaxes(visible=showyaxis)
    ##################################################

    fig.show()  

    #export images, refer to https://plotly.com/python/static-image-export/ for static image export options and https://plotly.com/python/interactive-html-export/ for interactive image export options
    import os
    if not os.path.exists("images"):
        os.mkdir("images")
    if output_file == 'png':
        fig.write_image("images/barchart_png.png")
    elif output_file == 'jpeg':
        fig.write_image("images/barchart_jpeg.jpeg")
    elif output_file == 'html':
        fig.write_html("images/barchart_html.html")
    ###################################################################################################################################################################################################################


    
    
    
# # #plot 1 not using symbol#########################################################################

# df = pd.DataFrame(
#     [ ['a', 'Rain', 0.1, '10%', 'Above 25'],
#         ['b',	'Rain',	0.05,	'0.05',	'Above 25'],
#         ['c',	'Rain',	0.3,	'0.3',	'Above 25'],
#         ['a',	'Sunny',	0.5,	'0.5',	'Above 25'],
#         ['b',	'Sunny',	0.6,	'0.6',	'Above 25'],
#         ['c',	'Sunny',	0.05,	'0.05',	'Above 25']
#     ]
#     ,columns = ['X',	'Color',	'Y',	'Y_Label',	'Pattern']
# )
# df


# create_bar_chart_plotly(data =df, x = 'X', y = 'Y', color = 'Color' #
#                         ,text = 'Y_Label'
#                        ,)

# # #plot 2 using patterns#########################################################################

# df = pd.DataFrame(
#     [['a',	'Rain',	0.2,	'10%',	'Above 25'],
#         ['b',	'Rain',	0.05,	'0.05',	'Above 25'],
#         ['c',	'Rain',	0.3,	'0.3',	'Above 25'],
#         ['a',	'Sunny',	0.5,	'0.5',	'Above 25'],
#         ['b',	'Sunny',	0.6,	'0.6',	'Above 25'],
#         ['c',	'Sunny',	0.05,	'0.05',	'Above 25'],
#         ['a',	'Rain',	0.1,	'0.1',	'Below 25'],
#         ['b',	'Rain',	0.05,	'0.05',	'Below 25'],
#         ['c',	'Rain',	0.3,	'0.3',	'Below 25'],
#         ['a',	'Sunny',	0.3,	'30%',	'Below 25'],
#         ['b',	'Sunny',	0.3,	'0.3',	'Below 25'],
#         ['c',	'Sunny',	0.35,	'0.35',	'Below 25']
#     ]
#     ,columns = ['X',	'Color',	'Y',	'Y_Label',	'Pattern']
# )
# print(df)

# create_bar_chart_plotly(data =df, x = 'X', y = 'Y', color = 'Color' #
#                         ,pattern_shape = 'Pattern' #
#                         ,text = 'Y_Label'
#                        ,)