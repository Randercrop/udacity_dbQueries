import psycopg2

DBNAME = "news"
popularArtists = '''
SELECT
    count(path) as num,
    path
FROM log
WHERE
    status like '200%' and
    method like 'GET'
GROUP BY path
ORDER BY num desc limit 3 offset 1'''

popularAuthors = '''
SELECT
    count(artiAuth.name) as num,
    name
FROM (articles join authors on articles.author=authors.id) as artiAuth
JOIN log on position(artiAuth.slug in log.path) > 0
WHERE
    log.status like '200%' and
    method like 'GET'
GROUP BY name
ORDER BY num desc'''

highRateOfFail = '''
SELECT
    allStatus.statusDate,
    allStatus.bad_status_count::double precision
        / allStatus.total_status_count::double precision
        * 100 as fractionFailed
FROM
    (SELECT
        date(log.time) AS statusDate,
        count(log.status)
            AS total_status_count,
        count(log.status) filter (where log.status like '404%')
            AS bad_status_count
    FROM log
    GROUP BY date(log.time)
    ORDER BY statusDate)
AS allStatus
ORDER BY fractionFailed desc'''

if __name__ == "__main__":
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(popularArtists)
    topArticles = cursor.fetchall()
    print ('\nThe top 3 articles are:')
    for i in topArticles:
        print (
            '%(key1)s with a total of %(key2)s views'
            % {'key1': i[1], 'key2': i[0]})

    cursor.execute(popularAuthors)
    topAuthors = cursor.fetchall()
    print ('\nThe ranking of best authors of all time are:')
    for i in topAuthors:
        print(
            '%(author)s with a lifetime total of %(totalViews)s views'
            % {'author': i[1], 'totalViews': i[0]})

    cursor.execute(highRateOfFail)
    daysFailed = cursor.fetchall()
    print('\nThe days with errors greater than 1% are:')
    for i in daysFailed:
        if(i[1] > 1):
            print(
                '%(date)s with a fail rate of %(failPercentage)f\n'
                % {'date': i[0], 'failPercentage': i[1]})

    db.close()
