from models.request_models import GenerateRequest
from models.analysis_models import PromptAnalysisResult
from services.analyzer_service import PromptAnalysisService

class PromptAnalyzer:

    def __init__(self):
        self.analysis_service = PromptAnalysisService()

    def analyze(self, request: GenerateRequest) -> PromptAnalysisResult:

        result = self.analysis_service.analyze(request.model_dump())
        return PromptAnalysisResult(**result)
   