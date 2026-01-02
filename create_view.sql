-- view contendo as colunas que serão usadas para análise
CREATE VIEW visao_geral AS
SELECT DISTINCT
    al.track_id,
    al.track_name,
    al.release_date,
    ar.name AS artist_name,
    ar.followers AS artist_followers,
    t.track_popularity,
    f.valence
FROM albums al
JOIN artists ar
    ON al.artist_id = ar.id
JOIN features f
    ON al.track_id = f.id
LEFT JOIN tracks t
    ON al.track_id = t.id;
