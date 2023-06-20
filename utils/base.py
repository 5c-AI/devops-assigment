from dotenv import load_dotenv
import os

# Load environment variables
dotenv_path = '.env'
load_dotenv(dotenv_path)


def get_env():
    return { "ENV_TYPE" : os.getenv('ENV') }