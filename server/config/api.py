from ninja import NinjaAPI

api = NinjaAPI(
    title="Aftertone API",
    version="0.1.0",
    docs_url="/docs",
)

@api.get("/")
def root(request):
    return {
        "name": "Aftertone API",
        "status": "ok",
        "version": "0.1.0",
    }

@api.get("/health")
def health(request):
    return {
        "status": "healthy",
    }
