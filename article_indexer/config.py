from contextlib import contextmanager
from typing import Callable, Dict, List


class Config:
    _instance = None
    _observers = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.DEBUG = False
            cls._instance.LENIENT = False
            cls._instance.ENVIRONMENT = "development"
        return cls._instance

    def __setattr__(self, key, value):
        old = getattr(self, key, None)
        super().__setattr__(key, value)
        if key in ["DEBUG", "LENIENT", "ENVIRONMENT"] and old != value:
            self._notify(key, old, value)

    def _notify(self, key, old, new):
        for callback in self._observers:
            callback(key, old, new)

    def subscribe(self, callback):
        self._observers.append(callback)

    def unsubscribe(self, callback: Callable[[str, bool, bool], None]):
        if callback in self._observers:
            self._observers.remove(callback)

    @classmethod
    @contextmanager
    def temporary_config(cls, **overrides):
        instance = cls()
        changes = {}

        for key, new_value in overrides.items():
            old_value = getattr(instance, key)
            setattr(instance, key, new_value)
            changes[key] = old_value
            instance._notify(key, old_value, new_value)

        try:
            yield
        finally:
            for key, old_value in changes.items():
                setattr(instance, key, old_value)
                instance._notify(key, overrides[key], old_value)

    @classmethod
    def reset(cls):
        cls._instance = None
        cls._observers = []


config = Config()
