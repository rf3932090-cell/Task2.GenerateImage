from models.request_models import GenerateRequest
from models.analysis_models import AnalyzeResponse, AnalyzerOutput
from services.analyzer_service import PromptAnalysisService

class PromptAnalyzer:

    def __init__(self):
        self.analysis_service = PromptAnalysisService()

    def analyze(self, request: GenerateRequest) -> AnalyzerOutput:

        result = self.analysis_service.analyze(request.model_dump())
        print(result)
        return AnalyzerOutput(**result)
   