'''
Francisco Figueroa
Section Leader: Elias Anastopoulos
11/22/2021
ISTA 131
top_team_bar.py
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
Parameters: frame, a dataframe of top 10 teams in Europe
Plots a bar graph value for each of the 10 teams included in the Europe
'''
def make_bar(frame):
    #aesthetic
    fig = plt.figure(figsize=(15,8)); ax = fig.subplots()
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
main() takes in nothing, calls all functions.
'''
def main():
    topTeamFrame = to_frame('top10teams.csv')
    make_bar(topTeamFrame)
    plt.show()

main()