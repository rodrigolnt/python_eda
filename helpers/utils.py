
import plotly.express as px
import pandas as pd

color_palette = [
    "#f5e623",  
    "#f48d46",
    "#da596a",
    "#6001a4",  
    "#1609aa",  
]
              
            
tight_margin = {"r":70,
                "l":70,
                "t":100,
                "b":70}


def correlation_heatmap(dataframe, columns=None, y_axis=None, x_axis=None, title='Correlation Heatmap', figsize=(800, 400)):    
    """
    Creates a correlation heatmap using Plotly with customization options.

    Parameters:
    - dataframe (pd.DataFrame): DataFrame to compute the correlation matrix.
    - title (str): Title for the heatmap.
    - figsize (tuple): Width and height of the figure (in pixels).
    """
    # Validate input arguments
    if x_axis is not None:
        corr_matrix = dataframe[columns].corr().loc[y_axis, x_axis]
    else:
        corr_matrix = dataframe[columns].corr()

    # Create the heatmap using Plotly Express
    fig = px.imshow(
        corr_matrix, 
        text_auto='.2f',  # Display annotations with 2 decimal points
       # color_continuous_scale=['#ff4d4d','#4361ee','#80ffdb'],  # Diverging colormap similar to Seaborn
        #range_color=[-1, 1],  # Set range from -1 to 1
        aspect='auto'  # Adjust cell aspect ratio
    )

    fig.update_layout(
        title=dict(
            text=title, 
            font=dict(size=16), 
            x=0.5,  # Center the title
            pad=dict(t=10)  # Title padding
        ),
        width=figsize[0],  # Set figure width
        height=figsize[1],  # Set figure height
        margin=tight_margin  # Adjust margins
    )

    # Show the figure
    fig.show()