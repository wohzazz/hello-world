#refer to: https://webflow.com/blog/best-color-combinations
import seaborn as sns
import matplotlib as mpl
colour_comb_dict = {}
colour_comb_dict['Royal blue/Peach'] = ['#00539CFF', '#EEA47FFF']
colour_comb_dict['Blue/Pink'] = ['#2F3C7E', '#FBEAEB']
colour_comb_dict['Charcoal/Yellow'] = ['#101820FF', '#FEE715FF']
colour_comb_dict['Red/Classic'] = ['#F96167', '#FCE77D']
colour_comb_dict['Lime green/Electric blue'] = ['#CCF381', '#4831D4']
colour_comb_dict['Lavender/Teal'] = ['#E2D1F9', '#317773']
colour_comb_dict['Cherry red/off-white'] = ['#990011FF', '#FCF6F5FF']
colour_comb_dict['Baby blue/White'] = ['#8AAAE5', '#FFFFFF']

colour_comb_dict['Hot pink/Cyan'] = ['#FF69B4', '#00FFFF']
colour_comb_dict['Peach/Burnt orange'] = ['#FCEDDA', '#EE4E34']
colour_comb_dict['Light blue/Dark blue'] = ['#ADD8E6', '#00008b']
colour_comb_dict['Sky blue/Bubblegum pink'] = ['#89ABE3FF', '#EA738DFF']
colour_comb_dict['Mustard/Sage/Forest green'] = ['#E3B448', '#CBD18F', '#3A6B35']

colour_comb_dict['Fuchsia/Neon green'] = ['#EC449B', '#99F443']
colour_comb_dict['Pastel orange/Peach/Custard'] = ['#FFA351FF', '#FFBE7BFF', '#EED971FF']
colour_comb_dict['Raspberry/Shades of blue'] = ['#8A307F', '#79A7D3', '#6883BC']
colour_comb_dict['Cherry red/Bubblegum pink'] = ['#CC313D', '#F7C5CC']
colour_comb_dict['Coral/Spiced apple & peach'] = ['#FC766AFF', '#783937FF', '#F1AC88FF']

colour_comb_dict['Light purple/Mint/Butter'] = ['#AA96DA', '#C5FAD5', '#FFFFD2']
colour_comb_dict['Forest green/Moss green'] = ['#2C5F2D', '#97BC62FF']
colour_comb_dict['Island green/white'] = ['#2BAE66FF', '#FCF6F5FF']
colour_comb_dict['Yellow/Verdant Green'] = ['#FFE77AFF', '#2C5F2DFF']
colour_comb_dict['Biege/Black-brown/Tan'] = ['#DDC3A5', '#201E20', '#E0A96D']

colour_comb_dict['Royal blue/Pale yellow'] = ['#234E70', '#FBF8BE']
colour_comb_dict['Blue/Maroon/Indigo'] = ['#408EC6', '#7A2048', '#1E2761']
colour_comb_dict['Scarlet/Light Olive/Light Teal'] = ['#B85042', '#E7E8D1', '#A7BEAE']
# colour_comb_dict   


def set_colour_palette(matplotlib_color_cycle=colour_comb_dict['Royal blue/Peach']
                           +colour_comb_dict['Red/Classic']
                           +colour_comb_dict['Lavender/Teal']
                          +colour_comb_dict['Scarlet/Light Olive/Light Teal']
                          +colour_comb_dict['Cherry red/Bubblegum pink']
                          +colour_comb_dict['Raspberry/Shades of blue']
                       ,show_colour_palette = False
                          ):
    """Set default color palette to use with matplotlib
    matplotlib_color_cycle = assign color palette (list form, hex codes). a default has been assigned
    show_colour_palette: if True, then show stored color palette colour_comb_dict. defaults to False
    """
    ######################################################################################################
    if show_colour_palette ==True:
        for i, key in enumerate(colour_comb_dict.keys()):
            print(i+1, key)
        for val in colour_comb_dict.values():
            _ = sns.palplot(sns.color_palette(val))        
    ######################################################################################################
    # Set the default color cycle
    mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=matplotlib_color_cycle) 
    sns.palplot(sns.color_palette(matplotlib_color_cycle))
    ######################################################################################################

set_colour_palette()    
    