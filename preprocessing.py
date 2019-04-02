#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

def process_ratings(df_ratings, fname_to_create):
    """

    """

    # Calculate ratings mean of users
    df_ratings = ratings[['movieId', 'rating']].groupby(['movieId'], as_index=False).mean()

    # Count number of ratings by movie
    df_ratings['nb_ratings'] = ratings[['userId', 'movieId']].groupby(['movieId']).count()

    df_ratings.to_csv(fname_to_create, index=False)

def process_tags(df_tags, fname_to_create):
    """

    """

    df_tags = tags[['movieId', 'userId']].groupby(['movieId'], as_index=False).count().rename(
        columns={'userId':'nb_tags'})

    df_tags['all_tags'] = tags.groupby(['movieId'], as_index=False)['tag'].progress_apply(list)
    df_tags['existing_tags'] = df_tags[['all_tags']].progress_apply(lambda line: list(filter(
        lambda tag: not genome_tags[genome_tags['tag'] == tag].empty, line['all_tags'])), axis=1)

    df_tags['existing_tagsId'] = df_tags[['existing_tags']].progress_apply(lambda line: list(map(
        lambda tag: genome_tags[genome_tags['tag'] == tag]['tagId'].iloc[0],
        line['existing_tags'])), axis=1)

    df_tags['existing_tagsRelevance'] = df_tags[['movieId', 'existing_tagsId']].progress_apply(
    lambda line: np.array(
        [*map(lambda tagId:
              genome_scores[(genome_scores['movieId'] == line.movieId) & \
                            (genome_scores['tagId'] == tagId)]['relevance'].values,
              line['existing_tagsId'])]).ravel(), axis=1)

    df_tags['mean_relevance'] = df_tags[['existing_tagsRelevance']].progress_apply(
    lambda line: line['existing_tagsRelevance'].mean(), axis=1).fillna(0)

    df_tags.to_csv(fname_to_create, index=False)



if __name__=="__main__":

    process_ratings("datasets/ratings.csv")
    process_tags("datasets/tags.csv")
