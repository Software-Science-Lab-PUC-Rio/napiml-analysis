"""
Easy plots handler.

This module aims to facilitate the building
of some basic plots, such as Barplot, Boxplot
Likert and Wordcloud.

Author: Antonio Pedro Santos Alves
Advisor: Marcos Kalinowski
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from wordcloud import WordCloud
import plot_likert


class PlotUtils:    
    def __init__(self, df: pd.DataFrame):
        self.df = df
        # some default configurations for all seaborn plots
        sns.set_theme(style="whitegrid")
        sns.set(rc={'figure.figsize':(13.7,13.27)})


    def single_barplot(self, x_axis, y_axis, title='', x_label='', y_label='', x_label_rotation=0, color='', total_answers='', bar_orientation='horizontal'):
        """
            Draw barplots with single bars.
        """
        if color:
            barplot = sns.catplot(data=self.df, kind="bar", x=x_axis, y=y_axis, color=color, alpha=.5, linewidth=5,
                                  height=5, aspect=10/5).set(title=title)

        # use a random list of colors
        else:
            barplot = sns.catplot(data=self.df, kind="bar", x=x_axis, y=y_axis, ci="boot", palette="dark", alpha=.5, linewidth=5,
                                  height=5, aspect=10/5).set(title=title)

        
        barplot.set_xticklabels(rotation=x_label_rotation)
        barplot.despine(left=True)
        barplot.set_axis_labels(x_label, y_label)
        x_axis = barplot.ax.get_xlim()
        y_axis = barplot.ax.get_ylim()
        if bar_orientation == 'horizontal':
            barplot.ax.text((x_axis[1] - x_axis[1] * 0.2), (y_axis[0] - y_axis[0] * 0.1), total_answers)
        elif bar_orientation == 'vertical':
            barplot.ax.text((x_axis[1] - x_axis[1] * 0.2), (y_axis[1] - y_axis[1] * 0.1), total_answers)


    def single_boxplot(self, y_axis: str, outliers: bool = True, title: str = '', total_answers: str =''):
        """
            Draw a boxplot over one dimension (y-axis)
        """
        boxplot = sns.boxplot(data=self.df, y=y_axis, showfliers=outliers)
        sns.despine(offset=10, trim=True)
        
        # plot the median value - https://stackoverflow.com/a/38649932
        median_df_column = self.df[y_axis].median()
        medians = [median_df_column]
        vertical_offset = median_df_column * 0.03 # offset from median for display
        
        for xtick in boxplot.get_xticks():
            boxplot.text(xtick, medians[xtick] + vertical_offset, medians[xtick], horizontalalignment='center',
                        size='x-small', color='w', weight='semibold')

        boxplot.set(title=title)
        
        x_axis = boxplot.get_xlim()
        y_axis = boxplot.get_ylim()

        boxplot.text((x_axis[1] - x_axis[1] * 0.25), (y_axis[1] - y_axis[1] * 0.1), total_answers)


    def multi_boxplot(self, x_axis: str, y_axis: str, outliers: bool = True, title: str = ''):
        """
            Draw a boxplot over the two dimensions (x-axis and y-axis)
        """
        #draw a single boxplot - only y axis
        boxplot = sns.boxplot(data=self.df, x=x_axis, y=y_axis, showfliers=outliers)
        sns.despine(offset=10, trim=True)
        
        # plot the median value - https://stackoverflow.com/a/38649932
        medians = self.df.groupby([x_axis])[y_axis].median()
        vertical_offset = self.df[y_axis].median() * 0.03 # offset from median for display
        
        for xtick in boxplot.get_xticks():
            boxplot.text(xtick, medians[xtick] + vertical_offset, medians[xtick], horizontalalignment='center',
                        size='x-small', color='w', weight='semibold')

        boxplot.set(title=title)


    def single_violinplot(self, y_axis: str, title: str = ''):
        """
            Draw a violinplot over one dimension (y-axis)
        """
        # also show a line indicating quartiles
        sns.violinplot(data=self.df, y=y_axis, inner="quartile", linewidth=1).set(title=title)
        sns.despine(left=True)


    def single_histplot(self, x_axis: str, title: str = ''):
        """
            Draw a histplot over one dimension (y-axis)
        """
        sns.histplot(data=self.df, x=x_axis, kde=True).set(title=title)


    def heatmap(self, x_axis: str, y_axis: str, xy_match: str, order: list = [], title: str = '', fmt: str = ''):
        """
            Draw a heatmap from dataframe where 'x_axis' is the column
            which will become row, 'y_axis' is the column which will
            keep being column and 'xy_match' is the column that
            associates x to y.
        """
        
        pivot_df = self.df.pivot(x_axis, y_axis, xy_match)
        
        # reorder pivot according to the positions passed
        if len(order):
            pivot_df = pivot_df.iloc[:, order]
        
        sns.heatmap(pivot_df, annot=True, fmt=fmt, linewidths=.5).set(title=title)


    def pie_chart(self, values_column: str, labels_column: str, title: str = "", total_answers: str = ''):
        """
            Draw a piechart from a dataframe containing labels 
            and the percentage of each label.
        """
        
        #'values' contains percentages of pie - sum must not exceed 100
        values = list(self.df[values_column])
        labels = list(self.df[labels_column])

        #define Seaborn color palette to use
        colors = sns.color_palette('pastel')[0:len(values)]

        #create pie chart with matplotlib but use seaborn default color pallete
        plt.pie(values, labels=labels, colors=colors, autopct='%.0f%%')
        plt.title(title)
        
        x_axis_min, x_axis_max, y_axis_min, y_axis_max = plt.axis()
        plt.text((x_axis_max), (y_axis_min + y_axis_min * 0.05), total_answers)

        plt.show()
        


    def wordcloud(self, word_column: str, count_column: str):
        """
            Draw a wordcloud from a dataframe containing word and its importance.
        """
        text_dict = {}
        
        for _, row in self.df.iterrows():
            text_dict[row[word_column]] = row[count_column]
    
        # Define the custom color range using a LinearSegmentedColormap
        colors = ["#003f5c", "#2f4b7c", "#665191", "#a05195", "#d45087", "#f95d6a", "#ff7c43", "#ffa600"]
        cmap = LinearSegmentedColormap.from_list("custom_colormap", colors)
        
        # Create the word cloud with higher resolution
        wc = WordCloud(max_words=1000, width=2000, height=1000, colormap=cmap, background_color='white')
        wc.generate_from_frequencies(text_dict)
        
        # Create the plot basis
        plt.figure(figsize=(15, 7.5))  # Adjust the figure size if needed
        plt.imshow(wc, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    

    def likert(self, labels: list[str], use_percentage: bool = True, bar_label: bool = True):
        """
            Draw a likert from dataframe.
        """
        plot_likert.plot_likert(self.df, labels, plot_percentage=use_percentage, bar_labels=bar_label)
