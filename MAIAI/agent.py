from openai import OpenAI  # Import OpenAI API client
from dotenv import load_dotenv  # Import environment variable reader

# Load environment variables
load_dotenv()

# Initialize the OpenAI client once for the entire package
client = OpenAI()

class Agent:
    """
    A class representing an AI agent that interacts with the OpenAI API for text generation tasks.

    Attributes:
        model (str): The model identifier for the OpenAI model to be used (e.g., "gpt-3.5-turbo").
        temperature (float): The temperature parameter for response randomness, ranging from 0 to 1 (default is 0.5).
        role (str): An optional description of the agent's role to guide the model's response style or perspective.
    """

    def __init__(self, model: str, temperature: float = 0.5, role: str = ""):
        """
        Initializes an instance of the Agent class with the specified model, temperature, and role.

        Args:
            model (str): The model identifier for the OpenAI model to be used.
            temperature (float): Controls response randomness; lower values make output more focused, 
                                 while higher values increase randomness (default is 0.5).
            role (str): Optional role description for the agent, which can influence the tone or perspective 
                        of responses generated by the model (default is an empty string).
        """
        self.model = model
        self.temperature = temperature
        self.role = role
