from dotenv import load_dotenv
import os

load_dotenv()

class Envs:

    negocios = os.getenv("API_NEGOCIOS")