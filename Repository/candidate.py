# repository/candidate.py

class Candidate:
    def __init__(self, db):
        self.db = db

    def add_candidate(self, name, major, previous_job, years_of_experience):
        query = "INSERT INTO candidate (name, major, previous_job, years_of_experience) VALUES (%s, %s, %s, %s) RETURNING id;"
        self.db.query(query, (name, major, previous_job, years_of_experience))
        return self.db.cur.fetchone()['id']

    def get_all_candidates(self):
        query = "SELECT id, name, major, previous_job, years_of_experience FROM candidate;"
        self.db.query(query)
        return self.db.fetch()
