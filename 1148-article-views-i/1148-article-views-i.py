import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    view_own_article=views[
        views['author_id']==views['viewer_id']
    ]
    unique_author=view_own_article[['author_id']].drop_duplicates()
    unique_author.columns=['id']
    return unique_author.sort_values('id')