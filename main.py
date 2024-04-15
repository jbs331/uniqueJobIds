import asyncio
import aiohttp
import json
from uuid import uuid4
import random

# Function to get a job id from a server using an asynchronous get request.
async def getJobId(session, url, jobId):
    try:
        # Execute the get request with a 10 second time span.
        async with session.get(url.format(jobId=jobId), timeout=10) as response:
            if response.status != 200:
                print(f"Failed to get job ID: {jobId}. HTTP Status: {response.status}")
                return None
            # Parse the json response.
            jsonResponse = await response.json()
            print(f"{jsonResponse}")
            return jsonResponse
    except asyncio.TimeoutError:
        print(f"Request timeout for job ID: {jobId}")
        return None
    except Exception as e:
        print(f"An error occurred while getting job ID: {jobId}. Error: {e}")
        return None

# Execute multiple asynchoronous requests.
async def main():
    # Generate a random number of requests between 1000 and 2000.
    numRequests = random.randint(1000, 2000)
    baseUrl = "https://yourapi.com/getjobdetails/{jobId}"
    jobs = []

    # Create a session to manage connections.
    async with aiohttp.ClientSession() as session:
        # Prepare tasks.
        tasks = []
        for _ in range(numRequests):
            jobId = str(uuid4())
            task = getJobId(session, baseUrl, jobId)
            tasks.append(task)
        
        # Await completion of all tasks.
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # Extract valid job ids.
        for result in results:
            if result and 'jobId' in result:
                jobs.append(result['jobId'])

    # Print the collected job ids to the console.
    print(json.dumps({'jobs': jobs}, indent=4))

if __name__ == "__main__":
    asyncio.run(main())

