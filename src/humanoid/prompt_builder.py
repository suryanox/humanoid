from io import StringIO

from humanoid.session_context import SessionContext


class PromptBuilder:
    def __init__(self, session_context: SessionContext):
        self._session_context = session_context
        self._builder = StringIO()


    def build(self):
        self._add_template()
        self._add_context()
        self._add_persona()
        self._add_adherence()
        self._add_rules()
        return self._builder.getvalue()

    def _add_template(self):
        pass

    def _add_context(self):
        pass

    def _add_persona(self):
        pass

    def _add_adherence(self):
        pass

    def _add_rules(self):
        pass