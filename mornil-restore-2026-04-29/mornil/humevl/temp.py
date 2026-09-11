import inspect
# from deepeval.models.base_model import DeepEvalBaseLLM

# print(inspect.getsource(DeepEvalBaseLLM))



from deepeval.benchmarks import HumanEval
# import inspect

# print(inspect.getsource(HumanEval))


print("\n\n\-----------\n\ninspect.getsource(HumanEval.evaluate):")
print(inspect.getsource(HumanEval.evaluate))

print("\n\n\-----------\n\ninspect.getfile(HumanEval):")
print(inspect.getfile(HumanEval))

# import your_module_name
# import deepeval
# print(deepeval.__file__)

import deepeval
print("\n\n\-----------\n\ndeepeval.__version__:")
print(deepeval.__version__)