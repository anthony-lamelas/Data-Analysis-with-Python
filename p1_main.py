# This entrypoint file to be used in development. Start by reading README.md
import p1_mean_var_std
from unittest import main

print(p1_mean_var_std.calculate([0,1,2,3,4,5,6,7,8]))

# Run unit tests automatically
main(module='p1_test_module', exit=False)