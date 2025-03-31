from groq import Groq
from dotenv import load_dotenv
from crewai import LLM


load_dotenv()


## --------------------- CrewAI GEMINI Testing --------------------- ##

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7
)

print( "Gemini models Response \n\n" , llm.call("Hi"))



## --------------------- Groq Testing --------------------- ##
client = Groq()

groq_chat_completion = client.chat.completions.create(
    #
    # Required parameters
    #
    messages=[

        {"role": "system", "content": "you are a helpful assistant."},
        { "role": "user", "content": "Write a two line joke on AI"}
    ],

    # The language model which will generate the completion.
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    max_completion_tokens=1024,
    top_p=1,
    stop=None,
    stream=False
            )

print( "Groq Output \n\n ",groq_chat_completion.choices[0].message.content)