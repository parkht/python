import pandas as pd

movies = pd.read_csv("data/ml-1m/movies.dat", sep="::", names=["MovieID", "Title", "Genres"])
# print(movies)
ratings = pd.read_csv("data/ml-1m/ratings.dat", sep="::", names=["UserID", "MovieID", "Rating", "Timestamp"])
# print(ratings)
users = pd.read_csv("data/ml-1m/users.dat", sep="::", names=["UserID", "Gender", "Age", "Occupation", "Zip-code"])
# print(users)

ur = users.merge(ratings, on='UserID')
# print(ur)
data = ur.merge(movies, on='MovieID')
print(data.columns)

gender_ratings = data.pivot_table(index='Title', columns='Gender', values='Rating')
# print(gender_ratings)

ratingscnt = data.groupby('Title').size()
# print(ratingscnt)
# print(type(ratingscnt))

# print(ratingscnt.sort_values(ascending=False))
ratingcnt200 = ratingscnt[ratingscnt >= 200]
# print(ratingcnt200.index)

gender_ratings200 = gender_ratings.loc[ratingcnt200.index]
# print(gender_ratings200.sort_values(by='F',ascending=False).head(10))

# 남녀간에 호불호가 큰 영화
gender_ratings200['diff'] = (gender_ratings200['F'] - gender_ratings200['M']).abs()
# gender_ratings200['diff'] = gender_ratings200['diff'].abs()
print(gender_ratings200.sort_values(by='diff', ascending=False))

# 제목별 Rating의 표준편차 std()
movie_rating_std = data.groupby('Title')['Rating'].std()
print(movie_rating_std.loc[ratingcnt200.index].sort_values(ascending=False).head(10))



