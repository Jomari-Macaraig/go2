from abc import ABC, abstractmethod


class BaseChannel(ABC):

    @abstractmethod
    def __call__(self, notification, *args, **kwargs):
        pass
