from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def search_docs(query: str):
    #     Search documents by query.
    # Currently just echoes the query.
    # Later we will connect this to Elasticsearch/OpenSearch.
    return {"result": f"You searched for {query}"}
