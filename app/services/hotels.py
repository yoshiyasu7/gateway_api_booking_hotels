from httpx import AsyncClient, HTTPStatusError


async def get_hotels():
    async with AsyncClient() as client:
        try:
            response = await client.get("http://localhost:8000/hotels/")
            response.raise_for_status()
            return response.json()
        except HTTPStatusError as exc:
            return {"error": f"HTTP error: {exc.response.status_code}"}
