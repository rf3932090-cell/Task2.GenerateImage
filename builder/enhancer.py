class PromptEnhancer:
    def enhance(self, user_prompt: str) -> str:
        raise NotImplementedError
    
class DictionaryEnhancer(PromptEnhancer):

    LOCATION_LIBRARY = {
        "mazandaran": "Caspian Sea, lush forests, humid climate, coastal scenery",
    }

    def enhance(self, user_prompt: str) -> str:
        prompt = user_prompt.lower()
        extra_details = []
        for location, description in self.LOCATION_LIBRARY.items():
            if location in prompt:
                extra_details.append(description)

        return ",".join(extra_details)