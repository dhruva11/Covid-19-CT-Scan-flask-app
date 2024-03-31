import sys
import uvicorn
from main import covid_ct

if __name__ == "__main__":
    uvicorn.run("main:covid_ct", host="0.0.0.0", port=7860)
