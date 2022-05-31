'''
Francisco Figueroa
Section Leader: Elias Anastopoulos
11/22/2021
ISTA 131
multi_league_scatter.py
Creates a scattergram from two related variables along with a regression line of the projection for
said values of defensive efficacy in European soccer leagues.
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
    fig = plt.figure(figsize=(14,11)); ax = fig.subplots(); ax.set_facecolor('black')
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
main() takes in nothing, calls all functions.
'''
def main():
    espFrame = to_frame('espStats.csv')
    fraFrame = to_frame('fraStats.csv'); deuFrame = to_frame('deuStats.csv')
    itaFrame = to_frame('itaStats.csv'); engFrame = to_frame('engStats.csv')
    make_scattergram(fraFrame, deuFrame, itaFrame, engFrame, espFrame)
    plt.show()

main()