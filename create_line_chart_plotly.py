def create_line_chart_plotly(data, x, y, title = 'Line chart',  label_renames = {}, text= None, symbol = None, color = None, markers=True 
                             , y_dashed = None, y_h = None, y_hb = None , x_v = None, x_vb = None, yaxfmt = None, output_file = None):
    """Plot line chart using plotly express
    
    prerequsites: DataFrame of all required data
    
    parameters:
    
    (required)
        data: DataFrame of data
        x: column of x values to plot
        y: column/s of y values to plot
    
    (with defaults)
        label_renames: dictionary of labels to rename. Defaults to {}
        title: specify title of chart. Defaults to 'Line chart'
        text: specify single column to use for annotations. Defaults to None
        color: single column to show colors by. Defaults to None
        symbol: specify field to use different symbols for markers default None
        markers: enable/disable markers, defaults to False
        y_dashed: specify list of values to update lines to 'dashed' style. These columns should be a subset of legend. Defaults to None
        y_h: specify a tuple of (value, text annoation) to be show on chart as a horizontal line. Defaults to None
        x_v: specify a tuple of (value, text annoation) to be show on chart as a vertical line. Defaults to None
        y_hb: specify a tuple of (tuple, value) to be shown on the chart as a horizontal bar. Defaults to None
        x_vb: specify a tuple of (tuple, value) to be shown on the chart as a vertical bar. Defaults to None
        yaxfmt: y axis format. Defaults to None (i.e. Plotly default is used). options include (non exhaustive):
            2 decimal places: .2f
            2 decimal places: .2%
            dollars to 2 decimal place: $.2f
            nearest dollar: $.0f
        output_file:
            1. 'png' static supposedly better quality
            2. 'jpeg' static
            3. 'html' interactive but large file size
            4. None. Default no output
            
    
    """
    import plotly.express as px
    # plotly line chart using plotly express
    fig = px.line(data_frame = data, x=x, y=y, color=color, markers=markers, symbol = symbol, text = text, title = title, labels = label_renames)

#     fig.update_traces(patch={"line": {"color": "black", "width": 4}})
#     fig.update_traces(patch={"line": {"color": "black", "width": 4, "dash": 'dot'}}, selector={"legendgroup": "Australia"}) 

    # specify is any lines should be dashed ####################################################################################################################################################################################################
    if y_dashed !=None:
        if type(y_dashed) == list:
            for val in y_dashed:
                fig.update_traces(patch={"line": {"dash": 'dot'}}, selector={"legendgroup": val}) # update linestyle to dashed
        else:
            print('y_dashed needs to be a list')
    # add horizontal line ################################################################################################################################################################################################################
    if y_h != None:
        if type(y_h) == tuple: # check if y_h is a tuple
            _ = fig.add_hline(y = y_h[0], annotation_text =y_h[1], line_dash = "dot", line_color = "grey", annotation_position = "bottom right", annotation_font_size = 10, annotation_font_color = "grey")
        else:
            print('y_h is specified but needs to be a tuple')
    # add vertical line ################################################################################################################################################################################################################
    if x_v != None:
        if type(x_v) == tuple: # check if x_h is a tuple
            _ = fig.add_vline(x = x_v[0], annotation_text =x_v[1], line_dash = "dot", line_color = "grey", annotation_position = "top right", annotation_font_size = 10, annotation_font_color = "grey")
        else:
            print('x_v is specified but needs to be a tuple')            
    # add vertical area#####################################################################################################################################################################################################################
    if x_vb != None:
        if type(x_vb) == tuple and type(x_vb[0]) == tuple: # check types of x_vb
            _ = fig.add_vrect (x0 = x_vb[0][0], x1 = x_vb[0][1], annotation_text = x_vb[1], annotation_position = "top left", annotation_font_size = 10, annotation_font_color = "grey"
#                                , annotation = dict(font_size = 9, font_family = 'Calibri')
                               , fillcolor = 'blue', opacity = 0.2, line_width =0)
        else:
            print('x_vb is specified but needs to be a tuple, first tuple value is also a tuple')
    # add horizontal area#####################################################################################################################################################################################################################
    if y_hb != None:
        if type(y_hb) == tuple and type(y_hb[0]) == tuple: # check types of y_hb
            _ = fig.add_hrect (y0 = y_hb[0][0], y1 = y_hb[0][1], annotation_text = y_hb[1], annotation_position = "top left", annotation_font_size = 10, annotation_font_color = "grey"
#                                , annotation = dict(font_size = 9, font_family = 'Calibri')
                               , fillcolor = 'blue', opacity = 0.2, line_width =0)
        else:
            print('y_hb is specified but needs to be a tuple, first tuple value is also a tuple')    

    # options on y axis format: https://www.tutorialspoint.com/plotly/plotly_format_axis_and_ticks.htm
    if yaxfmt != None:
        fig.update_yaxes(tickformat=yaxfmt)
    fig.show()
    
    
    #export images, refer to https://plotly.com/python/static-image-export/ for static image export options and https://plotly.com/python/interactive-html-export/ for interactive image export options
    import os
    if not os.path.exists("images"):
        os.mkdir("images")
    if output_file == 'png':
        fig.write_image("images/linechart_png.png")
    elif output_file == 'jpeg':
        fig.write_image("images/linechart_jpeg.jpeg")
    elif output_file == 'html':
        fig.write_html("images/linechart_html.html")
    ###################################################################################################################################################################################################################

