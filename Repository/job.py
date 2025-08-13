# repository/job.py

class Job:
    def __init__(self, db):
        self.db = db

    def add_job(self, skills, requirements, position, location):
        query = "INSERT INTO job (skills, requirements, position, location) VALUES (%s, %s, %s, %s) RETURNING id;"
        self.db.query(query, (skills, requirements, position, location))
        return self.db.cur.fetchone()['id']

    def get_available_jobs(self):
        query = "SELECT id, skills, requirements, position, location FROM job;"
        self.db.query(query)
        return self.db.fetch()
