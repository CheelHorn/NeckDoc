
JWT_SECRET: str = "TEST_SECRET_DO_NOT_USE_IN_PROD"
ALGORITHM: str = "HS256"

# 60 minutes * 24 hours * 8 days = 8 days
ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"

BUFF_SIZE = 65536
