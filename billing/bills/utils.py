""" Helper functions for plotting """
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import numpy as np

# Functions to get a plot in django
def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def mb_bar(x,y):
    ypos = np.arange(len(x))
    plt.switch_backend('AGG')
    plt.figure(figsize=(10, 5))
    plt.title('Monthly Breakdown')
    
    plt.bar(ypos, y, align='center')
    plt.xticks(ypos, x, rotation = 45)
    plt.xlabel('Month Paid')
    plt.ylabel('Paid Amount')
    plt.tight_layout()
    graph = get_graph()
    return graph