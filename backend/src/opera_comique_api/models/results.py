from pydantic import BaseModel

from opera_comique_api.models.edges import IsPerformance
from opera_comique_api.models.nodes import Performance, Work


class SimpleResult(BaseModel):
    work: Work
    performance: Performance
    source: IsPerformance

    @classmethod
    def _match(cls) -> str:
        return "MATCH (w:Work)-[r:IS_PERFORMED]->(p:Performance)"

    @classmethod
    def _return(cls) -> str:
        return "RETURN {work:w, performance: p, source: r} as result"

    @classmethod
    def _statements(cls) -> tuple[str]:
        return cls._match(), cls._return()
