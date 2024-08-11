from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECT']
ssl_cert_path = "us-east-1-bundle.pem"

engine = create_engine(
    db_connection_string,
    connect_args={
        "ssl": {
            "ssl_ca": ssl_cert_path
        }
    }
)
def load_jobs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM job"))
      columns = result.keys()
      job = [dict(zip(columns, row)) for row in result]
      return job  
