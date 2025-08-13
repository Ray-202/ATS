# repository/application.py

class Application:
    def __init__(self, db):
        self.db = db

    def add_application(self, candidate_id, job_id, status):
        query = "INSERT INTO application (candidate_id, job_id, status) VALUES (%s, %s, %s) RETURNING id;"
        self.db.query(query, (candidate_id, job_id, status))
        application_id = self.db.cur.fetchone()

        if application_id:
            return application_id.get('id')  # Return the 'id' field from the fetched row
        else:
            return None  # Handle case where no application_id was fetched
