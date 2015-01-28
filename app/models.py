from app import fake

def generate_shows(num):
    """
    Function generates a number of shows using the faker python package.
    """
    shows = []

    for i in range(num):
        shows.append({
            'date': fake.dateTimeBetween('now', '+1y'),
            'description': fake.text()
        })

    shows.sort(key=lambda x: x['date'])

    return shows

shows = generate_shows(10)