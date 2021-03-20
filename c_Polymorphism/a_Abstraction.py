"""
Abstraction is a process of hiding the implementation details and showing only functionality to the user.

By default Python dose not support Abstraction
for implementation we need to import {ABC} & {abstractmethod} from {abc} module

and inherit the ABC

An abstract class must have to at least one abstract method
.

"""
from abc import ABC, abstractmethod


class Calculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass  # you must have to user pass keyword for abstractmethod


class Mathematics(Calculator):

    def add(self, a, b):
        return a + b


math = Mathematics()

print(math.add(34, 4))  # Output: 38
