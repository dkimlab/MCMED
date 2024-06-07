import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import wfdb
import numpy as np
import os

def visualize_numerics(df_numerics, target_csn):
    # Get all unique measures
    measures = df_numerics['Measure'].unique()
    rows = df_numerics[df_numerics['CSN'] == target_csn]

    fig = make_subplots(rows=len(measures), cols=1, shared_xaxes=True, vertical_spacing=0.01)

    # Loop through all measures
    for i, measure in enumerate(measures):
        # Filter rows with Measure == measure
        measure_rows = rows[rows['Measure'] == measure][['Time', 'Value']]

        # Create scatter plot for measure
        fig_measure = px.scatter(measure_rows, x='Time', y='Value')

        # Add measure scatter plot to the i-th row of the subplots
        fig.add_trace(fig_measure.data[0], row=i+1, col=1)

        fig.update_traces(marker=dict(size=6, color='MediumPurple', line=dict(width=1, color='white')))

        # label the y-axis with the measure
        fig.update_yaxes(title_text=measure, row=i+1, col=1)

    # Update layout
    fig.update_xaxes(tickfont_size=14)

    fig.update_layout(
        height=200*len(measures),
        width=800,
        title_text="Numerics",
        font=dict(size=14),
        font_family="Arial",
    )

    # Show the figure
    fig.show()

    return fig

def visualize_lab_rad_order(df_labs, df_rad, df_orders, target_csn):
    # Helper function to truncate text and add ellipsis
    def truncate_text(text):
        max_char = 70
        if len(text) > max_char:
            return text[:max_char] + '...'
        else:
            return text
    
    rows_labs = df_labs[df_labs['CSN'] == target_csn].fillna('', inplace=False)
    rows_rad = df_rad[df_rad['CSN'] == target_csn].fillna('', inplace=False)
    rows_orders = df_orders[df_orders['CSN'] == target_csn].fillna('', inplace=False)

    # Create a trace for orders
    trace_orders = go.Scatter(
        x=rows_orders['Order_time'],
        y=['Order' for _ in range(len(rows_orders))],  # Set y-axis as 'Order' for orders
        mode='markers',
        marker=dict(symbol='square', size=10, line=dict(color='white', width=1)),  
        hovertemplate='Order Time: %{x}<br>First Admin Time: %{customdata[0]}<br>Result Time: %{customdata[1]}<br>Procedure Name: %{text}',
        text=rows_orders['Procedure_name'],
        customdata=list(zip(rows_orders['First_admin_time'], rows_orders['Result_time'])),
        name='Orders'
    )

    # Create a trace for radiology
    trace_rad = go.Scatter(
        x=rows_rad['Order_time'],
        y=['Radiology Report' for _ in range(len(rows_rad))],  # Set y-axis as 'Radiology Report' for radiology
        mode='markers',
        marker=dict(symbol='diamond', size=10, line=dict(color='white', width=1)),  
        hovertemplate='Order Time: %{x}<br>Result Time: %{customdata[0]}<br>Study: %{text}<br>Impression: %{customdata[1]}',
        text=rows_rad['Study'],
        customdata=list(zip(rows_rad['Result_time'], rows_rad['Impression'].apply(truncate_text))),
        name='Radiology'
    )

    # Create a trace for labs
    trace_labs = go.Scatter(
        x=rows_labs['Order_time'],
        y=['Lab' for _ in range(len(rows_labs))],  
        mode='markers',
        marker=dict(symbol='triangle-up', size=10, line=dict(color='white', width=1)),  
        hovertemplate='Order Time: %{x}<br>Result Time: %{customdata[0]}<br>Display Name: %{text}<br>Abnormal: %{customdata[1]}',
        text=rows_labs['Display_name'],
        customdata=list(zip(rows_labs['Result_time'], rows_labs['Abnormal'])),
        name='Labs'
    )

    # Create the layout
    layout = go.Layout(
        title='Orders, Radiology Report and Labs',
        xaxis=dict(title='Order Time'),
        hovermode='closest'
    )

    # Create the figure
    fig = go.Figure(data=[trace_orders, trace_rad, trace_labs], layout=layout)

    # Adjust the spacing between lab, radiology and med data points
    fig.update_layout(
    height=300,
        width=800,
        yaxis=dict(
            tickmode='array',
            tickvals=[0, 1, 2],
            ticktext=['Order', 'Radiology Report', 'Lab'],
            tickfont=dict(size=14),
            ticklen=20
        )
    )
    fig.update_xaxes(tickfont_size=14)
    # Show the updated figure
    fig.show()

    return fig
    

def visualize_waveform(record_name, name=None):

    # Helper function to get the waveform start time, which is the datetime 
    # at the beginning of the first segment (i.e., xxx_1.dat)
    def get_waveform_starttime(record_name):
        base_record = '_'.join(record_name.split('_')[:-1]+['1'])
        base_record_obj = wfdb.rdrecord(base_record)
        return base_record_obj.base_datetime

    # Load the record. E.g. if the data file is 'x/y.dat' then record_name is 'x/y'
    record = wfdb.rdrecord(record_name)
    wf_starttime = get_waveform_starttime(record_name)

    # p_signal: Physical signal values after calibration, representing the actual physical measurements.  
    # d_signal: Digital signal values before calibration, representing the raw, unprocessed data.
    # We are plotting the physical signal here
    signal = record.p_signal.reshape(-1)

    # Get the unit of the signal
    waveform_unit = record.units[0]

    # Create a time vector
    fs = record.fs  # sampling frequency
    num_samples = len(signal)
    duration = num_samples / fs
    time = np.linspace(0, duration, num_samples)

    basetime = record.base_datetime
    time = time + (basetime - wf_starttime).total_seconds()

    # Create a Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=time, y=signal, mode='lines'))

    fig.update_layout(
        xaxis_title='Time (s) from Waveform Start',
        yaxis_title=name if name is not None else f'Value ({waveform_unit})',
        title=f'Waveform for {os.path.basename(record_name)} at the frequency of {fs} Hz',
    )

    fig.show()
