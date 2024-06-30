class StrategyRegistry:
    def __init__(self):
        self.autofocus_strategies = {}
        self.cell_identifier_strategies = {}
        self.cell_selector_strategies = {}
        self.cell_processor_strategies = {}

    def register_autofocus(self, name, strategy_class):
        self.autofocus_strategies[name] = strategy_class

    def register_cell_identifier(self, name, strategy_class):
        self.cell_identifier_strategies[name] = strategy_class

    def register_cell_selector(self, name, strategy_class):
        self.cell_selector_strategies[name] = strategy_class

    def register_cell_processor(self, name, strategy_class):
        self.cell_processor_strategies[name] = strategy_class

    def get_autofocus(self, name):
        return self.autofocus_strategies.get(name)

    def get_cell_identifier(self, name):
        return self.cell_identifier_strategies.get(name)

    def get_cell_selector(self, name):
        return self.cell_selector_strategies.get(name)

    def get_cell_processor(self, name):
        return self.cell_processor_strategies.get(name)

    def get_autofocus_names(self):
        return list(self.autofocus_strategies.keys())

    def get_cell_identifier_names(self):
        return list(self.cell_identifier_strategies.keys())

    def get_cell_selector_names(self):
        return list(self.cell_selector_strategies.keys())

    def get_cell_processor_names(self):
        return list(self.cell_processor_strategies.keys())

strategy_registry = StrategyRegistry()