'''
Francisco Figueroa
Section Leader: Elias Anastopoulos
11/22/2021
ISTA 131
final_project.py
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
Parameters: fFrame, a Pandas dataframe of French league values
            dFrame, a Pandas dataframe of German league values
            iFrame, a Pandas dataframe of Italian league values
            enFrame, a Pandas dataframe of English leauge values
            espFrame, a Pandas dataframe of Spanish league values
Sets the aesthetics, plots each data frame along with a regression line of all datasets to 
create a scattergram.
'''
def make_scattergram(fFrame, dFrame, iFrame, enFrame, espFrame):
    #aesthetic
    fig = plt.figure(figsize=(13,10)); ax = fig.subplots(); ax.set_facecolor('black')
    fig.suptitle('Defensive Efficiency in Top 5 Leagues in Europe for 20/21 Season', fontsize=22)
    plt.ylabel('Total Successful Interceptions During Season', fontsize=14)
    plt.xlabel('Total Tackles Attempted During Season', fontsize=14)
    legend = ['Reg.Line','Fr. Ligue 1', 'Ger. Bundesliga 1', 'Ita. Serie A',
                 'Eng. Premier League', 'Spa. La Liga']
    #scatter plotting
    plt.scatter(fFrame['Tkl'],fFrame['Int'], color='pink')
    plt.scatter(dFrame['Tkl'],dFrame['Int'], color='yellow')
    plt.scatter(iFrame['Tkl'],iFrame['Int'], color='lime')
    plt.scatter(enFrame['Tkl'],enFrame['Int'], color='cyan')
    plt.scatter(espFrame['Tkl'],espFrame['Int'], color='red')
    #regression-line
    x = np.concatenate((fFrame['Tkl'].array, dFrame['Tkl'].array, iFrame['Tkl'].array, 
                        enFrame['Tkl'].array, espFrame['Tkl'].array))
    y = np.concatenate((fFrame['Int'].array, dFrame['Int'].array, iFrame['Int'].array,
                    enFrame['Int'].array, espFrame['Int'].array))
    m,b = np.polyfit(x,y,1); plt.plot(x, m * x + b, color='white')
    #legend has to be after plotting
    ax.legend(legend)


'''
Parameters: frame, a dataframe of top 10 teams in Europe
Plots a bar graph value for each of the 10 teams included in the Europe
'''
def make_bar(frame):
    #aesthetic
    fig = plt.figure(figsize=(20,8)); ax = fig.subplots()
    plt.title('Goals Conceded by Top 10 Teams in Europe for 20/21 Season', fontsize=22)
    legend = ['French', 'Italian', 'English', 'German', 'Spanish']
    ax.set_yticks(np.arange(0,19,2)); ax.set_xticks(np.arange(10)); ax.set_xticklabels(frame['Squad'])
    plt.ylabel('Goals Conceded', fontsize=16); plt.xlabel('Teams', fontsize=16)
    #psg
    ax.bar(0, frame.at[1,'GA'], color='pink', align='center', edgecolor='black')
    #napoli
    ax.bar(1, frame.at[2,'GA'], color='lime', align='center', edgecolor='black')
    #milan
    ax.bar(2, frame.at[3,'GA'], color='lime', align='center', edgecolor='black')
    #chelsea
    ax.bar(3, frame.at[4,'GA'], color='cyan', align='center', edgecolor='black')
    #bayernMunich
    ax.bar(4, frame.at[5,'GA'], color='yellow', align='center', edgecolor='black')
    #realMadrid
    ax.bar(5, frame.at[6,'GA'], color='red', align='center', edgecolor='black')
    #dortmund
    ax.bar(6, frame.at[7,'GA'], color='yellow', align='center', edgecolor='black')
    #manCity
    ax.bar(7, frame.at[8,'GA'], color='cyan', align='center', edgecolor='black')
    #inter
    ax.bar(8, frame.at[9,'GA'], color='lime', align='center', edgecolor='black')
    #sevilla
    ax.bar(9, frame.at[10,'GA'], color='red', align='center', edgecolor='black')
    #legend 
    ax.legend(legend); ax = plt.gca(); leg = ax.get_legend()
    leg.legendHandles[2].set_color('cyan'); leg.legendHandles[2].set_edgecolor('black')
    leg.legendHandles[3].set_color('yellow'); leg.legendHandles[3].set_edgecolor('black')
    leg.legendHandles[4].set_color('red'); leg.legendHandles[4].set_edgecolor('black')


'''
Parameter: frame, a Pandas dataframe
make_vert() takes in a dataframe object and allows for the visualisation of the wins a national team
had during the specific competition. Once the graph data is plotted, gradient() is called on the data
visualization. 
'''
def make_vert(frame):
    fig = plt.figure(figsize=(17,9)); ax = fig.subplots()
    fig.suptitle('Matches won at the EURO 2020 Continental Competition', fontsize=20)
    plt.ylabel('Teams', fontsize=14)
    plt.xlabel('Fixtures Won Across Competition', fontsize=14)
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
    espFrame = to_frame('espStats.csv')
    fraFrame = to_frame('fraStats.csv'); deuFrame = to_frame('deuStats.csv')
    itaFrame = to_frame('itaStats.csv'); engFrame = to_frame('engStats.csv')
    topTeamFrame = to_frame('top10teams.csv')
    euro2020frame = to_frame('top10national.csv')
    make_scattergram(fraFrame, deuFrame, itaFrame, engFrame, espFrame)
    make_bar(topTeamFrame)
    make_vert(euro2020frame)
    plt.show()

main()