import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class GetInstructionsRequest(BaseModel):
    openai_api_key: str
    assistant_id: str

class SetInstructionsRequest(BaseModel):
    openai_api_key: str
    assistant_id: str
    instructions: str

@app.post("/get_assistant_instructions")
def get_assistant_instructions(data: GetInstructionsRequest):
    try:
        client = openai.OpenAI(api_key=data.openai_api_key)
        assistant = client.beta.assistants.retrieve(data.assistant_id)
        return {"instructions": assistant.instructions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/set_assistant_instructions")
def set_assistant_instructions(data: SetInstructionsRequest):
    try:
        client = openai.OpenAI(api_key=data.openai_api_key)
        client.beta.assistants.update(
            data.assistant_id,
            instructions=data.instructions
        )
        return {"status": "ok", "assistant_id": data.assistant_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {"message": "API working!"}
