reddit_project/
├── data_extraction/            # Extraction scripts from Reddit API
│   ├── reddit_scraper.py       # Main Reddit scraping script
│   └── utils.py                # Utility functions for scraping
├── db/                         # PostgreSQL related files
│   ├── models/                 # SQLAlchemy models for your tables (if using ORM)
│   ├── migration/              # DB migrations if you are using Alembic
│   └── schema.sql              # SQL schema to create your tables
├── dbt/                        # DBT transformations
│   ├── models/                 # Intermediate models for transformations
│   ├── analysis/               # Any DBT analysis files
│   ├── seeds/                  # For any static data (e.g., reference tables)
│   └── dbt_project.yml         # DBT project config file
├── api/                        # FastAPI backend (serving data to frontend)
│   ├── main.py                 # FastAPI app setup
│   ├── endpoints/              # API endpoints (Search, Stats, etc.)
│   └── models/                 # Data models for FastAPI (Pydantic schemas)
├── frontend/                   # Frontend (using Streamlit)
│   ├── pages/                  # Streamlit page scripts
│   │   ├── search_page.py      # Page for searching posts
│   │   └── stats_page.py       # Page for stats (like most posted tools)
│   └── components/             # Reusable components (e.g., search bar)
├── airflow/                    # Airflow related files
│   ├── dags/                   # Airflow DAGs
│   │   ├── reddit_dag.py       # DAG for scraping Reddit and processing
│   │   └── dbt_dag.py          # DAG for triggering DBT transformations
│   ├── Dockerfile              # Dockerfile for Airflow image
│   ├── requirements.txt        # Dependencies for Airflow (e.g., airflow, python packages)
│   └── airflow.cfg             # Airflow configuration file
├── docker/                     # Docker-specific configurations
│   ├── Dockerfile.postgres     # Dockerfile for PostgreSQL image (if custom)
│   └── entrypoint.sh           # Entry script for initializing DB and services (optional)
├── docker-compose.yml          # Docker Compose file to set up Airflow, PostgreSQL, etc.
├── requirements.txt            # Python dependencies for general use (including FastAPI)
└── README.md                   # Project overview and instructions
