import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2

df['overweight'] = (df['weight'] / ((df['height']/100) **2) > 25).astype(int)

# 3
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1


# 4
def draw_cat_plot():
    # 5
    value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=value_vars, var_name='variable', value_name='value')
    
    # 6
    df_cat_count = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7
    cat_plot = sns.catplot(
        x='variable', y='total', hue='value', col='cardio', 
        data=df_cat_count, kind='bar', height=5, aspect=1
    )

    # 8
    fig = cat_plot.figure


    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]


    # 12
    corr = df_heat.corr()

    # 13
    mask = np.triu(corr)

    # 14
    fig, ax = plt.subplots()

    # 15

    ax = sns.heatmap(corr, mask=mask, annot=True, fmt='0.1f', square=True)


    # 16
    fig.savefig('heatmap.png')
    plt.show()
    return fig









