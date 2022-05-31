'''
Francisco Figueroa
Section Leader: Elias Anastopoulos
11/22/2021
ISTA 131
cont_comp_vbar.py
Creates a vertical bar graph representing the performace of national teams for a 
relevant international competition.
'''
import numpy as np, pandas as pd, matplotlib.pyplot as plt


'''
Paramaters: fname, a file name String
to_frame() takes in its string parameter and reads the csv file associated with it 
'''
def to_frame(fname):
    header = 1 if fname.find('10') == -1 else 0
    df = pd.read_csv(fname, index_col=0, header=[header])
    df.index.name = None
    return df


'''
Parameter: frame, a Pandas dataframe
make_vert() takes in a dataframe object and allows for the visualisation of the wins a national team
had during the specific competition. Once the graph data is plotted, gradient() is called on the data
visualization. 
'''
def make_vert(frame):
    fig = plt.figure(figsize=(17,9)); ax = fig.subplots()
    fig.suptitle('Matches won at the EURO 2020 Continental Competition', fontsize=20)
    plt.ylabel('Teams', fontsize=17)
    plt.xlabel('Fixtures Won Across Competition', fontsize=16)
    y_pos = np.arange(10); 
    ax.set_yticks(y_pos); ax.set_xticks(np.arange(7)); ax.set_yticklabels(frame.index.array)
    bars = ax.barh(y_pos, frame['W'], align='center')
    gradient(bars)


'''
Parameters: bars, a matplotlib bar graph
Using linspace() and atleast_2d() from numpy, to create a gradient, each bar is filled in with an
added colorful filling
'''
def gradient(bars):
    grad = np.atleast_2d(np.linspace(0,1,100))
    ax = bars[0].axes
    lim = ax.get_xlim()+ax.get_ylim()
    for bar in bars:
        bar.set_zorder(1)
        bar.set_facecolor("none")
        x,y = bar.get_xy()
        width, height = bar.get_width(), bar.get_height()
        ax.imshow(grad, extent=[x, x + width, y, y + height], aspect="auto", zorder=0)
    ax.axis(lim)


'''
main() takes in nothing, calls all functions.
'''
def main():
    euro2020frame = to_frame('top10national.csv')
    make_vert(euro2020frame)
    plt.show()

main()