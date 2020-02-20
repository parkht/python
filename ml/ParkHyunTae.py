import pandas as pd

# 1 번-------------------------------------------------------
data = pd.read_csv('data/alcol.csv', sep=',')
datadf = pd.DataFrame(data)
datadf = datadf.set_index('State')
print(datadf.head(5))
print('--'*30)

# 2번---------------------------------------------------------
data_wine = datadf.pivot_table(index='Year', columns='State', values='Wine')
print(data_wine)
print('--'*30)

# 3번-----------------------------------------------------------
data2009 = datadf[datadf['Year']==2009]
print(data2009)
print('--'*30)

# 4번--------------------------------------------------------------
data2009 = data2009.drop('Year', axis=1)
data2009 = data2009.reset_index()
print(data2009)
print('--'*30)
# 5번--------------------------------------------------------------


def cnt_null(x):
    # print(x.shape)
    return x.shape[0] - x.count()


data2009_null = data2009.apply(cnt_null)
print(data2009_null)
data2009 = data2009.fillna(0)
print(data2009)
print('--'*30)

# 6번----------------------------------------------------------
data2009['total'] = data2009['Beer'] + data2009['Wine'] + data2009['Spirits']
print(data2009)
print('--'*30)

# 7번------------------------------------------------------------
usa = pd.read_csv('data/usa.csv')
usa_df = pd.DataFrame(usa)
usa_df['country'] = '미국'
print(usa_df)
print('--'*30)

# 8번--------------------------------------------------------------
df = usa_df.merge(data2009, left_on='State', right_on='State')
df = df.set_index('State')
print(df)
print('--'*30)

# 9번--------------------------------------------------------------
canada = pd.read_csv('data/canada.csv')
canada_df = pd.DataFrame(canada)
canada_df['country'] = '캐나다'
print(canada_df)
print('--'*30)

# 10번------------------------------------------------------------
pop = pd.concat([canada_df, usa_df], ignore_index=True)
pop = pop.set_index(['country', 'State']).sort_index(ascending=True)
print(pop)

