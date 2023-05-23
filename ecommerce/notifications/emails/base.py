from abc import ABC, abstractmethod


class BaseEmail(ABC):
    subject = None

    def generate_greeting(self, name):
        return f"Hi {name},\n"

    def generate_signature(self):
        return f"\nThank you"

    @abstractmethod
    def generate_message(self, meta):
        pass

    def __call__(self, meta, *args, **kwargs):
        name = meta.get("name")

        return (
            self.subject,
            f"{self.generate_greeting(name=name)} {self.generate_message(meta=meta)} {self.generate_signature()}"
        )
