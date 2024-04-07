from typing import Sequence, Tuple


class Module:
    def __init__(self):
        self.training = True  # Default mode is training
        self.parameters_dict = {}  # Dictionary to store parameters
        self.modules_list = []  # List to store sub-modules

    def train(self) -> None:
        """
        Set the mode of this module and all descendent modules to train.
        """
        self.training = True
        for module in self.modules_list:
            module.train()

    def eval(self) -> None:
        """
        Set the mode of this module and all descendent modules to eval.
        """
        self.training = False
        for module in self.modules_list:
            module.eval()

    def named_parameters(self) -> Sequence[Tuple[str, 'Parameter']]:
        """
        Collect all the parameters of this module and its descendants.
        Returns:
            Sequence[Tuple[str, Parameter]]: The name and Parameter of each ancestor parameter.
        """
        all_parameters = []
        for name, param in self.parameters_dict.items():
            all_parameters.append((name, param))
        for module in self.modules_list:
            all_parameters.extend(module.named_parameters())
        return all_parameters

    def parameters(self) -> Sequence['Parameter']:
        """
        Enumerate over all the parameters of this module and its descendants.
        Returns:
            Sequence[Parameter]: List of all parameters.
        """
        all_parameters = []
        for param in self.parameters_dict.values():
            all_parameters.append(param)
        for module in self.modules_list:
            all_parameters.extend(module.parameters())
        return all_parameters