# help(create_line_chart_plotly)
# load sample data for testing
data = px.data.gapminder().query("continent == 'Oceania'")
data.loc[data['year']> 1987, 'Pre/Post 1987'] = 'Post'
data.loc[data['year']<= 1987, 'Pre/Post 1987'] = 'Pre'
# data


# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp', color = 'country', markers = True, symbol = 'country', text = 'lifeExp', title = 'Line graph' )
# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp', color = 'country', symbol = 'country', text = 'lifeExp', title = 'Line graph' )    
# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp', symbol = 'country', text = 'lifeExp', title = 'Line graph' )    
# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp', text = 'lifeExp', title = 'Line graph' )   
# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp' )   
# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp', color = 'country' )   
# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp', color = 'country', y_dashed = ['Australia'] )  # make Australia dashed
# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp', color = 'country', y_dashed = ['Australia'], y_h = (75, 'Example benchmark') )  # add y horizontal line
# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp', color = 'country', y_dashed = ['Australia'], y_h = (75, 'Example benchmark'), x_hb = ((1990,2000), 'Example focus period') )  # add x bar 
# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp', color = 'country', y_dashed = ['Australia'], y_h = (75, 'Example benchmark'), x_vb = ((1990,2000), 'Example focus period'), symbol = 'country', text = 'lifeExp' )  # add symbol and text

# create_line_chart_plotly(data = data, x = 'year', y = 'lifeExp', color = 'country', y_dashed = ['Australia'], y_h = (75, 'Example y_h'), y_hb = ((70, 72), 'Low'), x_v = (1980, 'Example x_v')
#                          , x_vb = ((1990,2000), 'Example x_hb'), symbol = 'country', text = 'lifeExp', output_file= 'png')  # add symbol and text



#illustrating PCP view, 4 columns required
data = pd.DataFrame([[100, 'CY', '06. June', 'Australia'], [99, 'CY', '07. July', 'Australia'], [102, 'CY', '08. August', 'Australia']
                     , [105, 'LY', '06. June', 'Australia'], [103, 'LY', '07. July', 'Australia'], [95, 'LY', '08. August', 'Australia']
                    , [62, 'CY', '06. June', 'NZ'], [76, 'CY', '07. July', 'NZ'], [80, 'CY', '08. August', 'NZ']
                     , [52, 'LY', '06. June', 'NZ'], [66, 'LY', '07. July', 'NZ'], [72, 'LY', '08. August', 'NZ']
                    ], columns = ['Y', 'Symbol', 'X', 'Color'])
print(data)

# ideas for PCP view 
create_line_chart_plotly(data = data, x = 'X', y = 'Y', color = 'Color', y_dashed = ['Australia, LY', 'NZ, LY']
                         ,symbol = 'Symbol', text = 'Y', output_file= 'png')  # add symbol and text
