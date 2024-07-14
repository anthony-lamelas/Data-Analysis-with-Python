# This entrypoint file to be used in development. Start by reading README.md
import p2_demographic_data_analyzer
from unittest import main

# Test your function by calling it here
p2_demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
main(module='p2_test_module', exit=False)