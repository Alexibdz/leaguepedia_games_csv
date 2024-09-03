from mwrogue.esports_client import EsportsClient

class LeaguepediaSite:
    def __init__(self, limit=500):
        self._site = None
        self.limit = limit

    @property
    def site(self):
        if not self._site:
            self._load_site()

        return self._site

    def _load_site(self):
        self._site = EsportsClient("lol")

    def query(self, **kwargs) -> list:
        result = []

        # We check if we hit the API limit
        while len(result) % self.limit == 0:
            result.extend(
                self.site.cargo_client.query(
                    limit=self.limit, offset=len(result), **kwargs
                )
            )
            if not result:
                break

        return result

leaguepedia = LeaguepediaSite()